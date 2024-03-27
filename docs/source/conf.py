# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python Template Package'
copyright = '2024, Max Planck Institute for Evolutionary Biology'
author = 'Max Planck'
version = "version = "version = "version = "version = "0.0.0"""""

import sys

sys.path.insert(0, '../../template')

import template

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx_rtd_theme',
              'myst_parser',
              'sphinx.ext.napoleon',
              ]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = ['.rst', '.md']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
