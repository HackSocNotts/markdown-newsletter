#!/usr/bin/env python3

# Copyright (c) 2020 HackSoc Nottingham
# License: MIT License

import sys
from os.path import isfile
from marko import convert
from premailer import transform


def help_and_exit():
    print("Usage:")
    print("  newsletter [-h|--help] template markdown")
    print("  Please specify a Template file and a Markdown file to convert.")
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
    content = convert(markdown_raw)
    return content


def to_html(template_path, content):
    html_file = open(template_path)
    initial_html = html_file.read()
    html_file.close()
    full_html = initial_html.replace("<!--REPLACED_WITH_CONTENT-->", content)
    html_out = transform(full_html)  # Inlines CSS and does a couple other email HTML tweaks.
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
