# -*- coding: utf-8 -*-
import os

here = os.path.abspath(os.path.join(__file__))
base = os.path.abspath(os.path.join(here, '..'))

DEBUG = False
SECRET_KEY = 'mySecret'
INSTALLED_MODULES = os.getenv(
    'INSTALLED_MODULES',
    ';'.join(['app.apis.v1'])
).split(';')

# Database
DB_DRIVER = os.getenv('DB_DRIVER', 'postgresql+psycopg')
DB_USERNAME = os.getenv('DB_USERNAME', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_DATABASE = os.getenv('DB_DATABASE', 'flask')
SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
    DB_DRIVER, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE)
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
