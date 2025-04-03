import argparse
from .core import extract_docs, copy_llm_format
import sys # To exit gracefully

def main():
    parser = argparse.ArgumentParser(
        description="""DocPorter: Documentation Extractor Tool

Extracts documentation files from GitHub repositories or local folders.
Supports READMEs (any case) and common documentation formats
(.md, .mdx, .rst, .txt) by default. Use include/exclude patterns
for custom file selection.""",
        formatter_class=argparse.RawTextHelpFormatter, # Preserves formatting in help text
        epilog="""Examples:

  Extract from GitHub repo (default output: repo-name-docs):
    docporter extract https://github.com/user/repo.git

  Extract from local folder into specific directory:
    docporter extract ./my-project -o ./output-docs

  Extract only markdown and Python files from a repo:
    docporter extract <source> --include "*.md" "*.py"

  Extract default docs but exclude anything in 'tests' or 'build' dirs:
    docporter extract <source> --exclude "tests/*" "build/*"

  Copy LLM format for specific file types to clipboard, excluding configs:
    docporter copy <source> --include "*.py" "*.js" --exclude "*.config.js"

Notes:
  - Patterns use shell-style wildcards (e.g., *, ?, []).
  - Exclude patterns take precedence over include patterns and default types.
  - Default doc types (.md, .rst, .txt, README*) are always considered unless
    excluded. --include patterns *add* to this set.
  - Paths in patterns are relative to the repository root.
""",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title='Commands',
        description='Choose a command to run:',
        help="Use {extract,copy} -h for command-specific help",
        required=True # Makes selecting a command mandatory (Python 3.7+)
    )

    # --- Extract Subcommand ---
    extract_parser = subparsers.add_parser(
        "extract",
        help="Extract docs to an output folder.",
        description="Extracts documentation files based on default types and include/exclude patterns.",
        formatter_class=argparse.RawTextHelpFormatter,
        # Add epilog here if needed, or let it inherit from main parser if sufficient
    )
    # --- Arguments for 'extract' ---
    extract_parser.add_argument(
        "source",
        metavar='SOURCE',
        type=str,
        help="GitHub repository URL (https/ssh/git) or path to local folder."
    )
    extract_parser.add_argument(
        "-o", "--output",
        metavar='OUTPUT_DIR',
        type=str,
        default=None,
        help="Custom output directory name/path. (Default: [repo_name]-docs)"
    )
    extract_parser.add_argument(
        "--include",
        "-i",
        nargs='+', # Allows one or more patterns
        metavar='PATTERN',
        type=str,
        default=None,
        help="Glob patterns for files/dirs to *additionally* include (e.g., \"*.py\", \"docs/*\")."
    )
    extract_parser.add_argument(
        "--exclude",
        "-e",
        nargs='+', # Allows one or more patterns
        metavar='PATTERN',
        type=str,
        default=None,
        help="Glob patterns for files/dirs to exclude (e.g., \"test/*\", \"*.log\"). Takes precedence."
    )


    # --- Copy Subcommand ---
    copy_parser = subparsers.add_parser(
        "copy",
        help="Format docs for LLM and copy to clipboard.",
        description="Copies filtered documentation content to the clipboard in an XML format suitable for LLM ingestion.",
        formatter_class=argparse.RawTextHelpFormatter,
        # Add epilog here if needed
    )
    # --- Arguments for 'copy' ---
    copy_parser.add_argument(
        "source",
        metavar='SOURCE',
        type=str,
        help="GitHub repository URL (https/ssh/git) or path to local folder."
    )
    copy_parser.add_argument(
        "--include",
        "-i",
        nargs='+', # Allows one or more patterns
        metavar='PATTERN',
        type=str,
        default=None,
        help="Glob patterns for files/dirs to *additionally* include (e.g., \"*.py\", \"docs/*\")."
    )
    copy_parser.add_argument(
        "--exclude",
        "-e",
        nargs='+', # Allows one or more patterns
        metavar='PATTERN',
        type=str,
        default=None,
        help="Glob patterns for files/dirs to exclude (e.g., \"test/*\", \"*.log\"). Takes precedence."
    )

    # --- Parse Arguments ---
    # Handle case where only 'docporter' is run (now handled by required=True if Python 3.7+)
    # Still good practice for broader compatibility or if required=False is ever used.
    if len(sys.argv) <= 1:
         parser.print_help(sys.stderr)
         sys.exit(1)

    try:
        args = parser.parse_args()
    except SystemExit as e:
         # Exit gracefully if argparse raises SystemExit (e.g., for -h)
         # Avoid printing the full traceback for standard help exit.
         sys.exit(e.code)


    # --- Execute Command ---
    # Access arguments directly from the parsed 'args' namespace
    # Argparse ensures the correct arguments are present based on the chosen command
    if args.command == "extract":
        extract_docs(
            args.source,
            output_folder=args.output, # This will be None if not provided for extract
            include_patterns=args.include,
            exclude_patterns=args.exclude
        )
    elif args.command == "copy":
        copy_llm_format(
            args.source,
            include_patterns=args.include,
            exclude_patterns=args.exclude
        )
    # else: # Not strictly necessary if subparsers required=True
    #     parser.print_error(f"Invalid command: {args.command}")
    #     sys.exit(1)

# Standard boilerplate for entry point
if __name__ == "__main__":
    main()