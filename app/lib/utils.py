# -*- coding: utf-8 -*-
"""Common functions and utilities."""


def parse_marshmallow_error(err):
    """Parse the marshmallow error.

    Args:
        err: Instance of marshmallow.ValidationError
    Returns:
        Error details.
    """
    error_details = []
    err_messages = err.normalized_messages()
    for field_name, message in err_messages.items():
        if isinstance(message, list):
            error_details.extend([
                {'target': field_name, 'message': msg}
                for msg in message
            ])
        else:
            error_details.append({
                'target': field_name,
                'message': message})
    return error_details
