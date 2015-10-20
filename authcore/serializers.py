from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from authcore.models import Org
# from authcore.models import OrgGroup
# from authcore.models import Permission
# from authcore.models import User
from rest_framework import serializers


class OrgSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize organization objects for viewing."""

    class Meta:
        model = Org
        fields = (
            "url",
            "name",
        )
        read_only_fields = ("groups",)


class GroupOrgOptionsField(serializers.HyperlinkedRelatedField):
    """A custom field to display the possible Orgs that a new group can belong to."""

    def display_value(self, instance):
        return "Org: {name}".format(name=instance.name)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize group objects for viewing."""

    class Meta:
        model = Group
        fields = (
            "url",
            "name",
            "permissions",
            "org",
        )

    org = GroupOrgOptionsField(queryset=Org.objects.all(), view_name="org-detail")


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
            "password",
            "email",
            "first_name",
            "last_name",
            "groups",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password",
                }
            }
        }
