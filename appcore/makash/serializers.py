from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize group objects for viewing."""

    class Meta:
        model = Group
        fields = (
            "url",
            "name",
            "permissions",
        )


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize perission objects for viewing."""

    class Meta:
        model = Permission
        fields = (
            "url",
            "name",
            "codename",
            "content_type",
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize user objects for viewing."""

    class Meta:
        model = User
        fields = (
            "url",
            "username",
            "email",
            "first_name",
            "last_name",
            "groups",
        )
