# inst326

This repository contains public course materials for **INST326: Object-Oriented Programming for Information Studies** at the University of Maryland. INST326 introduces students to the design, testing and use of object oriented software with the Python programming language.

You can find the public site at:

https://umd-ischool-inst326.github.io/inst326/

It is organized into weekly [modules] that have a suggested ordering but which can be reordered as desired. Each module contains an overview of the module's  learning objectives, presentation slides and exercises. We also have a private repository of exercises that are not for distribution on the public web. Please [get in touch] if you are interested in seeing those.

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

If you would like to add or modify a module you will need to clone the repository:

    git clone https://github.com/umd-ischool-inst326/inst326/
    cd inst326/modules

If adding a new module you can copy the module template:

    cp -r template my_new_module

Edit the content using existing modules as a guide.

## Build

The build process is a small Python program which runs [asciidoctor] on the input [asciidoc] files to create html files. So you will need to make sure you have [asciidoctor] installed and available in your system path.

    scripts/build.py

When you are finished adding or modifying content you  will want to commit 
your changes and push them up to GitHub where they are served from:

    git commit -m 'more awesome content 🦄' -a
    git push

## Questions?

If you have any questions or comments please send them our way via the GitHub issue tracker. We'd love to incorporate new and improved content if you have ideas.

## License

The contents of this repository are copyright University of Maryland and made available with the [CC-BY-NC-SA] License. 

[asciidoctor]: https://asciidoctor.org/
[asciidoc]: https://en.wikipedia.org/wiki/AsciiDoc
[CC-BY-NC-SA]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[modules]: https://umd-ischool-inst326.github.io/inst326/modules/
[get in touch]: https://github.com/umd-ischool-inst326/inst326/issues/
