# inst326

This repository contains public course materials for **INST326: Object-Oriented Programming for Information Science** at the University of Maryland.

You can find the public site at:

    https://umd-ischool-inst326.github.io/inst326/

It is organized into thematic modules that have a default ordering but which can be reordered as needed. Each module contains an overview of the module's  learning objectives, presentation slides and exercises.

## Overview

The repository uses the following directories for course content:

* **modules:** contains a sub-directory for each course module
* **syllabi**: includes current and previous course syllabi
* **style**: code style guide for the course

The following directories are used for managing the content:

* **scripts**: utilities for processing the course materials
* **lib**: third party software like reveal.js
* **css**: local stylesheets
* **includes**: reusable HTML fragments

## Add Content

If you would like to add a module you will need to clone the repository:

    git clone https://github.com/umd-ischool-inst326/inst326/
    cd inst326/modules

Then copy the module template:

    cp -r template my_new_module

Edit the content using existing modules as a guide.

## Build

The build process is a small Python program which runs [asciidoctor] on the input [asciidoc] files to create html files. So you will need to make sure you have installed [asciidoctor].

    scripts/build.py

## Questions?

If you have any questions or comments please send them our way via the GitHub issue tracker. We'd love to incorporate new and improved content if you have ideas.

## License

The contents of this repository are copyright University of Maryland and made available with the [CC-BY-NC-SA] License. 

[asciidoctor]: https://asciidoctor.org/
[asciidoc]: https://en.wikipedia.org/wiki/AsciiDoc
[CC-BY-NC-SA]: http://creativecommons.org/licenses/by-nc-sa/4.0/
