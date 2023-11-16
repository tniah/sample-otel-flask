# -*- coding: utf-8 -*-
"""This module implements a custom class of flask_restx.api.Api."""
import os
from distutils.util import strtobool

from flask import url_for
from flask_restx import Api as _Api


class Api(_Api):
    """Custom class of flask_restx.api.Api."""

    @property
    def specs_url(self):
        """Fixes issue where swagger-ui makes a call to swagger.json
        over HTTPs."""
        scheme = (
            'https'
            if strtobool(os.getenv('FORCE_SWAGGER_JSON_HTTPS', 'false'))
            else 'http')
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)
