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
                 ) -> None:
        """
        Represents a configuration entity with project details and settings.

        :attributes:
           :is_testing: A boolean flag indicating if the instance is in testing mode.
           :project: The name of the project.
           :copyright: The copyright information including year and author.
           :author: The author of the project.
           :release: The release version of the project.
        """
        self.is_testing: bool = is_testing

        self.project = 'Project Name'
        self.copyright = 'Year, Author'
        self.author = 'Author'
        self.release = '1.0'

    def configure_sphinx(self):
        """
        A method to collect all the configuration settings for Sphinx.
        :explanation: This will keep them better organized and easier to adjust
        since we have put them all in a class.
        """
        self.register_project_path()
        print(f"Current Directory Debug: {os.getcwd()}")
        print(f"Sphinx Version: {sphinx.__version__}")

    def register_project_path(self) -> None:
        """
        Register the project path to the Python path.
        With a code structure that looks like:::
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
        package;

        """
        if self.is_testing:
            sys.path.insert(0, os.path.abspath('../../..'))
        else:
            sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

conf = Conf(is_testing=True)
conf.configure_sphinx()

project = 'Project Name'
copyright = 'Year, Author'
author = 'Author'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_rtd_theme',
]
autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
