"""Simple script for converting SVG files to PDF files."""

import argparse
import glob
import os
import subprocess
import sys
import textwrap


def main():
    """The main function of the application"""
    try:
        args = _parse_args()

        svg_files = find_svgs(args.source_dir)

        for svg in svg_files:
            convert_svg_to_pdf(svg)

        return 0
    except Exception as ex:
        print("Error: {0}".format(ex), file=sys.stderr)
        return 1


def find_svgs(directory):
    """Find all SVG files in the provided directory and all subdirectories.

    :param directory: The directory to search for SVGs.
    :returns: An enumerable of SVG file names.
    """
    return glob.glob(os.path.join(directory, "**", "*.svg"), recursive=True)


def convert_svg_to_pdf(svg_name):
    """Converts the SVG provided SVG to a PDF file.

    The PDF file keeps the same basename as the SVG. The original SVG is kept
    and any existing PDFs with the same name are overwritten.

    :param svg_name: The name of the SVG file to convert.
    """
    print("Converting: {}".format(svg_name))

    pdf_name = os.path.splitext(svg_name)[0] + ".pdf"
    args = ['inkscape', '-z',
            '-f', svg_name,
            '--export-pdf={}'.format(pdf_name)]
    subprocess.run(args, check=True)


def _parse_args():
    description = textwrap.dedent("""\
    Converts SVG files to PDF files using inkscape.
    
    The PDF file keeps the same basename as the SVG. The original SVGs are kept
    and any existing PDFs with the same name are overwritten.
    """)

    epilog = textwrap.dedent("""\
    see also:
     * inkscape
    """)

    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('source_dir', metavar="SOURCE_DIR",
                        help="Source directory to search for SVG files to convert.")

    return parser.parse_args()


if __name__ == '__main__':
    sys.exit(main())
