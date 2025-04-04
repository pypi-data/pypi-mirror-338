# repo_sanitize/config.py
import re

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
    re.compile(r'(?i)(api_?key|secret|access_?token|client_?secret)\s*[=:]\s*[\'"]?([A-Za-z0-9_\-/+=]{20,})[\'"]?', re.IGNORECASE),

    # Private Keys
    re.compile(r'-----BEGIN (RSA|EC|DSA) PRIVATE KEY-----'),

    # Database Connection Strings
    re.compile(r'(?i)(postgres|mysql|mongodb)://.*:.*@', re.IGNORECASE),

    # Cloud Provider Credentials
    re.compile(r'(?i)(aws_?access_?key|gcp_?private_?key|azure_?connection_?string)\s*[=:]\s*[\'"]', re.IGNORECASE),

    # Email and Password Combinations
    re.compile(r'(?i)email\s*[=:]\s*[\'"]+.*[\'"]+.*password\s*[=:]\s*[\'"]+', re.IGNORECASE)
]
