#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# General Settings
AUTHOR = 'Matthew Geiger'
SITENAME = "Matthew Geiger's Blog"
#SITEURL = 'https://mgeiger.github.io'
SITEURL = ''
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Paths
PATH = 'content'
ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

DEFAULT_METADATA = {
}
# Drafts
DRAFT_URL = 'drafts/{slug}.html'


# Feeds
# Feed generation is usually not desired when developing
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = 'feeds/{slug}.tag.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
# MENUITEMS = [
#     ['RSS', "feeds/all.atom.xml"]
# ]

# Social
# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = None
# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/matthewjgeiger'),
        ('GitHub', 'https://github.com/mgeiger'),
        ('Twitter', 'https://twitter.com/mgeiger1980'))
# GITHUB_USER = 'mgeiger'
GITHUB_SKIP_FORK = True
# GITHUB_REPO_COUNT = 0
TWITTER_USERNAME = 'mgeiger1980'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
        'extra/robots.txt', 
        'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/favicon.ico': {'path': 'favicon.ico'},
}
PLUGIN_PATHS = [
        './pelican-plugins/',
]
PLUGINS = [
        'i18n_subsites', 
        'similar_posts',
        'readtime'
]
JINJA_ENVIRONMENT = {
        'extensions': ['jinja2.ext.i18n'],
}

# Similar Posts
SIMILAR_POSTS_MAX_COUNT = 10

# Rendering
TYPOGRIFY = True
THEME = './pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'paper'  # yeti is also nice
DEFAULT_PAGINATION = 5
# SUMMARY_MAX_LENGTH = 50
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
READING_TIME_LOWER_LIMIT = 1

# About Me
SHOW_ABOUTME = True
AVATAR = "images/profile.jpg"
ABOUT_ME = """
Software Engineer who loves working with Python
<br />
<br />
Currently working as a Senior Automation Engineer at Bose
"""
