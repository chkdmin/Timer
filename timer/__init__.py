# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser

from flask import Flask
from flask_s3 import FlaskS3

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'templates')
STATIC_DIR = os.path.join(ROOT_DIR, 'static')


def create_app():
    app_ = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
    app_.config['DEBUG'] = False

    with open(os.path.join(ROOT_DIR, '.aws/credentials')) as f:
        config = ConfigParser()
        config.read_file(f)
        app_.config['AWS_ACCESS_KEY_ID'] = config['zappa-personal']['aws_access_key_id']
        app_.config['AWS_SECRET_ACCESS_KEY'] = config['zappa-personal']['aws_secret_access_key']
    app_.config['FLASKS3_BUCKET_NAME'] = 'zappa-slave-timer'
    s3 = FlaskS3(app_)
    return app_


app = create_app()
import timer.views
