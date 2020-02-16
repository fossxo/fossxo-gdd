# Makefile for building the documentation.
# This is a modified version of the Sphinx generated file.

SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
PDFOUTPUT	  = $(wildcard $(BUILDDIR)/latex/*design*document*.pdf)
# The generated zip file is named after the PDF file.
ZIPNAME 	  = $(notdir $(basename $(PDFOUTPUT))).zip

# The targets supported by this make file.
.PHONY: all html singlehtml pdf handout slides linkcheck clean help


# All simply builds all the various outputs then ensures a copy of the PDF,
# single page HTML, and other supporting resources are copied to the HTML output
# directory so these can be downloaded.
# sed is used to fix the internal links and copy the single page HTML so
# they point to the correct location.
# Finally the resulting files are zipped so they can be eaisly uploaded.
all: html singlehtml pdf handout slides
	@sed -r 's/href="index.html/href="singlepage.html/g' "$(BUILDDIR)/singlehtml/index.html" > "$(BUILDDIR)/html/singlepage.html"
	@cp -v "$(PDFOUTPUT)" "$(BUILDDIR)/html/"
	@cp -v "$(BUILDDIR)/misc/handout.pdf" "$(BUILDDIR)/html/tic-tac-toe-overview-handout.pdf"
	@cp -v "$(BUILDDIR)/misc/slides.pdf" "$(BUILDDIR)/html/tic-tac-toe-overview-slides.pdf"
	@cd "$(BUILDDIR)/html"; zip -r $(ZIPNAME) *


html: _render_templates
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)"


# The single HTML page is copied into the HTML directory and renamed so it can
# use the same resources. Not how the internal links are fixed up.
singlehtml: _render_templates
	@$(SPHINXBUILD) -M singlehtml "$(SOURCEDIR)" "$(BUILDDIR)"


# Note: the -E is used to ensure the LaTeX gets a clean build. Sometimes the
# HTML builds leave a dirty environment behind that cause the LaTeX builder to fail.
# TODO: reduce the amount of output from this command.
pdf: _convert_svg _render_templates
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" -E


# For the handout and slides we need to change to the source directory as the TEX
# files import resources from paths relative to this directory.
handout:
	@mkdir --parents "${BUILDDIR}/misc"
	@cd "$(SOURCEDIR)"; lualatex -interaction=nonstopmode -output-directory "../${BUILDDIR}/misc" handout.tex

slides: _convert_svg
	@mkdir --parents "${BUILDDIR}/misc"
	@cd "$(SOURCEDIR)"; lualatex -interaction=nonstopmode -output-directory "../${BUILDDIR}/misc" slides.tex


linkcheck: _render_templates
	@$(SPHINXBUILD) -M linkcheck "$(SOURCEDIR)" "$(BUILDDIR)"


clean:
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)"


help:
	@echo "Makefile for building the documentation."
	@echo ""
	@echo "Available commands:"
	@echo "  all         Builds all the different output types. (default)"
	@echo "  html        Builds standalone HTML files for the documentation."
	@echo "  singlehtml  Builds a single HTML file of the documentation."
	@echo "  pdf         Builds a PDF of the documentation."
	@echo "  handout     Builds a single page overview PDF."
	@echo "  slides      Builds a PDF slide deck."
	@echo "  linkcheck   Checks for broken external links."
	@echo "  clean       Cleans the output directory."
	@echo "  help        Shows this help message."
	@echo ""
	@echo "For details on how to build the documentation see the README."


# Helper targets for doing file conversions and other work.
.PHONY: _convert_svg _render_templates

_convert_svg:
	@python3 build-tools.py convert-svg "$(SOURCEDIR)"

_render_templates:
	@python3 build-tools.py render-templates "$(SOURCEDIR)"
