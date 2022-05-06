from rest_framework.views import exception_handler
from rest_framework.response import Response


class CustomException(Exception):
    def __init__(self, status_code, message, attr) -> None:
        self.status = status_code
        self.data = {
            attr: [message]
        }

def custom_exception_handler(exc, context):
    if isinstance(exc, CustomException):
        return Response(data=exc.data, status=exc.status)
    response = exception_handler(exc, context)
    return response
