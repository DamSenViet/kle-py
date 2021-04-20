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

sys.path.insert(0, os.path.abspath("./../damsenviet"))

# -- Project information -----------------------------------------------------

project = "kle-py"
copyright = "2020, damsenviet"
author = "damsenviet"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosummary",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

autodoc_typehints = "none"
always_document_param_types = False
simplify_optional_unions = False
autodoc_member_order = "bysource"
autosummary_generate = True
autosummary_imported_members = False  # default

# Add any paths that contain templates here, relative to this directory.
templates_path = ["templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_title = "kle-py"
# html_logo = "_static/logo-text.svg"
# html_favicon = "_static/logo.svg"
html_theme = "pydata_sphinx_theme"
html_context = {
    "github_user": "DamSenViet",
    "github_repo": "kle-py",
    "github_version": "master",
    "doc_path": "docs",
}
html_theme_options = {
    "github_url": "https://github.com/DamSenViet/kle-py",
    "show_prev_next": False,
    # "use_edit_page_button": True,
}
language = "en"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_baseurl = "/kle-py/"

add_module_names = False


def setup(app):
    app.add_css_file("style.css")  # may also be an URL