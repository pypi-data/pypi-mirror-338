"""Jinja2 environment config for Gandula."""

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('gandula', 'html_templates'), autoescape=select_autoescape()
)
