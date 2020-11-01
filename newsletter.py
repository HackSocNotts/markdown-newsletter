#!/usr/bin/env python3

"""
Some license. I'm thinking of making the program itself open
source but the style file should be closed source to protect
our branding somewhat.
"""

import sys
from os.path import isfile


def help_and_exit():
    print("Usage:")
    print("  newsletter [-h|--help] style markdown")
    print("  Please specify a Style file and a Markdown file to convert.")
    print("\n  --help | -h | -?\n      Show this help and exit.")
    exit(1)


def markdown_converter(style_path, markdown_path):
    print("Converting markdown to HTML...")
    exit(0)


# Program entry
if __name__ == "__main__":
    # Display help for -h, --help, -?, or no args.
    if len(sys.argv) == 1 or sys.argv[1] == "--help" or sys.argv[1] == "-h" or sys.argv[1] == "-?":
        help_and_exit()
    
    # Catch unrecognised options
    if sys.argv[1].startswith("--") or sys.argv[1].startswith("-"):
        print("Unrecognised option:", sys.argv[1], "\n")
        help_and_exit()
    
    # Checks files are accessable.
    if isfile(sys.argv[-2]) and isfile(sys.argv()):
        print(sys.argv[-2], "is a file.")
        markdown_converter(sys.argv[-2], sys.argv[-1])
    else:
        print("Cannot access {} or {}".format(sys.argv[-2], sys.argv[-1]))
        help_and_exit()

print("Uncaught case!")
exit(1)
