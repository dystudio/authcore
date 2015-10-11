"""Custom data models."""
# from django.contrib import auth
from django.db import models


class Org(models.Model):
    """An organization to which groups belong.

    Indexes:
    - name: unique index.
    """

    name = models.CharField(max_length=50, unique=True)


# class Group(auth.models.Group):
#     """A subclass of the `django.contrib.auth.models.Group` model."""
#     class Meta:
#         proxy = True
#         unique_together = ("name", "org")  # The combination of these fields must be unique.

#     org = models.ForeignKey(auth.models.Org, db_index=True)


# class Permission(auth.models.Permission):
#     """A subclass of the `django.contrib.auth.models.Permission` model.

#     Indexes:
#     - codename: indexed for standard queries.
#     - name: unique index.
#     """

#     codename = models.CharField(max_length=100, db_index=True)
#     name = models.CharField(max_length=255, unique=True)


# class User(auth.models.User):
#     """A subclass of the `django.contrib.auth.models.User` model.

#     Indexes:
#     - codename: indexed for standard queries.
#     - name: unique index.
#     """

#     email = models.EmailField(max_length=254, required=True, unique=True)
#     # username = models.CharField(max_length=30, )
#     # username.required = False  # Ensure this field is not required.
#     # username.unique = True  # Ensure this field is unique.
