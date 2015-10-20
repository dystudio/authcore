"""Custom data models."""
from django.contrib import auth
from django.db import models


class Org(models.Model):
    """An organization to which groups belong.

    Indexes:
    - name: unique index.
    """

    name = models.CharField(max_length=50, unique=True)


class OrgGroup(models.Model):
    """A profile model for linking Groups and Orgs."""

    group = models.OneToOneField(auth.models.Group, related_name="org", related_query_name="org")
    org = models.ForeignKey(Org, related_name="groups", related_query_name="group")
