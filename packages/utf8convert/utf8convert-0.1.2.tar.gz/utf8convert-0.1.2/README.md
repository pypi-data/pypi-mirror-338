[![PyPI version](https://img.shields.io/pypi/v/utf8convert.svg)](https://pypi.org/project/utf8convert/)

# utf8convert

A command-line utility to recursively convert source files to UTF-8 encoding.

Supports:
- `.cpp`, `.h`, `.hpp` files by default
- Any custom extensions via `--extensions`
- Logging and summary reports (JSON and terminal)
- Dry-run mode
- Default and user-defined subdirectory exclusions

## 📦 GitHub

Project repository: [https://github.com/yhbyhb/utf8convert](https://github.com/yhbyhb/utf8convert)

---

## 🚀 Installation

You can install the package locally after downloading or cloning the repo:

```bash
pip install .
```

This will install the executable command: `utf8convert`

---

## 💻 Usage

```bash
utf8convert [DIRECTORY] [OPTIONS]
```

### Options:

- `--dry-run`  
  Preview files to convert without making changes.

- `--extensions [.ext1 .ext2 ...]`  
  List of file extensions to process (default: `.cpp .h .hpp`).

- `--exclude-dirs [dir1 dir2 ...]`  
  Relative paths of subdirectories to skip.  
  Defaults: `.git`, `.vs`, `vcpkg_installed`, and any dot-prefixed folders.

- `--json-output PATH`  
  Write a summary report as JSON to the specified path.

---

## 📌 Examples

### 🔍 Dry-run all C++ headers and sources
```bash
utf8convert ./src --dry-run
```

### 🛠 Convert files with `.c` and `.cc` extensions too
```bash
utf8convert ./src --extensions .cpp .h .hpp .c .cc
```

### 🧾 Generate a JSON report
```bash
utf8convert ./mycode --json-output utf8_summary.json
```

### 🚫 Skip specific folders
```bash
utf8convert ./codebase --exclude-dirs build third_party .cache
```

---

## 🧪 Test Locally

```bash
hatch run python -m utf8convert.cli ./your/code --dry-run
```

Let me know if you want to contribute or need help automating PyPI publishing.
