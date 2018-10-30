#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime 
from pathlib import Path


CURRENT_DIR_PATH = Path(__file__).resolve().parent

AUTHOR = 'Python Granada'
SITENAME = 'Python Granada'
SITESUBTITLE = u'La comunidad dedicada a Python en Granada y alrededores'


THEME = '{}/themes/MinimalXY'.format(CURRENT_DIR_PATH)
NEST_CSS_MINIFY = True

MINIMALXY_FAVICON = 'extra/favicon.ico'

MINIMALXY_CURRENT_YEAR = 2018

#MENUITEMS = [('Homepage', '/')]
HEADER_IMAGES = 'header.png'
HEADER_LOGO = 'logo.png'


PATH = 'content'
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Publish
DELETE_OUTPUT_DIRECTORY = False


# Blogroll
LINKS = (('Python España', 'https://www.es.python.org/'),
         ('PyCon18 Málaga', 'https://2018.es.pycon.org/'),
   		)

# Social widget
SOCIAL = (('@python_granada', 'https://twitter.com/python_granada'),
          ('Grupo de Telegram', 'https://telegram.me/pythongranada'),)


DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.jpg']

SUMMARY_MAX_LENGTH = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
