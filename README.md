Pound of Rust Project Documentation
===================================

:warning: This documentation is a work in progress.

This repository contains documentation for the Pound of Rust project ---
the creation of a Tic Tac Toe game in Rust. This project is the successor of
the [Ounce of Rust Project](https://github.com/j-richey/ounce-of-rust-manual).

The latest version of the documentation is hosted here:
[Pound of Rust Project Documentation](https://j-richey.github.io/project-documentation/pound-of-rust/)


## Building
This documentation is rendered using [Sphinx](https://www.sphinx-doc.org/en/master/).
The following applications are required to build this documentation:

* Python 3.5 or newer
* inkscape
* plantuml
* A LaTeX toolchain
* Sphinx

On Ununtu / Debian system the required packages can be installed and
documentation built with:

```
$ sudo apt install texlive-full inkscape plantuml
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
The project documentation is licensed under the
[CC-BY-SA-4.0 license](https://github.com/j-richey/pound-of-rust-docs/blob/master/LICENSE.txt).
