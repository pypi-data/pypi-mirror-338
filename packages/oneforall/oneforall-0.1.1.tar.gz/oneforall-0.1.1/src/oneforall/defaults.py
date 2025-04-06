# src/oneforall/defaults.py
"""Default configuration and constants."""

# Default patterns to ignore, similar to a common .gitignore
# Using PathSpec pattern syntax
DEFAULT_IGNORE_PATTERNS = [
    # Version control
    ".git/",
    ".hg/",
    ".svn/",

    # Python cache and artifacts
    "__pycache__/",
    "*.py[cod]",
    "*$py.class",
    ".pytest_cache/",
    ".mypy_cache/",
    "*.egg-info/",
    ".eggs/",
    "*.egg",
    "dist/",
    "build/",
    "wheels/",
    "*.so", # Compiled extensions

    # Virtual environments
    ".venv/",
    "venv/",
    "ENV/",
    "env/",
    ".env",
    "env.bak",
    ".envrc",

    # OS generated files
    ".DS_Store",
    "Thumbs.db",

    # IDE specific files
    ".idea/",
    ".vscode/",
    "*.swp",
    "*.swo",
    "*.swn",

    # Common logs and temp files
    "*.log",
    "*.tmp",
    "*.bak",

    # Bundler's own output
    "*.pybundle",
    "*.filebundle",
    "*.oneforall", # Added new default extension
]

# Markers for the bundle file format
START_MARKER_TEMPLATE = "--- START FILE: {filepath} ---"
END_MARKER_TEMPLATE = "--- END FILE: {filepath} ---"

# Default output bundle filename
DEFAULT_BUNDLE_FILENAME = "project.oneforall" # Changed default extension 