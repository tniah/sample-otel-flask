# -*- coding: utf-8 -*-
import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
DEFAULT_CONFIG_PATH = os.path.join(BASE_PATH, 'default.py')
DEVELOPMENT_CONFIG_PATH = os.path.join(BASE_PATH, 'development.py')
PRODUCTION_CONFIG_PATH = os.path.join(BASE_PATH, 'production.py')
TEST_CONFIG_PATH = os.path.join(BASE_PATH, 'test.py')
