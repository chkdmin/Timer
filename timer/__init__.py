# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser

from flask import Flask
from flask_s3 import FlaskS3

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'templates')
STATIC_DIR = os.path.join(ROOT_DIR, 'static')
s3 = FlaskS3()


def init_config(app_):
    from timer import config
    for c in dir(config):
        if c.startswith('__') and c.endswith('__'):
            continue
        attr = getattr(config, c, None)
        if attr is None:
            continue

        app_.config[c] = attr


def init_flask_s3(app_):
    with open(os.path.join(ROOT_DIR, '.aws/credentials')) as f:
        config = ConfigParser()
        config.read_file(f)
        app_.config['AWS_ACCESS_KEY_ID'] = config['zappa-personal']['aws_access_key_id']
        app_.config['AWS_SECRET_ACCESS_KEY'] = config['zappa-personal']['aws_secret_access_key']

    s3.init_app(app_)


def create_app():
    app_ = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
    init_config(app_)
    init_flask_s3(app_)
    return app_


app = create_app()
import timer.views
