# src/oneforall/cli.py
"""Command-line interface for OneForAll."""

import argparse
from pathlib import Path
import sys

from . import pack, unpack, __version__
from .defaults import DEFAULT_BUNDLE_FILENAME

def main() -> None:
    parser = argparse.ArgumentParser(
        description=f"OneForAll v{__version__}: Pack or unpack project files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Bundle current directory into 'project.oneforall', using .gitignore
  oneforall bundle .

  # Bundle 'my_project/' into 'my_app.ofa' (example custom extension)
  oneforall bundle my_project/ -o my_app.ofa

  # Bundle current directory, using a custom ignore file
  oneforall bundle . --ignore .customignore

  # Unpack 'my_app.ofa' into 'output_project/' directory
  oneforall unbundle my_app.ofa -o output_project/
"""
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # --- Bundle command ---
    parser_bundle = subparsers.add_parser("bundle", help="Pack a directory into a single bundle file.")
    parser_bundle.add_argument(
        "source_dir",
        type=Path,
        help="The source directory to bundle.",
    )
    parser_bundle.add_argument(
        "-o", "--output",
        type=Path,
        default=None, # Default is calculated based on source_dir name
        help=f"Output bundle file path (default: <source_dir_name>/{DEFAULT_BUNDLE_FILENAME}).",
    )
    parser_bundle.add_argument(
        "-i", "--ignore",
        type=Path,
        default=None,
        help="Path to a custom .gitignore-style file to use for exclusions (adds to default .gitignore if present).",
    )

    # --- Unbundle command ---
    parser_unbundle = subparsers.add_parser("unbundle", help="Unpack a bundle file into a directory structure.")
    parser_unbundle.add_argument(
        "bundle_file",
        type=Path,
        help="The .pybundle file to unpack.",
    )
    parser_unbundle.add_argument(
        "-o", "--output",
        type=Path,
        required=True, # Output directory is required for unpacking
        help="The target directory to unpack the project into.",
    )

    args = parser.parse_args()

    try:
        if args.command == "bundle":
            output_file = args.output
            if output_file is None:
                # Default output: <source_dir_name>.pybundle in the current dir,
                # or 'project.pybundle' if source_dir is '.'
                source_name = args.source_dir.resolve().name
                if source_name == '.': # Handle bundling current directory
                   source_name = Path.cwd().name
                # Use the default filename from defaults module
                output_file = Path(f"{source_name}.{DEFAULT_BUNDLE_FILENAME.split('.')[-1]}")
                print(f"Output file not specified, defaulting to: '{output_file}'")

            pack(args.source_dir.resolve(), output_file.resolve(), args.ignore.resolve() if args.ignore else None)

        elif args.command == "unbundle":
            unpack(args.bundle_file.resolve(), args.output.resolve())

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()