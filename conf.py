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
import os
import sys

# -- Path setup --------------------------------------------------------------

# Our extension
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "_ext"))
)
# Weblate code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def setup(app):
    # Used in Sphinx docs, needed for intersphinx links to it
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )


# -- Project information -----------------------------------------------------

project = "MonaLiSa"
copyright = "2022, MonaLiSa Project Group. This work is licensed under a CC BY 4.0 license."
author = "MonaLiSa Project Group"

# The full version, including alpha/beta/rc tags
release = "1.0.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxcontrib.httpdomain",
    "sphinx.ext.autodoc",
    "sphinx.ext.graphviz",
    "sphinx.ext.intersphinx",
    "sphinx-jsonschema",
    'sphinx_copybutton',
    "sphinxext.opengraph",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "venv"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Translations
language = "en"
gettext_compact = "docs"

html_logo = "images/ls-logo.png"
figure_language_filename = '{path}{language}/{basename}{ext}'

ogp_site_url = "https://docs.listening-skills.eu"
ogp_image = "https://docs.listening-skills.eu/en/latest/_static/ls-logo.png"