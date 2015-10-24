"""Authcore utils."""
import datetime
import functools

import django.dispatch

# Signals.
user_nonce_needs_update = django.dispatch.Signal(providing_args=["user"])


def get_usable_nonce():
    """Return an Epoch timestamp."""
    return datetime.datetime.utcnow().strftime('%s')


def bound_user_method_nonce_update(func, presignal=False):
    """Wrap a method bound to the User model and emit a signal to have the user nonce updated.

    :param bool presignal: Emit signal before executing the wrapped function.
    """

    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if presignal:
            user_nonce_needs_update.send(sender=user.__class__, user=user)
            return func(user, *args, **kwargs)

        else:
            output = func(user, *args, **kwargs)
            user_nonce_needs_update.send(sender=user.__class__, user=user)
            return output

    return wrapper
