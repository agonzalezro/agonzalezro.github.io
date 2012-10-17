#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Álex González'
SITENAME = 'Ehyyy, non hai fallo!'
SITEURL = 'http://example.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Paylogic', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Google', 'http://python.org'),
          ('Shit', '#'),
          ('Shit1', '#'),
          ('Shit2', '#'))

# Social widget
SOCIAL = (('Twitter', '#'),
          ('Facebook', '#'),
          ('Google+', '#'))

DEFAULT_PAGINATION = 3

GITHUB_ACTIVITY_FEED = 'https://github.com/agonzalezro.atom'
GITHUB_URL = 'http://agonzalezro.github.com/'
LICENSE = 'SHITTY GPL'


PLUGINS = ['pelican.plugins.github_activity',
           'pelican.plugins.gravatar',
           'pelican.plugins.global_license']

TAG_CLOUD_STEPS = 4
TAG_CLOUD_STEPSG_CLOUD_MAX_ITEMS = 100

MENUITEMS = SOCIAL

TWITTER_USERNAME = 'agonzalezro'

# global metadata to all the contents
DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["pictures", ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

DISQUS_SITENAME = 'agonzalezro'

##THEME = 'simple'
##THEME = 'brownstone'
##THEME = 'mnmlist'

THEME = '_dev_theme'
#THEME = 'notmyidea-cms'
#THEME = 'subtle'

#interesante# THEME = 'tuxlite_tbs'  # parecido a bootstrap
#THEME = 'dev-random'  # bastante parecido a lo que quiero

OUTPUT_PATH = '.'
DELETE_OUTPUT_DIRECTORY = False
