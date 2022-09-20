# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'XIVITA Docker Dalamud'
copyright = '2022, FFXIVITA'
author = 'XIVITA'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_ahd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_ahd_theme'
html_static_path = ['_static']
html_theme_options = dict(
    project_name="XIVITA Docker Dalamud",
    logo_alt="FFXIVITA",
    logo="img/ffxivita.svg",
    logo_width=45,
    logo_url="/",
    footer_links=",".join([
        "FFXIVITA|https://ffxivita.it/",
        "Lista Plugin|https://ffxivita.github.io/XIVITADalamudPlugins/",
        "Discord|https://discord.gg/ffxivita",
    ]),
    header_links="Sito Ufficiale|https://ffxivita.it, Directory Plugin|https://ffxivita.github.io/XIVITADalamudPlugins/",
    github_url="https://github.com/ffxivita/docker-dalamud/blob/main/source/"
)
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
master_doc = 'index'
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', 'requirements.txt']
today_fmt = '%d-%m-%Y %H:%M'
gettext_uuid = True
gettext_compact = False
