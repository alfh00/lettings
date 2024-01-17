# conf.py

import os
import sys

import django

sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'

# Setup Django
django.setup()

# Configuration file for the Sphinx documentation builder.

project = 'OC LETTINGS'
copyright = '2024, AF'
author = 'AF'
release = 'beta'

# -- General configuration ---------------------------------------------------

extensions = ['sphinx.ext.autodoc']
autodoc_mock_imports = ['django']
master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
