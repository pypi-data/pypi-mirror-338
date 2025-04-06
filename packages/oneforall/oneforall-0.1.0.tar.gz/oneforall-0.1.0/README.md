# OneForAll

[![PyPI version](https://badge.fury.io/py/oneforall.svg)](https://badge.fury.io/py/oneforall) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) Pack and unpack project source code into a single, structured text file. Ideal for sharing, archiving snapshots, and interacting with Large Language Models (LLMs) like Gemini, Claude, or GPT.

## The Problem

Sharing multi-file codebases or providing them as context to LLMs can be cumbersome. You might need to zip archives, copy-paste multiple files, or struggle with context window limits. LLMs often work best when they can see the relevant code structure and content together.

## The Solution

`oneforall` traverses your project directory, reads the text-based source files, and concatenates them into one `.oneforall` file. Each file's content is clearly marked with its original path. It intelligently ignores files based on default patterns (like `.git`, `__pycache__`, `.venv`) and your project's `.gitignore` file (or a custom ignore file).

You can then easily share this single file or paste its content into an LLM prompt. `oneforall` can also unpack this bundle file back into the original directory structure.

**Key Features:**

- Packs relevant project files into a single text file (`.oneforall`).
- Unpacks a `.oneforall` file back into a directory structure.
- Uses `.gitignore` syntax for excluding files (reads `.gitignore` by default, supports custom ignore files).
- Includes sensible default ignores for common temporary files, caches, and VCS directories.
- Provides clear markers showing the original path of each file within the bundle.
- Skips likely binary files.
- Simple Command-Line Interface (CLI).
- Can also be used programmatically.

## Installation

```bash
pip install oneforall
```

## Usage

`oneforall` provides two main commands: `bundle` and `unbundle`.

### Bundling a Project (`bundle`)

This command packs a project directory into a single `.oneforall` file.

**Basic Syntax:**

```bash
oneforall bundle <source_directory> [options]
```

**Arguments:**

- `<source_directory>`: (Required) The path to the project directory you want to bundle. Use `.` for the current directory.

**Options:**

- `-o OUTPUT`, `--output OUTPUT`: Specifies the path for the output `.oneforall` file.
  - If omitted, the default is `<source_directory_name>.oneforall` in the current working directory (e.g., bundling `my_project/` creates `my_project.oneforall`).
  - If `<source_directory>` is `.`, the default output is `<current_directory_name>.oneforall`.
- `-i IGNORE`, `--ignore IGNORE`: Path to a custom `.gitignore`-style file. Patterns in this file are added to the patterns found in the standard `.gitignore` within the `source_directory` (if one exists).
- `-h`, `--help`: Show the help message for the `bundle` command.

**Examples:**

1.  **Bundle the current directory into the default output file:**

    ```bash
    oneforall bundle .
    # Creates 'oneforall.oneforall' (if run in the project root)
    ```

2.  **Bundle a specific project directory into a named output file:**

    ```bash
    oneforall bundle ./my_cool_project -o cool_project_bundle.ofa
    ```

3.  **Bundle the current directory using an additional custom ignore file:**
    ```bash
    oneforall bundle . --ignore ./.custom_ignores
    ```

### Unbundling a Project (`unbundle`)

This command extracts the contents of a `.oneforall` file back into a directory structure.

**Basic Syntax:**

```bash
oneforall unbundle <bundle_file> -o <output_directory> [options]
```

**Arguments:**

- `<bundle_file>`: (Required) The path to the `.oneforall` file you want to unpack.

**Options:**

- `-o OUTPUT`, `--output OUTPUT`: (Required) The path to the target directory where the project structure will be created. The directory will be created if it doesn't exist.
- `-h`, `--help`: Show the help message for the `unbundle` command.

**Examples:**

1.  **Unpack a bundle into a new directory:**

    ```bash
    oneforall unbundle cool_project_bundle.ofa -o ./unpacked_project
    # Creates ./unpacked_project/ and extracts the contents there
    ```

2.  **Unpack a bundle into an existing directory (will overwrite existing files with the same name):**
    ```bash
    oneforall unbundle project.oneforall -o ./existing_output_dir
    ```

## Programmatic Usage

You can also use `oneforall` directly within your Python code:

```python
from oneforall import pack, unpack
from pathlib import Path

# Define paths
source_dir = Path("./my_project")
bundle_file = Path("my_project.oneforall")
output_dir = Path("./unpacked_project")

try:
    # Pack the project
    pack(source_dir, bundle_file)
    print(f"Project packed into {bundle_file}")

    # Unpack the project
    unpack(bundle_file, output_dir)
    print(f"Project unpacked into {output_dir}")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```
