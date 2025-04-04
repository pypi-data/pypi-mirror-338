import os
import re
import json
import pathlib
import subprocess
import shutil
import logging
from typing import List, Optional, Dict, Any
from rich.console import Console
from rich.table import Table
from rich.logging import RichHandler
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)
logger = logging.getLogger("repo_sanitizer")

# Expanded list of sensitive file patterns
SENSITIVE_FILE_PATTERNS = [
    # Credential and configuration files
    "*.env", "*.ini", "*.json", 
    "*.pem", "*.p12", "*.crt", "*.key", 
    "*.cfg", "*.config", 
    # Cloud provider specific credential files
    "*credentials*", 
    "*secret*", 
    # Development and deployment configs
    "*.yaml", "*.yml", 
    "*secrets*",
    # Specific cloud provider files
    ".aws/credentials", 
    ".gcloud/credentials.json",
    # CI/CD configuration files
    ".github/workflows/*.yml",
    ".gitlab-ci.yml",
]

# Enhanced regex patterns for detecting sensitive information
SENSITIVE_PATTERNS = [
    # API Keys and Secrets
    re.compile(r'(?i)(api_?key|secret|access_?token|client_?secret)\s*[=:]\s*[\'"]?([A-Za-z0-9_\-\/+=]{20,})[\'"]?', re.IGNORECASE),
    
    # Private Keys
    re.compile(r'-----BEGIN (RSA|EC|DSA) PRIVATE KEY-----'),
    
    # Database Connection Strings
    re.compile(r'(?i)(postgres|mysql|mongodb)://.*:.*@', re.IGNORECASE),
    
    # Cloud Provider Credentials
    re.compile(r'(?i)(aws_?access_?key|gcp_?private_?key|azure_?connection_?string)\s*[=:]\s*[\'"]', re.IGNORECASE),
    
    # Email and Password Combinations
    re.compile(r'(?i)email\s*[=:]\s*[\'"].*[\'"].*password\s*[=:]\s*[\'"]', re.IGNORECASE)
]

