#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Maxime Trebitsch'
SITENAME = u'Maxime Trebitsch'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
DISPLAY_TAGS_ON_SIDEBAR = False


# # Pages settings
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# Menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Research', 'research.html'),
    ('CV', 'cv.html'),
    ('Contact', 'contact.html'),
)

AVATAR = "img/maximetrebitsch.jpg"
ABOUT_ME = "I'm a post-doctoral researcher in astrophysics working within the BLACK project at the IAP in Paris, interested in high-redshift galaxy formation."


# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/maximetrebitsch'),
          ('Bitbucket', 'https://bitbucket.org/mtrebitsch'),
          ('GitHub', 'https://github.com/mtrebitsch'),
          ('ResearchGate', 'https://www.researchgate.net/profile/Maxime_Trebitsch'),
)
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'cosmo'

PLUGIN_PATHS = ['../pelican-utils/pelican-plugins']
PLUGINS = ['render_math',
           'twitter_bootstrap_rst_directives',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', # 'liquid_tags.notebook'
]

MATH_JAX = {'mathjax_font': 'sanserif'}


STATIC_PATHS = ['img', 'pdf', 'video']
TYPOGRIFY = True
TWITTER_USERNAME = 'maximetrebitsch'
