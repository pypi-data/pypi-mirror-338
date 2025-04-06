# src/oneforall/unbundler.py
"""Core logic for unpacking a bundle file back into a project structure."""

import logging
import re
from pathlib import Path

from .defaults import START_MARKER_TEMPLATE, END_MARKER_TEMPLATE

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Prepare regex patterns from templates, making filepath capture generic
# Escape potential regex characters in templates and replace placeholder
start_marker_re = re.escape(START_MARKER_TEMPLATE).replace(r"\{filepath\}", r"(.+?)")
end_marker_re = re.escape(END_MARKER_TEMPLATE).replace(r"\{filepath\}", r"(.+?)")

# Regex to find a full file block: START MARKER \n CONTENT \n END MARKER \n\n
# Using re.DOTALL so '.' matches newlines within the content
# Using non-greedy matching `(.*?)` for content
# Assuming markers are on their own lines as written by pack()
FILE_BLOCK_RE = re.compile(
    rf"^{start_marker_re}\n(.*?)\n^{end_marker_re}\n\n?", # Allow optional final newline
    re.MULTILINE | re.DOTALL
)

def unpack(bundle_file: Path, output_dir: Path) -> None:
    """
    Unpacks a bundle file into a directory structure.

    Args:
        bundle_file: The path to the .pybundle file.
        output_dir: The directory where the project structure will be created.
    """
    if not bundle_file.is_file():
        logger.error(f"Bundle file '{bundle_file}' not found.")
        raise FileNotFoundError(f"Bundle file '{bundle_file}' not found.")

    logger.info(f"Unpacking '{bundle_file}' into directory '{output_dir}'...")

    try:
        # Create output directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)

        bundle_content = bundle_file.read_text(encoding="utf-8")
        unpacked_files_count = 0

        for match in FILE_BLOCK_RE.finditer(bundle_content):
            start_filepath = match.group(1)
            content = match.group(2)
            end_filepath = match.group(3)

            if start_filepath != end_filepath:
                logger.warning(
                    f"Mismatched markers found: START='{start_filepath}', END='{end_filepath}'. Skipping block."
                )
                continue

            relative_path = Path(start_filepath)
            target_file_path = output_dir / relative_path

            logger.debug(f"Unpacking '{start_filepath}' to '{target_file_path}'")

            # Create parent directories for the file
            target_file_path.parent.mkdir(parents=True, exist_ok=True)

            # Write the content to the file
            target_file_path.write_text(content, encoding="utf-8")
            unpacked_files_count += 1

        logger.info(f"Successfully unpacked {unpacked_files_count} files into '{output_dir}'.")

    except Exception as e:
        logger.error(f"Failed to unpack bundle file '{bundle_file}': {e}")
        raise 