"""Custom data models."""
from django.db import models


class Org(models.Model):
    """An organization to which groups belong."""

    name = models.String
