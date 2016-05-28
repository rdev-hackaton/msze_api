# -*- coding: utf-8 -*-
from flask import (
    Flask,
    make_response,
    redirect,
    render_template,
    send_file,
)


def register_controllers(app: Flask):

    @app.route('/')
    def index():
        return redirect(app.config['MOBILE_APP_STORE_URL'], code=302)

    @app.route('/test/')
    def test_page():
        return render_template('test_page.haml')

    @app.route(app.config['DATAFILE_URL_PATH'])
    def datafile_page():
        file_content = send_file(app.config['DATAFILE_FILEPATH'])
        response = make_response(file_content)
        response.mimetype = 'application/json'
        return response

    @app.after_request
    def add_header(response):
        response.cache_control.max_age = app.config['CACHE_TIME']
        return response
