"""
Provides a wrapper for Sphinx that allows you to create an instance of
SphinxSetup that will automatically configue Sphinx with minimal manual configuration.

**Required Parameters:**
   :param: *package_name*
   :param: *project*
   :param: *author*

**Usage:**
   .. code-block:: python

    sphinx = SphinxSetup(
        package_name = 'my_package'
        project = 'My Package'
        author = 'My Name'
    )
    sphinx.build_documentation()
"""

import os
import shutil
import importlib
import subprocess

class SphinxSetup:
    def __init__(self, package_name: str ,project_path: str = ".",
                 build_directory_path = "docs/build/",
                 source_directory_path = "docs/source/",
                 project: str = 'Project Name', copyright: str  = 'Year, Author',
                 author: str = 'Author', release: str = '1.0', language: str = 'en',
                 extensions: list = [
                    'sphinx.ext.autodoc',
                    'sphinx.ext.napoleon',
                    'sphinx_autodoc_typehints',
                    'sphinx.ext.autosummary',
                ],
                 autosummary_generate: bool = "True",
                 templates_path: list = ['_templates'],
                 exclude_patterns: list = [
                     'venv',
                     'Thumbs.db',
                     '.DS_Store',
                     'tests'
                 ],
                 html_theme: str = 'sphinx_rtd_theme',
                 html_static_path: list = ['_static'],
                 autodoc_default_options = {
                     'members': True,
                     'undoc-members': True,
                     'show-inheritance': True
                 }
    ):
        self.package_name = package_name
        self.project_path: str = project_path
        self.build_directory_path: str = build_directory_path
        self.source_directory_path: str = source_directory_path
        self.docs_path = os.path.join(self.project_path, 'docs/')
        self.project: str = project
        self.copyright: str = copyright
        self.author: str = author
        self.release: str = release
        self.language: str = language
        self.extensions: list = extensions
        self.autosummary_generate: bool = bool(autosummary_generate)
        self.templates_path: list = templates_path
        self.exclude_patterns: list = exclude_patterns
        self.html_theme: str = html_theme
        self.html_static_path: list = html_static_path
        self.autodoc_default_options = autodoc_default_options
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

    def __str__(self) -> str:
        return (
            f"\nSphinx Setup Configuration Variables:\n\
            \tProject Name: {self.project}\n\
            \tProject Path: {self.project_path}\n\
            \tDocs Path: {self.docs_path}\n\
            \tBuild Directory Path: {self.build_directory_path}\n\
            \tSource Directory Path: {self.source_directory_path}\n\
            \tAuthor: {self.author}\n\
            \tCopyright: {self.copyright}\n\
            \tRelease: {self.release}\n\
            \tLanguage: {self.language}\n\
            \tExtensions: {self.extensions}\n\
            \tAutosummary Generate: {self.autosummary_generate}\n\
            \tTemplates Path: {self.templates_path}\n\
            \tExclude Patterns: {self.exclude_patterns}\n\
            \tHTML Theme: {self.html_theme}\n\
            \tHTML Static Path: {self.html_static_path}\n\n\
           ")

    def _validate_sphinx_installation(self) -> bool:
        """Validates that Sphinx is installed in the environment and exits the program if it isn't."""
        sphinx_installed: bool = importlib.util.find_spec("sphinx") is not None
        if not sphinx_installed:
            print("Sphinx is not installed. Please install Sphinx")
            exit(1)

    def _validate_sphinx_extensions(self) -> bool:
        """Validates that all listed sphinx extensions are installed and exits the program if they arent."""
        extensions_not_installed: list = []
        for extension in self.extensions:
            installed: bool = importlib.util.find_spec(extension) is not None
            if not installed: extensions_not_installed.append(extension)
        if len(extensions_not_installed) > 0:
            print(f"The following extensions are not installed: {extensions_not_installed}")
            exit(1)

    def _validate_quickstart_ran(self):
        """ Validates that quick start has been run. If it has not been run, quickstart will be called."""
        if os.path.exists(self.docs_path):
            pass
        else:
            self._run_quickstart()

    def _clean_previous_documentation(self):
        """
        Removes the docs/build/directory and docs/sources/generated directory
        to provide a clean environment to generate new documentation.
        """
        if os.path.exists(self.build_directory_path):
            try:
                shutil.rmtree(self.build_directory_path)
            except:
                print("Could not remove docs/build/ directory")
        else:
            print("docs/build/ directory does not exist")

        if os.path.exists(self.source_directory_path + "generated"):
            try:
                shutil.rmtree(self.source_directory_path + "generated")
            except:
                print("Could not remove docs/sources/generated/ directory")
        else:
            print("docs/sources/generated/ directory does not exist")
        return

    def _generate_conf_file(self):
        """Generates a conf.py file using the attributes the user entered."""
        config_items: list[str] = [
            'project',
            'copyright',
            'author',
            'release',
            'html_theme',
            'html_theme_path'
            'html_static_path',
            'extensions',
            'autosummary_generate',
            'templates_path',
            'exclude_patterns',
            'autodoc_default_options'
        ]

        if os.path.exists(self.source_directory_path + "conf.py"):
            os.remove(self.source_directory_path + "conf.py")
        config_string: str = 'import os\n'
        config_string += 'import sys\n\n'
        config_string += f'# We are inserting the path to be three deep to account for a variety of structures.\n'
        #config_string += f"sys.path.insert(0, os.path.abspath('.'))\n"
        config_string += f"sys.path.insert(0, os.path.abspath('..'))\n"
        config_string += f"sys.path.insert(0, os.path.abspath('../..'))\n"
        config_string += f"sys.path.insert(0, os.path.abspath('../../..'))\n\n"

        for key, value in self.__dict__.items():
            if key in config_items:
                if type(value) is str:
                    config_string += f'{key} = "{value}"\n'
                else:
                    config_string += f'{key} = {value}\n'

        try:
            with open(self.source_directory_path + "conf.py", "w") as conf_file:
                conf_file.write(config_string)
        except Exception as e:
            print(e)
            print("Could not write index.rst file")
        return

    def _generate_index_file(self):
        """Generates an index.rst file using the attributes the user entered."""
        if os.path.exists(self.source_directory_path + "index.rst"):
            os.remove(self.source_directory_path + "index.rst")

        file_contents: str = (
            f"Welcome to {self.project}'s Documentation!\n")
        file_contents += f"===============================================\n\n"
        file_contents += f".. autosummary::\n"
        file_contents += f"   :toctree: generated/\n"
        file_contents += f"   :recursive:\n\n"
        file_contents += f"   {self.package_name}\n\n"
        file_contents += f"Indices and tables\n"
        file_contents += f"==================\n\n"
        file_contents += f"* :ref:`genindex`\n"
        file_contents += f"* :ref:`modindex`\n"
        file_contents += f"* :ref:`search`"
        try:
            with open(self.source_directory_path + "index.rst", "w") as index_file:
                index_file.write(file_contents)
        except Exception as e:
            print(e)
            print("Could not write index.rst file")
        return

    def _run_quickstart(self):
        command = ['sphinx-quickstart']
        try:
            shutil.rmtree(self.docs_path)
        except FileNotFoundError as e:
            print(e)
            print("Checking for docs/... docs/ not present, continuing.")
        os.makedirs(self.docs_path, exist_ok=True)
        options=[
            f'-q',
            f'--sep',
            f'--project={self.project}',
            f'--author={self.author}',
            f'--release={self.release}',
            f'--language={self.language}'
        ]
        command.extend(options)

        try:
            subprocess.run(command, cwd=self.docs_path, check=True)
            print(f"Sphinx quickstart complete")
        except subprocess.CalledProcessError as e:
            print(f"Sphinx quickstart failed: {e}")
            exit(1)
        return

    def _run_sphinx(self):
        """Runs sphinx-apidoc and sphinx-build to generate documentation."""
        apidoc_command: list = ['sphinx-apidoc']
        apidoc_options:list = [
            '-o',
            f'{self.source_directory_path}generated/',
            f'{self.project_path}'
        ]
        apidoc_command.extend(apidoc_options)

        build_command: list = ['sphinx-build']
        build_options: list = [
            '-b',
            'html',
            f'{self.source_directory_path}',
            f'{self.build_directory_path}'
        ]
        build_command.extend(build_options)


        try:
            subprocess.run(apidoc_command, check=True)
            subprocess.run(build_command, check=True)
        except Exception as e:
            print(f'Sphinx build failed: {e}')
        return

    def build_documentation(self):
        """
        Validates sphinx, sphinx extensions, and file structures. Next, it clears
        the build/ and generated/ directories to prepare for new documentation.
        Finally, the sphinx-apidoc and sphinx-build commands to build the documentation.
        """
        self._validate_sphinx_installation()
        self._validate_sphinx_extensions()
        self._validate_quickstart_ran()
        self._clean_previous_documentation()
        self._generate_conf_file()
        self._generate_index_file()
        self._run_sphinx()
        return

