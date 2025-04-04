> ⚠️ **Note**: This README and project structure were generated with the help of a large language model (LLM). Please review before publishing or deploying.

[![PyPI version](https://img.shields.io/pypi/v/utf8convert.svg)](https://pypi.org/project/utf8convert/)

# utf8convert

A command-line utility to recursively convert source files to UTF-8 encoding.

Supports:
- `.cpp`, `.h`, `.hpp` files by default  
- Any custom extensions via `--extensions`  
- Logging with timestamped filenames  
- Dry-run mode  
- Skip ASCII files (optional)  
- JSON summary output (optional)  
- Separate counts for intentionally skipped files and error cases  
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
  Preview files to convert without modifying anything.

- `--extensions [.ext1 .ext2 ...]`  
  List of file extensions to process (default: `.cpp .h .hpp`).

- `--exclude-dirs [dir1 dir2 ...]`  
  Relative paths of subdirectories to skip.  
  Defaults: `.git`, `.vs`, `vcpkg_installed`, and any dot-prefixed folders.

- `--skip-ascii`  
  Skip files detected with ASCII encoding (they're usually already compatible with UTF-8).

- `--json-output PATH`  
  Write a summary report as JSON to the specified path (not printed in logs).

---

## 📊 Summary Breakdown

The summary will show:
- Total scanned
- Already UTF-8
- Converted or would-convert
- Skipped (intentionally ignored, like ASCII)
- Errors (files that failed to decode/convert)

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

### ⚙️ Skip ASCII-encoded files
```bash
utf8convert ./legacy --skip-ascii
```

---

## 🧪 Test Locally

```bash
hatch run python -m utf8convert.cli ./your/code --dry-run
```

> ⚠️ **Note**: This README and project structure were generated with the help of a large language model (LLM). Please review before publishing or deploying.
