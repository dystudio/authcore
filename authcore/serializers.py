from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse

from authcore.models import Org


class OrgSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize organization objects for viewing."""

    class Meta:
        model = Org
        fields = (
            "url",
            "name",
            "groups",
            "users",
        )
        extra_kwargs = {
            "groups": {
                "read_only": True,
                "view_name": "group-detail",
            },
            "users": {
                "read_only": True,
                "view_name": "user-detail",
            }
        }


class GroupOrgField(serializers.HyperlinkedRelatedField):
    """A custom field to display the possible Orgs that a new group can belong to."""

    def display_value(self, instance):
        return "Org: {name}".format(name=instance.name)

    def get_url(self, obj, view_name, request, format):
        if isinstance(obj, Org):
            url_kwargs = {"pk": obj.pk}

        else:
            url_kwargs = {"pk": obj.org.pk}

        return reverse("org-detail", kwargs=url_kwargs, request=request, format=format)


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

    org = GroupOrgField(queryset=Org.objects.all(), view_name="org-detail")

    def update(self, instance, validated_data):
        """Handle group updates."""
        # Only allow for group name & permissions to be changed.
        instance.name = validated_data.get("name", instance.name)
        instance.permissions = validated_data.get("permissions", instance.permissions)
        instance.save()
        return instance


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
            "orgs",
        )
        extra_kwargs = {
            "groups": {
                "read_only": True,
                "view_name": "group-detail",
            },
            "orgs": {
                "read_only": True,
                "view_name": "org-detail",
            },
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password",
                }
            }
        }

    def create(self, validated_data):
        """Handle user creation."""
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Handle user updates."""
        # FIXME(TheDodd): browsable API is requiring password to be passed in during updates. Don't want that.
        # Update basic profile info. Nothing more for now.
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()
        return instance
