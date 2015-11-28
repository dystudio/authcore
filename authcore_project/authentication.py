"""Authcore authentication protocols."""
import functools

from django.utils.translation import ugettext as _
from rest_framework import exceptions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import VerificationBaseSerializer


class JSONWebTokenAuthenticationWithNonce(JSONWebTokenAuthentication):

    def authenticate_credentials(self, payload):
        """Overload authentication protocol to check user nonce as well."""
        user = super(JSONWebTokenAuthenticationWithNonce, self).authenticate_credentials(payload)
        if user.nonce.value != payload['nonce']:
            msg = _('Invalid nonce.')
            raise exceptions.AuthenticationFailed(msg)

        return user


def check_user_enforce_nonce(func):
    """Wrap the JWT check user protocl to also check the user's nonce."""

    @functools.wraps(func)
    def wrapper(self, payload, *args, **kwargs):
        user = func(self, payload, *args, **kwargs)
        if user.nonce.value != payload['nonce']:
            msg = _('Invalid nonce.')
            raise exceptions.AuthenticationFailed(msg)

        return user

    return wrapper

VerificationBaseSerializer._check_user = check_user_enforce_nonce(VerificationBaseSerializer._check_user)
