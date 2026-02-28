from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def ilimi_exception_handler(exc, context):
    """
    Custom exception handler that formats all errors
    using the Ilimi API response envelope.
    """
    response = exception_handler(exc, context)

    if response is not None:
        error_detail = response.data

        if isinstance(error_detail, dict) and 'detail' in error_detail:
            message = str(error_detail['detail'])
            errors = None
        elif isinstance(error_detail, dict):
            message = 'Validation failed'
            errors = error_detail
        else:
            message = str(error_detail)
            errors = None

        response.data = {
            'status': 'error',
            'message': message,
            'data': None,
            'errors': errors,
        }

    return response