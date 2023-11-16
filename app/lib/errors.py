# -*- coding: utf-8 -*-
"""Error classes."""
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


class ApiHTTPError(Exception):
    """Base error class for API HTTP errors."""
    http_status = 500

    def __init__(self, message=None, error_details=None):
        """Initialize the class object.

        Args:
            message: A short description of the error.
            error_details: More details about the error.
        """
        self.message = message or HTTP_STATUS_CODES[self.http_status]
        self.error_details = error_details

    def build_response(self):
        """Create a response object.

        Returns:
            Response object (instance of flask.wrappers.Response)
        """
        error = {
            'code': self.http_status,
            'message': self.message
        }
        if self.error_details:
            error['details'] = self.error_details
        resp = jsonify(error)
        resp.status_code = self.http_status
        return resp


class BadRequestError(ApiHTTPError):
    """Raised when the Flask app cannot or will not process the request."""
    http_status = 400


class UnauthorizedError(ApiHTTPError):
    """Raised when the request lacks valid authentication credentials
    for the target resource."""
    http_status = 401


class ForbiddenError(ApiHTTPError):
    """Raised when the Flask app understood the request
    but refuses to authorize it."""
    http_status = 403


class NotFoundError(ApiHTTPError):
    """Raised when the requested resource could not be found."""
    http_status = 404


class MethodNotAllowedError(ApiHTTPError):
    """Raised when the Flask app knows the request method, but the target
    resource does not support this method."""
    http_status = 405


class UnsupportedMediaTypeError(ApiHTTPError):
    """Raised when the Flask app refuses to accept the request because the
    payload format is in an unsupported format."""
    http_status = 415
