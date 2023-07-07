# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use abspath to make it absolute, like shown here.

from sys import path as sys_path
from os.path import abspath
from pathlib import Path
from json import loads

from pyTooling.Packaging import extractVersionInformation

ROOT = Path(__file__).resolve().parent

sys_path.insert(0, abspath('.'))
sys_path.insert(0, abspath('..'))
sys_path.insert(0, abspath('../pyEDAA/IPXACT'))
#sys_path.insert(0, abspath('_extensions'))


# ==============================================================================
# Project information and versioning
# ==============================================================================
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
project =     "pyEDAA.IPXACT"

packageInformationFile = Path(f"../{project.replace('.', '/')}/__init__.py")
versionInformation = extractVersionInformation(packageInformationFile)

author =    versionInformation.Author
copyright = versionInformation.Copyright
version =   ".".join(versionInformation.Version.split(".")[:2])  # e.g. 2.3    The short X.Y version.
release =   versionInformation.Version

# ==============================================================================
# Miscellaneous settings
# ==============================================================================
# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
	"_build",
	"_themes",
	"Thumbs.db",
	".DS_Store"
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'stata-dark'


# ==============================================================================
# Restructured Text settings
# ==============================================================================
prologPath = Path("prolog.inc")
try:
	with prologPath.open("r") as fileHandle:
		rst_prolog = fileHandle.read()
except Exception as ex:
	print(f"[ERROR:] While reading '{prologPath}'.")
	print(ex)
	rst_prolog = ""


# ==============================================================================
# Options for HTML output
# ==============================================================================

html_context = {}
ctx = ROOT / 'context.json'
if ctx.is_file():
	html_context.update(loads(ctx.open('r').read()))

if (ROOT / "_theme").is_dir():
	html_theme_path = ["."]
	html_theme = "_theme"
	html_theme_options = {
		'logo_only': True,
		'home_breadcrumbs': False,
		'vcs_pageview_mode': 'blob',
	}
else:
	html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = str(Path(html_static_path[0]) / "logo.svg")
html_favicon = str(Path(html_static_path[0]) / "favicon.svg")

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyEDAAIPXACTDoc'

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
html_last_updated_fmt = "%d.%m.%Y"


# ==============================================================================
# Options for LaTeX / PDF output
# ==============================================================================
from textwrap import dedent

latex_elements = {
	# The paper size ('letterpaper' or 'a4paper').
	'papersize': 'a4paper',

	# The font size ('10pt', '11pt' or '12pt').
	#'pointsize': '10pt',

	# Additional stuff for the LaTeX preamble.
	'preamble': dedent(r"""
		% ================================================================================
		% User defined additional preamble code
		% ================================================================================
		% Add more Unicode characters for pdfLaTeX.
		% - Alternatively, compile with XeLaTeX or LuaLaTeX.
		% - https://GitHub.com/sphinx-doc/sphinx/issues/3511
		%
		\ifdefined\DeclareUnicodeCharacter
			\DeclareUnicodeCharacter{2265}{$\geq$}
			\DeclareUnicodeCharacter{21D2}{$\Rightarrow$}
		\fi


		% ================================================================================
		"""),

	# Latex figure (float) alignment
	#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
	( master_doc,
		'pyEDAA.IPXACT.tex',
		'The pyEDAA.IPXACT Documentation',
		'Patrick Lehmann',
		'manual'
	),
]


# ==============================================================================
# Extensions
# ==============================================================================
extensions = [
# Standard Sphinx extensions
	"sphinx.ext.autodoc",
	'sphinx.ext.extlinks',
	'sphinx.ext.intersphinx',
	'sphinx.ext.inheritance_diagram',
	'sphinx.ext.todo',
	'sphinx.ext.graphviz',
	'sphinx.ext.mathjax',
	'sphinx.ext.ifconfig',
	'sphinx.ext.viewcode',
# SphinxContrib extensions
	'sphinxcontrib.mermaid',
# Other extensions
	'sphinx_fontawesome',
	'sphinx_autodoc_typehints',
	'autoapi.sphinx',
]

# ==============================================================================
# Sphinx.Ext.InterSphinx
# ==============================================================================
intersphinx_mapping = {
	'python':   ('https://docs.python.org/3', None),
#	'pyFlags':      ('http://pyFlags.readthedocs.io/en/latest', None),
}


# ==============================================================================
# Sphinx.Ext.AutoDoc
# ==============================================================================
# see: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
autodoc_default_options = {
	"private-members": True,
	"special-members": True,
	"inherited-members": True,
	"exclude-members": "__weakref__"
}
#autodoc_class_signature = "separated"
autodoc_member_order = "bysource"       # alphabetical, groupwise, bysource
autodoc_typehints = "both"
#autoclass_content = "both"



# ==============================================================================
# Sphinx.Ext.ExtLinks
# ==============================================================================
extlinks = {
	'ghrepo':      ('https://github.com/%s', 'gh:'),
	'ghissue':     ('https://github.com/edaa-org/pyEDAA.IPXACT/issues/%s', 'issue #'),
	'ghpull':      ('https://github.com/edaa-org/pyEDAA.IPXACT/pull/%s', 'pull request #'),
	'ghsrc':       ('https://github.com/edaa-org/pyEDAA.IPXACT/blob/main/%s', ''),
	'pypiproject': ('https://pypi.org/project/%s', 'pypi:')
}


# ==============================================================================
# Sphinx.Ext.Graphviz
# ==============================================================================
graphviz_output_format = "svg"



# ==============================================================================
# Sphinx.Ext.ToDo
# ==============================================================================
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_link_only = True



# ==============================================================================
# AutoAPI.Sphinx
# ==============================================================================
autoapi_modules = {
  'pyEDAA.IPXACT':  {'output': "pyEDAA.IPXACT", "override": True}
}
