# repo_sanitize/git_tools.py
import subprocess
import logging
from pathlib import Path

logger = logging.getLogger("repo_sanitizer")

def create_backup_branch(repo_path: Path, private: bool = False):
    branch_name = "private-backup-before-sanitization" if private else "public-backup-before-sanitization"
    logger.info(f"Creating backup branch '{branch_name}'...")

    try:
        subprocess.run(
            ["git", "checkout", "-b", branch_name],
            cwd=repo_path,
            check=True,
            capture_output=True,
            text=True
        )
        subprocess.run(
            ["git", "push", "-u", "origin", branch_name],
            cwd=repo_path,
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to create backup branch: {e.stderr}")
        raise
