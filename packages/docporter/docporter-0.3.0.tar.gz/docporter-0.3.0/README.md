# Doc Porter

A Python package to extract documentation files from GitHub repositories and local folders.

## Features

- **GitHub Support**:

  - Clones repositories (shallow clone)
  - Handles various GitHub URL formats
  - Automatically cleans up after cloning

- **Local Folder Support**:

  - Processes documentation files from local directories
  - Validates path existence and permissions

- **Documentation Extraction**:

  - Recognizes .md, .mdx, .rst, .txt files
  - Automatically includes README files
  - Preserves directory structure in output
  - Supports file pattern filtering

- **LLM Integration**:

  - Formats documentation in XML for LLM ingestion
  - Copies formatted content to clipboard

- **CLI Interface**:
  - Simple command-line usage
  - Comprehensive help messages
  - Robust error handling

## Installation

Install directly from PyPI:

```bash
pip install docporter
```

Or install from source:

```bash
git clone https://github.com/aatitkarki/docporter
cd docporter
pip install .
```

## Usage

### Extract Documentation

Basic extraction from GitHub:

```bash
docporter extract https://github.com/user/repo.git
```

With custom output directory:

```bash
docporter extract https://github.com/user/repo.git -o ./my-docs
```

With file pattern filters:

```bash
docporter extract https://github.com/user/repo.git --include "*.md" "*.py" --exclude "tests/*"
```

Basic local extraction:

```bash
docporter extract /path/to/local/docs
```

With custom output and patterns:

```bash
docporter extract /path/to/local/docs -o ./output --include "README*" "docs/*.md"
```

### Copy Documentation for LLM

Basic copy from local folder:

```bash
docporter copy /path/to/local/docs
```

Copy with pattern filters:

```bash
docporter copy /path/to/local/docs --include "*.py" --exclude "test_*"
```

Copy from GitHub repo:

```bash
docporter copy https://github.com/user/repo.git
```

## Options

- `-o, --output OUTPUT_DIR`: Custom output directory (default: [repo_name]-docs)
- `--include PATTERN`: Glob patterns for additional files to include
- `--exclude PATTERN`: Glob patterns for files to exclude (takes precedence)

## Pattern Matching

- By default, includes: `.md`, `.mdx`, `.rst`, `.txt` files and `README*`
- Patterns use shell-style wildcards: `*`, `?`, `[]`
- Paths are relative to repository root
- Exclude patterns override include patterns and default types

## Development

Run tests:

```bash
pytest
```

## License

MIT
