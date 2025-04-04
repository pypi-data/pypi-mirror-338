# RepoSanitize

**RepoSanitize** is a command-line tool and Python library for identifying and removing sensitive files and secrets from Git repositories. It is designed to help developers and teams sanitize their codebases before sharing, archiving, or open-sourcing.

---

## 🚀 Features

- 🔍 Detects secrets using regex and file patterns
- 🧠 Scans common config, credential, and token files
- 🛡️ Automatically updates `.gitignore`
- 🧬 Supports custom search paths
- 🗃️ Creates backup branches before rewriting history
- 🧹 Uses `git filter-branch` to scrub files from all commits
- 🎨 Beautiful CLI output with `rich`

---

## 🧰 Installation

```bash
poetry add repo-sanitize
# or install globally
poetry install && poetry run python -m repo_sanitize.cli
```

---

## 📦 Usage

```bash
python -m repo_sanitize <path-to-repo> [--paths path1 path2 ...] [--private] [--verbose]
```

### Examples

```bash
# Sanitize a full repo
python -m repo_sanitize ~/projects/myrepo

# Target specific subfolders
python -m repo_sanitize . --paths config/ secrets/

# Create a private backup branch before cleaning
python -m repo_sanitize . --private
```

---

## 📄 Documentation

Full API documentation is available at:
👉 **[ReadTheDocs](https://repo-sanitize.readthedocs.io/)**

Includes:
- API Reference for `RepoSanitizer`
- CLI options
- Git integration helpers

---

## 🧪 Development

```bash
poetry install
nox -s lint tests docs
```

### Linting, Type Checks, and Docs Preview
```bash
nox -s lint
nox -s typecheck
nox -s docs
```

---

## 📘 License

MIT License © 2025 William R. Astley / Pr1m8
