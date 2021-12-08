# -*- coding: utf-8 -*-
import os
import sys
from datetime import date

import recommonmark
from recommonmark.transform import AutoStructify

from sphinx_scylladb_theme.utils import multiversion_regex_builder

sys.path.insert(0, os.path.abspath(".."))

# -- General configuration ------------------------------------------------

# Target Sphinx version
needs_sphinx = "1.8"

# Add any Sphinx extension module names here, as strings.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx.ext.extlinks",
    "sphinx_scylladb_theme",
    "sphinx_multiversion",  # optional
    "recommonmark",  # optional
]

# The suffix(es) of source filenames.
source_suffix = [".rst", ".md"]
autosectionlabel_prefix_document = True

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Scylla Sphinx Theme"
copyright = str(date.today().year) + ", ScyllaDB. All rights reserved."
author = u"Scylla Project Contributors"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Setup Sphinx
def setup(sphinx):
    sphinx.add_config_value(
        "recommonmark_config",
        {
            "enable_eval_rst": True,
            "enable_auto_toc_tree": False,
        },
        True,
    )
    sphinx.add_transform(AutoStructify)


# List of substitutions
rst_prolog = """
.. |rst| replace:: RestructuredText
"""
# -- Options for not found extension -------------------------------------------

# Template used to render the 404.html generated by this extension.
notfound_template = "404.html"

# Prefix added to all the URLs generated in the 404 page.
notfound_urls_prefix = ""

# -- Options for redirect extension ---------------------------------------

# Read a YAML dictionary of redirections and generate an HTML file for each
redirects_file = "_utils/redirections.yaml"

# -- Options for multiversion extension ----------------------------------

# Whitelist pattern for tags (set to None to ignore all tags)
TAGS = []
smv_tag_whitelist = multiversion_regex_builder(TAGS)
# Whitelist pattern for branches (set to None to ignore all branches)
BRANCHES = ["branch-1.0", "master"]
smv_branch_whitelist = multiversion_regex_builder(BRANCHES)
# Defines which version is considered to be the latest stable version.
# Must be listed in smv_tag_whitelist or smv_branch_whitelist.
smv_latest_version = "branch-1.0"
smv_rename_latest_version = "stable"
# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r"^origin$"
# Pattern for released versions
smv_released_pattern = r"^tags/.*$"
# Format for versioned output directories inside the build directory
smv_outputdir_format = "{ref.name}"

# -- Options for HTML output ----------------------------------------------

# The theme to use for pages.
html_theme = "sphinx_scylladb_theme"
html_theme_path = ["../.."]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for the theme, see the
# documentation.
html_theme_options = {
    "conf_py_path": "docs/source/",
    "banner_button_text": "Learn more",
    "banner_button_url": "https://sphinx-theme.scylladb.com/stable/upgrade/CHANGELOG",
    "banner_icon_path": "",
    "banner_title_text": "Sphinx ScyllaDB Theme 1.0 is now released 🥳",
    "hide_edit_this_page_button": "false",
    "hide_sidebar_index": "true",
    "hide_banner": "false",
    "hide_version_dropdown": ["master"],
    "github_issues_repository": "scylladb/sphinx-scylladb-theme",
    "github_repository": "scylladb/sphinx-scylladb-theme",
    "site_description": "Sphinx Theme for ScyllaDB projects.",
}

# Last updated format
html_last_updated_fmt = "%d %b %Y"

# Custom sidebar templates, maps document names to template names.
html_sidebars = {"**": ["side-nav.html"]}

# Output file base name for HTML help builder.
htmlhelp_basename = "ScyllaDocumentationdoc"

# URL which points to the root of the HTML documentation.
html_baseurl = "https://sphinx-theme.scylladb.com"

# Dictionary of values to pass into the template engine’s context for all pages
html_context = {"html_baseurl": html_baseurl}
