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

    md_file = open(markdown_path)
    markdown_raw = md_file.read()
    md_file.close()
    
    contents = parse_markdown(markdown_raw)

    sty_file = open(style_path)
    style_raw = sty_file.read()
    sty_file.close()

    html = to_html(contents, style_raw)

    newsletter_output = open("newsletter.html", "wt")
    newsletter_output.write(html)
    newsletter_output.close()

    exit(0)


def parse_markdown(markdown_raw):
    contents = {"title": "<h1 class='title'>This is a title</h1>", "subtitle": "<h4>This is a subtitle</h4>", "content": "<p>This is some content</p>"}
    return contents


def to_html(contents, style):
    html_file = open("template.html")
    initial_html = html_file.read()
    html_file.close()
    contents.update({"style": style})
    return initial_html.format(contents)


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
