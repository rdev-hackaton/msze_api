# -*- coding: utf-8 -*-
import os
import sys

from flask import Flask
from werkzeug.datastructures import ImmutableDict
from whitenoise import WhiteNoise

from .controllers import register_controllers


DEV_MODE = any(command in sys.argv for command in ('runserver', 'show_urls'))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')


# Hamlish support
class FlaskWithHamlish(Flask):
    jinja_options = ImmutableDict(
        extensions=[
            'jinja2.ext.autoescape',
            'jinja2.ext.with_',
            'hamlish_jinja.HamlishExtension'
        ]
    )


def get_app():
    # Hamlish
    app = FlaskWithHamlish(__name__)
    app.jinja_env.hamlish_enable_div_shortcut = True
    app.jinja_env.hamlish_mode = 'debug'

    # app setup
    app.config.from_object('msze_www.settings')
    app.config.from_envvar('FLASK_SETTINGS')
    register_controllers(app)

    # static files
    if not DEV_MODE:
        app = WhiteNoise(app, root=STATIC_DIR, prefix='static')

    return app
