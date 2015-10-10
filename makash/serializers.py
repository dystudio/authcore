from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
# from makash.models import Group
from makash.models import Org
# from makash.models import Permission
# from makash.models import User
from rest_framework import serializers


class OrgSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize organization objects for viewing."""

    class Meta:
        model = Org
        fields = (
            "url",
            "name",
        )


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
    """Serialize permission objects for viewing."""

    class Meta:
        model = Permission
        fields = (
            "url",
            "name",
            "codename",
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
