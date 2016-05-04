#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.script import Manager, Server

from msze_www.app import get_app


app = get_app()
manager = Manager(app)
manager.add_command(
    "runserver",
    Server(host="0.0.0.0", port=5000, use_debugger=True))


@manager.command
def show_urls():
    import urllib.parse
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(
            rule.endpoint, methods, rule))
        output.append(line)
    for line in sorted(output):
        print(line)


if __name__ == "__main__":
    manager.run()
