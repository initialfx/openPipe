#!/usr/bin/python
# Copyright: Jihyun Nam
# Version: 1.0

import os
import sys
import argparse
from pathlib import Path

def print_tree(directory: Path, current_level: int = 0, dirs_only: bool = False):
    """
    Recursively prints a directory tree structure.
    """
    # Print the current directory
    indent = ' ' * 4 * current_level
    print(f"{indent}{directory.name}/")

    try:
        # Use iterdir for more efficient path processing
        for path in sorted(directory.iterdir()):
            if path.is_dir():
                # Recurse into directories
                print_tree(path, current_level + 1, dirs_only)
            elif not dirs_only and path.is_file():
                # Print files if dirs_only is False
                sub_indent = ' ' * 4 * (current_level + 1)
                print(f"{sub_indent}{path.name}")
    except PermissionError:
        print(f"{' ' * 4 * (current_level + 1)}[Permission Denied]")

def main():
    parser = argparse.ArgumentParser(
        description="A professional directory tree view utility for OpenPipe."
    )
    parser.add_argument(
        "path", 
        type=str, 
        nargs="?", 
        default=".", 
        help="Target directory path to display (default: current directory)"
    )
    parser.add_argument(
        "-d", "--dirs-only", 
        action="store_true", 
        help="Display directories only, hide files"
    )
    parser.add_argument(
        "-v", "--version", 
        action="version", 
        version="OpenPipe Treeview 1.0"
    )

    args = parser.parse_args()

    target_path = Path(args.path)

    if not target_path.exists():
        print(f"Error: Path '{target_path}' does not exist.")
        sys.exit(1)

    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a directory.")
        sys.exit(1)

    print_tree(target_path, dirs_only=args.dirs_only)

if __name__ == "__main__":
    main()
