# Copyright © LFV

import logging
from importlib.resources import Package, files
from pathlib import PosixPath

from jinja2 import (
    BaseLoader,
    Environment,
    FileSystemLoader,
    PackageLoader,
    Template,
    TemplateNotFound,
    select_autoescape,
)

import reqstool.commands.report.templates


class Jinja2Utils:

    @staticmethod
    def create_template(template_name: str) -> Template:
        """Returns a Template based on the template name

        Args:
            template_name (str): The name of the template to retrieve

        Returns:
            Template: Jinja2 template used for rendering of the AsciiDoc document
        """

        def load_template(loader: BaseLoader) -> Template:
            template_env = Environment(
                loader=loader, autoescape=select_autoescape(), trim_blocks=True, lstrip_blocks=True
            )
            return template_env.get_template(template_name)

        try:
            template_module: Package = reqstool.commands.report
            template_path: PosixPath = files(template_module).joinpath("templates")
            fs_loader = FileSystemLoader(searchpath=template_path)
            return load_template(fs_loader)
        except TemplateNotFound:
            logging.info("Can't find local files. Uses package loader instead.")

            package_loader = PackageLoader("reqstool")
            return load_template(package_loader)

    @staticmethod
    def render(data: dict, template: Template) -> str:
        """Returns a string with rendered template as an AsciiDoc Document

        Args:
            template (Template): Template to base the rendering upon
            data: Data to render

        Returns:
            str: The rendered template
        """

        return template.render(data=data)
