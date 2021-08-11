#!/usr/bin/env python3

import sys

from re import sub
from os import walk
from os.path import dirname, abspath, join
from subprocess import run

repo_dir = dirname(dirname(abspath(__file__)))

def asciidoc(adoc_file):
    html_file = sub(r'\.adoc$', '.html', adoc_file)
    cmd = ['asciidoctor', adoc_file, '-o', html_file]
    result = run(cmd, capture_output=True)
    if result.stderr:
        print(f"{adoc_file} - {result.stderr.decode('utf8')}") 

def main():
    for dir_name, dirs, files in walk(repo_dir):
        for filename in files:
            if filename.endswith('.adoc'):
                asciidoc(join(dir_name, filename))

if __name__ == "__main__":
    main()
                