class RepoSanitizer:
    def __init__(self, repo_path: str, specific_paths: Optional[List[str]] = None):
        """
        Initialize the RepoSanitizer with a repository path.
        
        :param repo_path: Path to the Git repository
        :param specific_paths: Optional list of specific paths to scan
        """
        self.repo_path = pathlib.Path(repo_path).resolve()
        self.specific_paths = specific_paths
        self.console = Console()
        self.sensitive_files = []

    def find_sensitive_files(self) -> List[pathlib.Path]:
        """
        Find files matching sensitive patterns in the repository.
        
        :return: List of sensitive files found
        """
        sensitive_files = []
        paths_to_scan = (
            [self.repo_path / path for path in self.specific_paths] 
            if self.specific_paths 
            else [self.repo_path]
        )

        for scan_path in paths_to_scan:
            # Scan for files in the current path and all subdirectories
            for pattern in SENSITIVE_FILE_PATTERNS:
                for file_path in scan_path.rglob(pattern):
                    # Exclude .git directory
                    if '.git' not in file_path.parts:
                        # Check file contents for sensitive patterns
                        if self._scan_file_for_secrets(file_path):
                            sensitive_files.append(file_path)

        return sensitive_files

    def _scan_file_for_secrets(self, file_path: pathlib.Path) -> bool:
        """
        Scan a file for sensitive content using regex patterns.
        
        :param file_path: Path to the file to scan
        :return: True if sensitive content is found, False otherwise
        """
        try:
            # For large files, only scan the first 1MB
            with file_path.open("r", encoding="utf-8", errors="ignore") as f:
                content = f.read(1024 * 1024)  # Read first 1MB
                for pattern in SENSITIVE_PATTERNS:
                    if pattern.search(content):
                        logger.warning(f"Sensitive content detected in {file_path}")
                        return True
        except Exception as e:
            logger.error(f"Error scanning {file_path}: {e}")
        return False

    def create_backup_branch(self, private: bool = False):
        """
        Create a backup branch before modifying Git history.
        
        :param private: Whether to create a private backup branch
        """
        branch_name = "private-backup-before-sanitization" if private else "public-backup-before-sanitization"
        logger.info(f"Creating backup branch '{branch_name}'...")
        
        try:
            subprocess.run(
                ["git", "checkout", "-b", branch_name], 
                cwd=self.repo_path, 
                check=True, 
                capture_output=True, 
                text=True
            )
            subprocess.run(
                ["git", "push", "-u", "origin", branch_name], 
                cwd=self.repo_path, 
                check=True, 
                capture_output=True, 
                text=True
            )
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to create backup branch: {e.stderr}")
            raise

    def update_gitignore(self):
        """
        Update .gitignore to ensure sensitive files are not tracked.
        """
        gitignore_path = self.repo_path / ".gitignore"
        existing_entries = set()
        
        if gitignore_path.exists():
            with gitignore_path.open("r", encoding="utf-8") as f:
                existing_entries = set(f.read().splitlines())
        
        with gitignore_path.open("a", encoding="utf-8") as f:
            for pattern in SENSITIVE_FILE_PATTERNS:
                entry = f"**/{pattern}"
                if entry not in existing_entries:
                    f.write(f"\n{entry}")
                    logger.info(f"Added {entry} to .gitignore")

    def sanitize_repository(self, private_backup: bool = False):
        """
        Perform full repository sanitization.
        
        :param private_backup: Whether to create a private backup branch
        """
        logger.info("Starting repository sanitization...")
        
        # Find sensitive files
        self.sensitive_files = self.find_sensitive_files()
        
        if self.sensitive_files:
            # Display sensitive files
            table = Table(title="Detected Sensitive Files")
            table.add_column("File Path", justify="left", style="cyan")
            table.add_column("Action", justify="center", style="yellow")
            
            for file in self.sensitive_files:
                table.add_row(str(file.relative_to(self.repo_path)), "Mark for removal")
            
            self.console.print(table)
            
            # Update .gitignore
            self.update_gitignore()
        
        # Create backup branch
        self.create_backup_branch(private=private_backup)
        
        # Sanitize Git history (you might want to use BFG or filter-branch)
        self._sanitize_git_history()
        
        logger.info("Repository sanitization complete.")

    def _sanitize_git_history(self):
        """
        Sanitize Git history to remove sensitive information.
        This is a basic implementation and might need customization.
        """
        logger.info("Sanitizing Git history...")
        
        try:
            # Remove sensitive files from Git history
            for file in self.sensitive_files:
                relative_path = str(file.relative_to(self.repo_path))
                subprocess.run(
                    ["git", "filter-branch", "--force", "--index-filter", 
                     f"git rm --cached --ignore-unmatch '{relative_path}'", 
                     "--prune-empty", "--tag-name-filter", "cat", "--", "--all"],
                    cwd=self.repo_path,
                    check=True,
                    capture_output=True,
                    text=True
                )
            
            # Clean up and compact repository
            subprocess.run(
                ["git", "for-each-ref", "--format=%(refname)", "refs/original/"],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            
            subprocess.run(
                ["git", "gc", "--aggressive", "--prune=now"],
                cwd=self.repo_path,
                check=True,
                capture_output=True,
                text=True
            )
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Error sanitizing Git history: {e.stderr}")
            raise

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Sanitize a Git repository by removing sensitive files and secrets.")
    parser.add_argument("repo_path", help="Path to the Git repository")
    parser.add_argument("--paths", nargs="*", help="Specific paths to scan within the repository")
    parser.add_argument("--private", action="store_true", help="Create a private backup branch")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    
    args = parser.parse_args()
    
    # Set logging level based on verbosity
    if args.verbose:
        logging.getLogger("repo_sanitizer").setLevel(logging.DEBUG)
    
    try:
        sanitizer = RepoSanitizer(args.repo_path, args.paths)
        sanitizer.sanitize_repository(private_backup=args.private)
    except Exception as e:
        logger.error(f"Sanitization failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()