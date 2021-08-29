#!/usr/bin/env python3

import sys
import time
import shutil
import argparse
import subprocess

from re import sub
from os import walk
from os.path import dirname, abspath, join, getmtime, isfile, basename

# base directory for the git repository clone
repo_dir = dirname(dirname(abspath(__file__)))

# test to see if asciidoctor is available
if not shutil.which("asciidoctor"):
    sys.exit("ERROR: asciidoctor is not installed or is not in your PATH")


def main():
    """
    Walk through the repository directory looking for asciidoc files
    to convert to HTML. Only files with the .adoc file extension that
    have been modified since the last run will be converted.
    """
    parser = argparse.ArgumentParser(description="convert asciidoc to html")
    parser.add_argument(
        "-f", "--force", action="store_true", help="Force regeneration of all files"
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Suppress output"
    )
    parser.add_argument(
        "-w", "--watch", action="store_true", help="Watch for changes"
    )
    args = parser.parse_args()

    if args.watch:
        while True:
            build(repo_dir, args)
            time.sleep(1)
    else:
        build(repo_dir, args)


def build(repo_dir, args):
    """
    Process the contents of the given repository directory with the 
    given command line arguments.
    """
    for dir_name, dirs, files in walk(repo_dir):
        for filename in files:
            if filename.endswith(".adoc"):
                adoc_path = join(dir_name, filename)
                adoc_mtime = getmtime(adoc_path)

                html_path = sub(r"\.adoc$", ".html", adoc_path)
                html_mtime = getmtime(html_path)

                if args.force or html_mtime < adoc_mtime:
                    asciidoc(adoc_path, html_path, args.quiet)


def asciidoc(adoc_file, html_file, quiet=False):
    """
    Convert an asciidoc file to HTML using asciidoctor or asciidoctor-revealjs.
    Returns True if no errors or warnings were generated and False if they
    were.
    """

    if basename(adoc_file) == "slides.adoc":
        cmd = ["asciidoctor-revealjs", adoc_file, "-o", html_file]
    else:
        cmd = ["asciidoctor", adoc_file, "-o", html_file]

    if not quiet:
        print(adoc_file)

    result = subprocess.run(cmd, capture_output=True)
    if result.stderr:
        print(f"{adoc_file} - {result.stderr.decode('utf8')}")
        return False
    else:
        return True


if __name__ == "__main__":
    main()
