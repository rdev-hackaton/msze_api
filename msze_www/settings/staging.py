# -*- coding: utf-8 -*-
import os

ENV_NAME = "staging"
DEBUG = os.environ.get("FLASK_DEBUG", False) == "True"
