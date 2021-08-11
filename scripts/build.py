#!/usr/bin/env python3

import sys
import json
import shutil
import subprocess

from re import sub
from os import walk
from os.path import dirname, abspath, join, getmtime, isfile

# base directory for the git repository clone
repo_dir = dirname(dirname(abspath(__file__)))

# test to see if asciidoctor is available
if not shutil.which('asciidoctor'):
    sys.exit('ERROR: asciidoctor is not installed or is not in your PATH')

def main():
    """
    Walk through the repository directory looking for asciidoc files
    to convert to HTML. Only files with the .adoc file extension that 
    have been modified since the last run will be converted.
    """
    history = History()
    for dir_name, dirs, files in walk(repo_dir):
        for filename in files:
            if filename.endswith('.adoc'):
                path = join(dir_name, filename)
                if history.is_modified(path):
                    asciidoc(path)

def asciidoc(adoc_file):
    """
    Convert an asciidoc file to HTML using asciidoctor or asciidoctor-revealjs.
    Returns True if no errors or warnings were generated and False if they 
    were.
    """

    html_file = sub(r'\.adoc$', '.html', adoc_file)
    if adoc_file == "slides.adoc":
        cmd = ['asciidoctor-revealjs', adoc_file, '-o', html_file]
    else:
        cmd = ['asciidoctor', adoc_file, '-o', html_file]
    result = subprocess.run(cmd, capture_output=True)
    if result.stderr:
        print(f"{adoc_file} - {result.stderr.decode('utf8')}") 
        return False
    else:
        return True

class History:

    def __init__(self):
        self.file = join(repo_dir, '.history')
        if isfile(self.file):
            self.mtimes = json.load(open(self.file))
        else:
            self.mtimes = {}

    def is_modified(self, path):
        mtime = getmtime(path)
        if path in self.mtimes and mtime > self.mtimes[path]:
            result = True
        elif path not in self.mtimes:
            result = True
        else:
            result = False

        if result:
            self.mtimes[path] = mtime
            self.write()
        
        return result

    def write(self):
        with open(self.file, 'w') as fh:
            json.dump(self.mtimes, fh, indent=2)

if __name__ == "__main__":
    main()
