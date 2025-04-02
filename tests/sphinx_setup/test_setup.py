from src.chelexicon.tools.sphinx_setup.setup import SphinxSetup
import os
from shutil import rmtree

def test_sphinx_setup_default_initialization():
    sphinx_setup = SphinxSetup(package_name='tests')
    assert sphinx_setup.package_name == 'tests'
    assert sphinx_setup.project_path == "."
    assert sphinx_setup.build_directory_path == "docs/build/"
    assert sphinx_setup.source_directory_path == "docs/source/"
    assert sphinx_setup.docs_path == "./docs/"
    assert sphinx_setup.project == 'Project Name'
    assert sphinx_setup.copyright == 'Year, Author'
    assert sphinx_setup.author == 'Author'
    assert sphinx_setup.release == '1.0'
    assert sphinx_setup.language == 'en'
    assert sphinx_setup.extensions == [
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
        'sphinx_autodoc_typehints',
        'sphinx.ext.autosummary',
    ]
    assert sphinx_setup.autosummary_generate == True
    assert sphinx_setup.templates_path == ['_templates']
    assert sphinx_setup.exclude_patterns == [
                     'venv',
                     'Thumbs.db',
                     '.DS_Store',
                     'tests'
                 ]
    assert sphinx_setup.html_theme == 'sphinx_rtd_theme'
    assert sphinx_setup.html_static_path == ['_static']
    assert sphinx_setup.autodoc_default_options == {
                     'members': True,
                     'undoc-members': True,
                     'show-inheritance': True
                 }
    assert sphinx_setup.builtin_themes == [
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


def test_sphinx_setup_custom_initialization():
    sphinx_setup = SphinxSetup(
        package_name='tests',
        project_path="/custom/path",
        build_directory_path="/custom/build",
        source_directory_path="/custom/source",
        project="Custom Project",
        copyright="2025, Custom Author",
        author="Custom Author",
        release="2.0",
        language="fr",
        extensions=['sphinx.ext.todo', 'sphinx.ext.viewcode'],
        autosummary_generate=False,
        templates_path=["custom_templates"],
        exclude_patterns=["custom_pattern"],
        html_theme="custom_theme",
        html_static_path=["custom_static"]
    )
    assert sphinx_setup.package_name == 'tests'
    assert sphinx_setup.project_path == "/custom/path"
    assert sphinx_setup.build_directory_path == "/custom/build"
    assert sphinx_setup.source_directory_path == "/custom/source"
    assert sphinx_setup.docs_path == "/custom/path/docs/"
    assert sphinx_setup.project == "Custom Project"
    assert sphinx_setup.copyright == "2025, Custom Author"
    assert sphinx_setup.author == "Custom Author"
    assert sphinx_setup.release == "2.0"
    assert sphinx_setup.language == "fr"
    assert sphinx_setup.extensions == ['sphinx.ext.todo', 'sphinx.ext.viewcode']
    assert sphinx_setup.autosummary_generate == False
    assert sphinx_setup.templates_path == ["custom_templates"]
    assert sphinx_setup.exclude_patterns == ["custom_pattern"]
    assert sphinx_setup.html_theme == "custom_theme"
    assert sphinx_setup.html_static_path == ["custom_static"]
    assert sphinx_setup.autodoc_default_options == {
        'members': True,
        'undoc-members': True,
        'show-inheritance': True
    }
    assert sphinx_setup.builtin_themes == [
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

def test__validate_sphinx_installation():
    sphinx_setup = SphinxSetup(package_name="tests")
    assert sphinx_setup._validate_sphinx_installation() is None

def test__validate_sphinx_extensions():
    sphinx_setup = SphinxSetup(package_name='tests')
    assert sphinx_setup._validate_sphinx_extensions() is None

def test__clean_previous_documentation():
    sphinx_setup = SphinxSetup(package_name="tests")
    sphinx_setup._clean_previous_documentation()
    assert os.path.exists(sphinx_setup.build_directory_path) == False
    assert os.path.exists(sphinx_setup.source_directory_path + "generated") == False

def test__run_quickstart():
    sphinx_setup = SphinxSetup(package_name="tests")
    sphinx_setup._run_quickstart()
    assert os.path.exists(sphinx_setup.docs_path) == True
    remove_test_files(sphinx_setup.docs_path)
    assert os.path.exists(sphinx_setup.docs_path) == False

def test__validate_quickstart_ran():
    sphinx_setup = SphinxSetup(package_name="tests")
    sphinx_setup._validate_quickstart_ran()
    print(sphinx_setup.docs_path)
    assert os.path.exists(sphinx_setup.docs_path) == True
    remove_test_files(sphinx_setup.docs_path)
    assert os.path.exists(sphinx_setup.docs_path) == False

def test__generate_conf_file():
    sphinx_setup = SphinxSetup(package_name="tests")
    os.makedirs(sphinx_setup.source_directory_path, exist_ok=True)
    sphinx_setup._generate_conf_file()
    assert os.path.exists(sphinx_setup.source_directory_path + "conf.py") == True
    remove_test_files(sphinx_setup.docs_path)
    assert os.path.exists(sphinx_setup.docs_path) == False

def test__generate_index_file():
    sphinx_setup = SphinxSetup(package_name="tests")
    os.makedirs(sphinx_setup.source_directory_path, exist_ok=True)
    sphinx_setup._generate_index_file()
    assert os.path.exists(sphinx_setup.source_directory_path + "index.rst") == True
    remove_test_files(sphinx_setup.docs_path)
    assert os.path.exists(sphinx_setup.docs_path) == False

def test_build_documentation():
    sphinx_setup = SphinxSetup(package_name="sphinx_setup")
    remove_test_files(sphinx_setup.docs_path)
    assert os.path.exists(sphinx_setup.docs_path) == False
    sphinx_setup.build_documentation()
    assert os.path.exists(sphinx_setup.docs_path) == True
    assert os.path.exists(sphinx_setup.source_directory_path + "conf.py") == True
    assert os.path.exists(sphinx_setup.source_directory_path + "index.rst") == True
    assert os.path.exists(sphinx_setup.build_directory_path) == True
    assert os.path.exists(sphinx_setup.build_directory_path + 'index.html') == True
    assert os.path.exists(sphinx_setup.build_directory_path + 'generated/modules.html') == True
    remove_test_files(sphinx_setup.docs_path)
    assert os.path.exists(sphinx_setup.docs_path) == False

def remove_test_files(path):
    try:
        rmtree(path)
    except:
        pass
    assert os.path.exists(path) == False