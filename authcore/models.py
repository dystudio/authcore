"""Custom data models."""
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from authcore.utils import get_usable_nonce
from authcore.utils import bound_user_method_nonce_update
from authcore.utils import user_nonce_needs_update


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

    @staticmethod
    @receiver(post_save, sender=User)
    def create_user_nonce(sender, instance, created, **kwargs):
        """Create a user's nonce."""
        if created:
            UserNonce(user=instance).save()

    @staticmethod
    @receiver(user_nonce_needs_update)
    def update_user_nonce(user, **kwargs):
        """Update a user's nonce."""
        # If user has not been saved yet, then do nothing.
        if not user.id:
            return

        # Else, just update it.
        else:
            user.nonce.value = get_usable_nonce()
            user.nonce.save()


#######################
# User model updates. #
#######################
# Force the standard User model to require unique emails for users.
User._meta.get_field('email')._unique = True
User._meta.get_field('email')._required = True

# Ensure these user methods update the user's nonce.
User.set_password = bound_user_method_nonce_update(User.set_password)
User.set_unusable_password = bound_user_method_nonce_update(User.set_unusable_password)
