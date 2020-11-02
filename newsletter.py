#!/usr/bin/env python3

"""
Some license. I'm thinking of making the program itself open
source but the template file should be closed source to protect
our branding somewhat.
"""

import sys
from os.path import isfile

import marko


def help_and_exit():
    print("Usage:")
    print("  newsletter [-h|--help] style markdown")
    print("  Please specify a Style file and a Markdown file to convert.")
    print("\n  --help | -h | -?\n      Show this help and exit.")
    exit(1)


def markdown_converter(template_path, markdown_path):
    print("Converting markdown to HTML...")
    md_file = open(markdown_path)
    markdown_raw = md_file.read()
    md_file.close()
    content = parse_markdown(markdown_raw)
    html = to_html(template_path, content)
    newsletter_output = open("newsletter.html", "wt")
    newsletter_output.write(html)
    newsletter_output.close()
    print("Done!")
    exit(0)


def parse_markdown(markdown_raw):
    content = marko.convert(markdown_raw)
    print("######## Marko start ########")
    print(content)
    print("########  Marko end  ########")
    return content


def to_html(template_path, content):
    html_file = open("template.html")
    initial_html = html_file.read()
    html_file.close()
    html_out = initial_html.replace("<!--REPLACED_WITH_CONTENT-->", content)
    return html_out


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
    if isfile(sys.argv[-2]) and isfile(sys.argv[-1]):
        markdown_converter(sys.argv[-2], sys.argv[-1])
    else:
        print("Cannot access {} or {}".format(sys.argv[-2], sys.argv[-1]))
        help_and_exit()

print("Uh Oh! Uncaught case.")
exit(1)
