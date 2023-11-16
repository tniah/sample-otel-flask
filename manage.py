# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

from app import create_app

# Load dotenv in the base root
root_app = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path=os.path.join(root_app, '.env'), override=True)

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
