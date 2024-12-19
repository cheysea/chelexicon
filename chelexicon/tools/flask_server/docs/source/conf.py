"""
The configuration file for the Sphinx documentation builder.
"""

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
import sphinx

class Conf():
    """
    A configuration class for the Sphinx documentation builder.

    :Why do we do this?:
       We are using a class for this configuration file instead of the normal
       way of using a configuration file. We do this so we are able to use
       self.is_testing() as a way to control the behavior of the configuration
       during periods of testing.
    """
    def __init__(self,
                 is_testing: bool =False,
                 project: str = 'Flask Server',
                 copyright: str = '2024, Cheysea Dax',
                 author: str = 'Cheysea Dax',
                 release: str = '1.0',
                 extensions: list =  None,
                 autosummary_generate: bool = True,
                 templates_path: list = None,
                 exclude_patterns: list = None,
                 available_html_themes: list = None,
                 html_theme: str = None,
                 html_static_path: list = None,
                 ) -> None:
        """Represents a configuration entity with project details and settings."""

        # Set the variable for testing.
        self.is_testing: bool = is_testing

        # Configure project settings.
        self.project = project
        self.copyright = copyright
        self.author = author
        self.release = release

        # Configure extensions and autosummary.
        if extensions is None:
            self.extensions =  [
                'sphinx.ext.autodoc',
                'sphinx.ext.autosummary',
                'sphinx_rtd_theme',
                'sphinx_wagtail_theme'
            ]
        self.autosummary_generate = autosummary_generate

        if templates_path is None:
            self.templates_path = ['_templates']
        if exclude_patterns is None:
            self.exclude_patterns = []

        # Configure the html_theme for Sphinx based on user preference
        # from most preferred to least preferred.
        if available_html_themes is None:
            self.available_html_themes = [
                #'sphinx_documatt_theme',
                'sphinx_wagtail_theme',
                'sphinx_rtd_theme',
                'alabaster',]
        self.builtin_themes = [
            'alabaster',
            'classic'
            'sphinxdoc',
            'scrolls',
            'agogo',
            'traditional',
            'nature',
            'haiku',
            'pyramid',
            'bizstyle',

        ]
        if html_theme is None:
            self.html_theme = self.generate_html_theme()
        else:
            self.html_theme = html_theme

        # Set the path for the static folder
        if html_static_path is None:
            self.html_static_path = ['_static']
        else:
            self.html_static_path = html_static_path

    def configure_sphinx(self) -> dict:
        """
        A method to collect all the configuration settings for Sphinx.

        :returns: A dictionary of configuration settings. With the key:value
        being the setting name and the value of the setting.
        """
        self.register_project_path()

        config_item: dict = { key: value for key,value in self.__dict__.items() if not key.startswith('__') }
        return config_item

    def register_project_path(self) -> None:
        """
        Register the project path to the Python path.

        With a code structure that looks like:
        ::
           project_root/
              |- project_directory
                 |- __init__.py
                 |- project_sub_directory
                    |- __init__.py
                    |- project_sub_directory_module
                 |- project_module
              |- docs
                 |- build
                 |- source
                    |- conf.py
                    |- index.rst
        Going back two directories (../../) will get us to the project root. From
        here we can import the project modules.

        For testing and for this template package itself we go back three
        directories (../../../) so we can call on the project_root as the top level
        package
        """
        if self.is_testing:
            sys.path.insert(0, os.path.abspath('../../..'))
        else:
            sys.path.insert(0, os.path.abspath('../..'))

    def generate_html_theme(self):
        """ Reads the available html_themes and returns the first one that is available."""
        for html_theme in self.available_html_themes:
            if html_theme in sys.modules or self.is_testing:
                available_theme =  html_theme
                break
            #elif html_theme == self.available_html_themes[-1]:
                #available_theme = 'alabaster'
        return available_theme


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

conf = Conf(is_testing=True,
            html_theme='sphinx_wagtail_theme')
config_item = conf.configure_sphinx()

project = config_item['project']
copyright = config_item['copyright']
author = config_item['author']
release = config_item['release']

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = config_item['extensions']
autosummary_generate = config_item['autosummary_generate']

templates_path = config_item['templates_path']
exclude_patterns = config_item['exclude_patterns']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = config_item['html_theme']
html_static_path = config_item['html_static_path']


