#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import (
    Flask,
    redirect,
    render_template,
)
from werkzeug.datastructures import ImmutableDict


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
    app = FlaskWithHamlish(__name__)
    app.jinja_env.hamlish_enable_div_shortcut = True
    app.jinja_env.hamlish_mode = 'debug'

    app.config['MOBILE_APP_STORE_URL'] = 'https://www.google.com'
    register_pages(app)
    return app


def register_pages(app: Flask):

    @app.route('/')
    def index():
        return redirect(app.config['MOBILE_APP_STORE_URL'], code=302)

    @app.route('/test/')
    def test_page():
        return render_template('test_page.haml')
