FoxXO Game Design Document
==========================

This repository contains the FoxXO game design document. FoxXO is a free and
open-source example of tic-tac-toe. The game design document describes in detail
the design considerations of the game.

The latest version of the game design document is hosted here:
[FoxXO Game Design Document](https://j-richey.github.io/project-documentation/foxxo-gdd/)


## Building
This documentation is rendered using [Sphinx](https://www.sphinx-doc.org/en/master/).
The following applications are required to build this documentation:

* Python 3.6 or newer
* inkscape
* plantuml
* LibreOffice
* A LaTeX toolchain
* Sphinx

On Ununtu / Debian system the required packages can be installed and
documentation built with:

```
$ sudo apt install texlive-full inkscape plantuml libreoffice
$ python3 -m venv pyvenv
$ source pyvenv/bin/activate
$ pip install -r requirements.txt
$ make
```

The output will be in the `build` directory, specifically, the `build/html`
directory contains the complete documentation including the PDF and single page
versions and is suitable for copying to a web server for hosting the document.


## Editing
The document is written in reStructuredText. The following characters are used
for headings:

* `#` with  overline for the page title
* `=` with overline for page sections
* `-` with overline for subsections
* Single `=` then `-` if additional levels are needed.

For details on reStructuredText as understood by Sphinx see
[Sphinx's reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).

When editing specific versions of the documentation can be built with `make html`
or `make pdf` allowing one to quickly look at modifications.  See `make help`
for a complete list of output types.


## License
The FoxXO game design document is licensed under the
[CC-BY-SA-4.0 license](https://github.com/j-richey/foxxo-gdd/blob/master/LICENSE.txt).
