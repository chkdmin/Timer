# -*- coding: utf-8 -*-

DEBUG = False

START_DATE_STRING = '2017-03-15'
END_DATE_STRING = '2020-01-14'

# Flask-S3
FLASKS3_BUCKET_NAME = 'zappa-slave-timer'
FLASKS3_FILEPATH_HEADERS = {
    r'.css$': {
        'Content-Type': 'text/css',
    }
}
