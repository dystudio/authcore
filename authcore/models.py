"""Custom data models."""
from django.db import models


class Org(models.Model):
    """An organization to which groups belong.

    Indexes:
    - name: unique index.
    """

    name = models.CharField(max_length=50, unique=True)
