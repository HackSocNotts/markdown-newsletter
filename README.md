# HackSoc Markdown Newsletter Converter
Converts a markdown file to the HTML for sending as a newsletter using an existing template.

## REQUIREMENTS
 - A recent version of Python 3 (Only tested on Python 3.8.6)
 - [Marko](https://marko-py.readthedocs.io/en/latest/) `pip3 install marko`

## USAGE
`python3 newsletter.py [template file] [markdown file]`

The template file should be a HTML file with all of the styling and such included.
Put the string `<!--REPLACED_WITH_CONTENT-->` into the body where you want the content
to go and it will be replaced with the content from the markdown.

Otherwise the markdown is standard [CommonMark](https://spec.commonmark.org/).

## TODO
 - Look into better (more markdown like) way to add buttons.
 - Add Docs into program help output.
 - Add `[-v|--verbose]` flag to print HTML while program is running.