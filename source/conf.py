# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
import sys
import os

# -- Project information -----------------------------------------------------

project = 'Tech Assignment'
copyright = "2020, ㈜비바리퍼블리카"
author = "Kim, EunJung"

# The full version, including alpha/beta/rc tags
release = '20.12.00.00'

# The master toctree document
master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

needs_sphinx = "1.3"

# Sphinx extension module names and templates location
sys.path.append(os.path.abspath("_extensions"))

extensions = [
    "sphinx_rtd_theme",
 #   'sphinx.ext.autosectionlabel',
 #   'sphinx.ext.autodoc',
 #   'sphinx.ext.intersphinx',
 #   'sphinxcontrib.httpdomain',
    'sphinx_tabs.tabs',
#    'sphinx-prompt',
#    'notfound.extension',
#    'hoverxref.extension',
    'sphinx_search.extension'
#    'recommonmark'
]

# Warning when the Sphinx Tabs extension is used with unknown
# builders (like the dummy builder) - as it doesn't cause errors,
# we can ignore this so we still can treat other warnings as errors.
sphinx_tabs_nowarn = True

if not os.getenv("SPHINX_NO_SEARCH"):
    extensions.append("sphinx_search.extension")

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]

# You can specify multiple suffix as a list of string: ['.rst', '.md']
source_suffix = ".rst"
source_encoding = "utf-8-sig"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
if on_rtd:
    using_rtd_theme = True

# Theme options
html_theme_options = {
    # if we have a html_logo below, this shows /only/ the logo with no title text
    "logo_only": True,
    # Collapse navigation (False makes it tree-like)
    "collapse_navigation": False,
}

# VCS options: https://docs.readthedocs.io/en/latest/vcs.html#github
html_context = {
#  "display_github": not is_i18n,  # Integrate GitHub
    "github_user": "ejkim-author",  # Username
    "github_repo": "tw_assignment",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/",  # Path in the checkout to the docs root
   # "godot_inject_language_links": True,
   # "godot_docs_supported_languages": list(supported_languages.keys()),
   # "godot_docs_basepath": "https://docs.godotengine.org/",
   # "godot_docs_suffix": ".html",
   # "godot_default_lang": "en",
   # "godot_canonical_version": "stable",
    # Distinguish local development website from production website.
    # This prevents people from looking for changes on the production website after making local changes :)
    # "godot_title_prefix": "" if on_rtd else "(DEV) ",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Version info for the project, acts as replacement for |version| and |release|
# The short X.Y version
version = os.getenv("READTHEDOCS_VERSION", "latest")
# The full version, including alpha/beta/rc tags
release = version

# Parse Sphinx tags passed from RTD via environment
env_tags = os.getenv("SPHINX_TAGS")