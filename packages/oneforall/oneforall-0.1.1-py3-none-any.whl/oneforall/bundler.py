# src/oneforall/bundler.py
"""Core logic for packing a project into a single bundle file."""

import logging
from pathlib import Path
from typing import List, Optional

import pathspec # type: ignore # pathspec is not typed yet

from .defaults import (DEFAULT_IGNORE_PATTERNS, START_MARKER_TEMPLATE,
                       END_MARKER_TEMPLATE)

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def _is_likely_text_file(file_path: Path) -> bool:
    """Check if a file is likely text-based by trying to decode it."""
    try:
        # Read a small chunk to check encoding
        with file_path.open("r", encoding="utf-8") as f:
            f.read(512) # Read up to 512 bytes
        return True
    except (UnicodeDecodeError, OSError):
        # OSError can occur for various reasons like permissions,
        # but UnicodeDecodeError strongly suggests non-text or wrong encoding.
        return False
    except Exception as e:
        logger.warning(f"Could not read file {file_path} to check type: {e}")
        return False # Assume not text if error occurs

def pack(source_dir: Path, output_file: Path, ignore_file: Optional[Path] = None) -> None:
    """
    Packs the contents of source_dir into output_file, respecting ignores.

    Args:
        source_dir: The root directory of the project to bundle.
        output_file: The path to the bundle file to create.
        ignore_file: Optional path to a .gitignore style file for exclusions.
    """
    if not source_dir.is_dir():
        logger.error(f"Source directory '{source_dir}' not found or is not a directory.")
        raise FileNotFoundError(f"Source directory '{source_dir}' not found.")

    # --- Ignore Patterns ---
    ignore_patterns: List[str] = list(DEFAULT_IGNORE_PATTERNS) # Start with defaults

    # Check for standard .gitignore in source root first
    default_gitignore = source_dir / ".gitignore"
    if default_gitignore.is_file():
        logger.info(f"Using standard '.gitignore' file found in '{source_dir}'")
        try:
            with default_gitignore.open("r", encoding="utf-8") as f:
                ignore_patterns.extend(f.read().splitlines())
        except Exception as e:
            logger.warning(f"Could not read {default_gitignore}: {e}")

    # Check for custom ignore file (overrides/adds to default .gitignore)
    if ignore_file:
        if ignore_file.is_file():
            logger.info(f"Using custom ignore file: '{ignore_file}'")
            try:
                with ignore_file.open("r", encoding="utf-8") as f:
                    # Add custom patterns; pathspec handles duplicates/precedence
                    ignore_patterns.extend(f.read().splitlines())
            except Exception as e:
                logger.warning(f"Could not read custom ignore file {ignore_file}: {e}")
        else:
            logger.warning(f"Custom ignore file '{ignore_file}' not found.")

    # Filter out empty lines and comments, and strip trailing comments/whitespace
    filtered_patterns = []
    for p in ignore_patterns:
        line = p.strip()
        if line and not line.startswith('#'):
            # Strip trailing comments after whitespace
            pattern_part = line.split('#', 1)[0].strip()
            if pattern_part:
                filtered_patterns.append(pattern_part)

    spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, filtered_patterns)

    # --- File Iteration and Bundling ---
    logger.info(f"Bundling project from '{source_dir}' into '{output_file}'...")
    bundled_files_count = 0

    try:
        with output_file.open("w", encoding="utf-8") as outfile:
            # Use rglob to recursively find all items (files and directories)
            for item_path in source_dir.rglob("*"):
                relative_path = item_path.relative_to(source_dir)
                relative_path_str = str(relative_path.as_posix()) # Use posix paths for consistency

                # Check against ignore patterns - match against relative path
                if spec.match_file(relative_path_str):
                    logger.debug(f"Ignoring '{relative_path_str}' due to ignore rules.")
                    continue

                # We only bundle files
                if not item_path.is_file():
                    continue

                # Basic check for text files - skip likely binaries
                if not _is_likely_text_file(item_path):
                    logger.info(f"Skipping likely binary file: '{relative_path_str}'")
                    continue

                # Read file content
                try:
                    content = item_path.read_text(encoding="utf-8")
                    logger.debug(f"Bundling '{relative_path_str}'")

                    # Write start marker, content, and end marker
                    outfile.write(START_MARKER_TEMPLATE.format(filepath=relative_path_str) + "\n")
                    outfile.write(content)
                    # Ensure a newline before the end marker if file didn't end with one
                    if not content.endswith('\n'):
                         outfile.write('\n')
                    outfile.write(END_MARKER_TEMPLATE.format(filepath=relative_path_str) + "\n\n") # Add extra newline for readability
                    bundled_files_count += 1

                except Exception as e:
                    logger.warning(f"Could not read or write file '{relative_path_str}': {e}")

    except Exception as e:
        logger.error(f"Failed to create bundle file '{output_file}': {e}")
        # Clean up potentially incomplete output file
        if output_file.exists():
             output_file.unlink()
        raise

    logger.info(f"Successfully bundled {bundled_files_count} files into '{output_file}'.")