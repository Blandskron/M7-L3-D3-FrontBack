import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError as DjangoValidationError

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    """
    Unifica formato de error sin romper los errores estándar de DRF.
    """
    response = exception_handler(exc, context)

    # Si DRF ya creó una respuesta (ValidationError, NotFound, PermissionDenied, etc.)
    if response is not None:
        payload = {
            "error": {
                "type": exc.__class__.__name__,
                "detail": response.data,
            }
        }
        response.data = payload
        return response

    # Errores de validación Django (no DRF)
    if isinstance(exc, DjangoValidationError):
        return Response(
            {"error": {"type": "ValidationError", "detail": exc.message_dict if hasattr(exc, "message_dict") else str(exc)}},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Cualquier otra excepción -> 500
    logger.exception("Unhandled exception", exc_info=exc)
    return Response(
        {"error": {"type": "ServerError", "detail": "Internal server error"}},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )