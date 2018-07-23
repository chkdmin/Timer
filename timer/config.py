# -*- coding: utf-8 -*-

import os

DEBUG = True

START_DATE_STRING = '2017-03-15'
END_DATE_STRING = '2020-01-14'

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'templates')
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

# Flask-S3
FLASKS3_BUCKET_NAME = 'zappa-slave-timer'
FLASKS3_FILEPATH_HEADERS = {
    r'.css$': {
        'Content-Type': 'text/css',
    }
}
