#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matthew Geiger'
SITENAME = 'Geiger Labs Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/matthewjgeiger'),
        ('GitHub', 'https://github.com/mgeiger'),)

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/favicon.ico': {'path': 'favicon.ico'},
        }
TYPOGRIFY = True
PLUGIN_PATHS = ['../pelican-plugins/', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
        'extensions': ['jinja2.ext.i18n'],
        }
THEME = '../pelican-themes/pelican-bootstrap3'
