# repo_sanitize/cli.py
import argparse
import logging
from .core import RepoSanitizer

def main():
    parser = argparse.ArgumentParser(description="Sanitize a Git repo by removing sensitive files and secrets.")
    parser.add_argument("repo_path", help="Path to the Git repository")
    parser.add_argument("--paths", nargs="*", help="Specific subpaths to scan")
    parser.add_argument("--private", action="store_true", help="Create a private backup branch")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()
    if args.verbose:
        logging.getLogger("repo_sanitizer").setLevel(logging.DEBUG)

    sanitizer = RepoSanitizer(args.repo_path, args.paths)
    sanitizer.sanitize_repository(private_backup=args.private)
