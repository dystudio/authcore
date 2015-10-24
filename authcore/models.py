"""Custom data models."""
from django.contrib import auth
from django.db import models


# Force the standard User model to require unique emails for users.
auth.models.User._meta.get_field('email')._unique = True
auth.models.User._meta.get_field('email')._required = True


class Org(models.Model):
    """An organization to which groups belong."""

    name = models.CharField(max_length=50, unique=True)
    users = models.ManyToManyField(auth.models.User, related_name="orgs", related_query_name="orgs")


class OrgGroup(models.Model):
    """A profile model for linking Groups and Orgs."""

    group = models.OneToOneField(auth.models.Group, related_name="org", related_query_name="org")
    org = models.ForeignKey(Org, related_name="groups", related_query_name="group")
