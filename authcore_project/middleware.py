"""Middleware for the authcore app."""
import traceback


class StdExceptionMiddleware():
    """Middleware for processing exceptions."""

    def process_exception(self, request, exception):
        # Just dump the exception to standard output.
        traceback.print_exc()
