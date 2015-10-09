# -*- coding: utf-8 -*-

import sys
import os

extensions = []

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'Cantal-Py'
copyright = u'2015, Paul Colomiets'

version = '0.1'
release = '0.1'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = ['_static']

htmlhelp_basename = 'Cantal-Pydoc'

latex_elements = {
}

latex_documents = [
  ('index', 'Cantal-Py.tex', u'Cantal-Py Documentation',
   u'Paul Colomiets', 'manual'),
]

man_pages = [
    ('index', 'cantal-py', u'Cantal-Py Documentation',
     [u'Paul Colomiets'], 1)
]

texinfo_documents = [
  ('index', 'Cantal-Py', u'Cantal-Py Documentation',
   u'Paul Colomiets', 'Cantal-Py', 'One line description of project.',
   'Miscellaneous'),
]

import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

