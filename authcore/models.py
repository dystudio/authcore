"""Custom data models."""
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import Group
from django.core.validators import RegexValidator
from django.db import models

from authcore.utils import get_usable_nonce


class UserManager(BaseUserManager):
    """Authcore custom user manager."""

    def create_user(self, username, password, **other_fields):
        """."""
        import ipdb;ipdb.set_trace()
        print("testing")
        pass

    def create_superuser(self, username, password, **other_fields):
        """."""
        import ipdb;ipdb.set_trace()
        print("testing")
        pass


class User(AbstractBaseUser):
    """Authcore custom user model."""

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('username', 'email', 'password')

    objects = UserManager()
    username = models.CharField(max_length=30, validators=[
        RegexValidator(
            regex=r'^[-A-Za-z0-9_@+.]+$',
            message='Username must be alphanumeric and may contain _, @, +, . and -.'
        )
    ])
    email = models.EmailField(unique=True)
    first_name = CharField(max_length=30, blank=True)
    last_name = CharField(max_length=30, blank=True)

    def set_password(self, raw_password):
        """Overload set password to update user nonce."""
        output = super(User, self).set_password(raw_password)

        # Only attempt to create a nonce if the user has been saved to disk.
        if self.id:
            UserNonce(user=self).save()

        return output

    def set_unusable_password(self):
        """Overload set password to update user nonce."""
        output = super(User, self).set_unusable_password()

        # Only attempt to create a nonce if the user has been saved to disk.
        if self.id:
            UserNonce(user=self).save()

        return output


class Org(models.Model):
    """An organization to which groups belong."""

    name = models.CharField(max_length=50, unique=True)
    users = models.ManyToManyField(User, related_name="orgs", related_query_name="orgs")


class OrgGroup(models.Model):
    """A profile model for linking Groups and Orgs."""

    group = models.OneToOneField(Group, related_name="org", related_query_name="org")
    org = models.ForeignKey(Org, related_name="groups", related_query_name="group")


class UserNonce(models.Model):
    """A profile model for linking a nonce value with a User.

    This is implemented specifically for invalidating JWTs under needed circumstances, as JWTs
    are typically not stored in a database.
    """
    user = models.OneToOneField(User, related_name="nonce", related_query_name="nonce")
    value = models.CharField(max_length=255, default=get_usable_nonce)
