"""Simple script that helps with the documentation build process.

This includes converting SVG files to PDF files and rendering parts of the
documentation.

See the commandline help for details.
"""

import abc
import argparse
import datetime
import glob
import os
import subprocess
import sys
import textwrap
import inspect

import jinja2
import yaml


def main():
    """The main function of the application"""
    try:
        # Parse the command line arguments extracting the tool to use.
        args = _parse_args()

        # Create and run the tool passing in the provided options.
        all_build_tools = _get_build_tool_command_map()
        build_tool_type = all_build_tools[args.build_tool]
        build_tool = build_tool_type(args.source_dir)
        build_tool.run()
        return 0

    except Exception as ex:
        print("Error: {0}".format(ex), file=sys.stderr)
        return 1


class BuildTool(metaclass=abc.ABCMeta):
    """Base class for build tools."""

    def __init__(self, source_dir):
        """Initializes the build tool with the provided options.

        :param source_dir: The directory to run the build tool over.
        """
        self._source_dir = source_dir

    @abc.abstractmethod
    def run(self):
        """Runs the build tool."""
        pass

    @classmethod
    @abc.abstractmethod
    def get_command_name(cls):
        """Provides the user visible name of the build tool.

        :return: The name of the build tool to use on the command line options.
        """
        pass


class SVGToPDFBuildTool(BuildTool):
    """Converts SVG files to PDF files so they can be used by LaTeX.

    The PDF file keeps the same basename as the SVG. The original SVGs are kept
    and any existing PDFs with the same name are overwritten.
    """

    @classmethod
    def get_command_name(cls):
        return "convert-svg"

    def run(self):
        svg_files = self._find_svgs(self._source_dir)

        for svg in svg_files:
            self._convert_svg_to_pdf(svg)

    @staticmethod
    def _find_svgs(directory):
        """Find all SVG files in the provided directory and all subdirectories.

        :param directory: The directory to search for SVGs.
        :return: An enumerable of SVG file names.
        """
        return glob.glob(os.path.join(directory, "**", "*.svg"), recursive=True)

    @staticmethod
    def _convert_svg_to_pdf(svg_name):
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


class TemplateDataInfo:
    """Class that holds information about a template to render."""

    def __init__(self, template, output, data_source):
        """Creates a new template data class.

        :param template: Path to the template file.
        :param output: Name of the output file to render.
        :param data_source: Path to the file containing the template's data.
        """
        self.template = template
        self.output = output
        self.data_source = data_source


class RenderTemplatesBuildTool(BuildTool):
    """Renders templates to output files using the Jinja templating engine."""

    # List of all template to render.
    TEMPLATE_DATA_MAP = [
        TemplateDataInfo(template="environments.rst_t",
                         output="environments.rst",
                         data_source="environments.yaml")
    ]

    @classmethod
    def get_command_name(cls):
        return "render-templates"

    def run(self):
        tool_info = self._get_tool_info()

        # For each item load its data and template. Then render the template and
        # write the output.
        for item in self.TEMPLATE_DATA_MAP:
            print(f"Rendering template '{item.template}' to '{item.output}' "
                  f"using data from '{item.data_source}'.")
            data = self._load_data(item.data_source)
            template = self._load_template(item.template)
            # TODO: Determine a better way to set the template parameter names.
            # We only have one template at the moment so this is not a bug issue
            # but would cause more problems if we added templates in the future.
            rendered_template = template.render(
                environments=data,
                tool_info=tool_info)
            self._write_output(item.output, rendered_template)

    def _load_data(self, data_source):
        """Loads data from the provided data source.

        :param data_source: Path to the data to load.
        :return: Dictionary containing the loaded data.
        """
        with open(os.path.join(self._source_dir, data_source)) as f:
            return yaml.safe_load(f)

    def _load_template(self, template):
        """Loads the indicated template.

        :param template: Path to the template to load.
        :return: The loaded Jinja template.
        """
        template_path = os.path.join(self._source_dir, template)
        with open(template_path) as template_file:
            return jinja2.Template(template_file.read())

    def _write_output(self, filename, output):
        """Writes the provided output to the indicated file.

        Any existing files are overwritten.

        :param filename: Name of the file to write the data to.
        :param output: The output text to write.
        """
        output_path = os.path.join(self._source_dir, filename)
        with open(output_path, mode='w') as output_file:
            output_file.write(output)

    def _get_tool_info(self):
        """Returns information about this tool.

        Templates can include this information to warn editors from modifying
        the rendered output files.
        """
        return {"tool_name": sys.argv[0],
                "render_time": datetime.datetime.now()}


def _get_build_tool_command_map():
    """Searches this module for all available build tools.

    :return: Dictionary whose keys are the tool's command name and whose values
        are the type of command.
    :raises RuntimeError: A error is raised if two build tools try to register
        the same command name.
    """
    # Search the current module for classes that are build tools. Their command
    # name is extracted so the name and type can be added to the returned map.
    command_map = {}
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and issubclass(obj, BuildTool) \
                and not obj == BuildTool:
            command_name = obj.get_command_name()
            if command_name in command_map:
                existing_build_tool = command_map[command_name]
                raise RuntimeError(f"Two build tools have registered the same "
                                   f"command name of '{command_name}': "
                                   f"{obj} and {existing_build_tool}.")

            command_map[obj.get_command_name()] = obj

    return command_map


def _parse_args():
    description = textwrap.dedent("""\
    Script that helps with the documentation build process.
    
    This includes converting converting SVG files to PDF files using inkscape
    and rendering template files.
    """)

    epilog = textwrap.dedent("""\
    build tool actions:
      convert-svg:
        Converts all SVG files to PDF files. This allows LaTeX outputs to use 
        these graphics. The PDF file keeps the same basename as the SVG. The 
        original SVGs are kept and any existing PDFs with the same name are 
        overwritten.
      
      render-templates:
        Renders the templates into their output forms. This allows a single
        input file to generate multiple output files. See the 
        `RenderTemplatesBuildTool` in this script's source for more details.
    
    see also:
     * inkscape
    """)

    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('build_tool', metavar="ACTION",
                        choices=_get_build_tool_command_map().keys(),
                        help="The action to take. See below for more details.")
    parser.add_argument('source_dir', metavar="SOURCE_DIR",
                        help="Directory containing the source files for the"
                             "build tool to use.")

    return parser.parse_args()


if __name__ == '__main__':
    sys.exit(main())
