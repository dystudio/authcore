"""Authcore serializers."""
import calendar
import datetime

from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm
from rest_framework import serializers
from rest_framework.reverse import reverse

from authcore.models import Org
from authcore_project import settings


class OrgSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize organization objects for viewing."""

    class Meta:
        model = Org
        fields = (
            "id",
            "url",
            "name",
            "groups",
            "users",
        )
        read_only_fields = (
            "id",
            "groups",
            "users",
        )
        extra_kwargs = {
            "groups": {"view_name": "group-detail"},
            "users": {"view_name": "user-detail"}
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
            "id",
            "url",
            "name",
            "permissions",
            "org",
        )
        read_only_fields = ("id",)

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
            "id",
            "url",
            "name",
            "codename",
        )
        read_only_fields = ("id",)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize user objects for viewing."""

    class Meta:
        model = User
        fields = (
            "id",
            "url",
            "username",
            "password",
            "nonce",
            "email",
            "first_name",
            "last_name",
            "groups",
            "orgs",
        )
        read_only_fields = (
            "id",
            "nonce",
            "groups",
            "orgs",
        )
        extra_kwargs = {
            "groups": {"view_name": "group-detail"},
            "orgs": {"view_name": "org-detail"},
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password",
                }
            }
        }

    nonce = serializers.PrimaryKeyRelatedField(read_only=True, source="nonce.value")

    def create(self, validated_data):
        """Handle user creation."""
        user = User.objects.create_user(**validated_data)
        assign_perm('authcore.add_org', user)
        return user

    def update(self, instance, validated_data):
        """Handle user updates."""
        # FIXME(TheDodd): browsable API is requiring password to be passed in during updates. Don't want that.
        # Update basic profile info. Nothing more for now.
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()
        return instance


def jwt_payload_handler(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'nonce': user.nonce.value,
        'exp': datetime.datetime.utcnow() + settings.JWT_AUTH['JWT_EXPIRATION_DELTA'],
    }

    # Include original issued at time for a brand new token, to allow token refresh.
    if settings.JWT_AUTH['JWT_ALLOW_REFRESH']:
        payload['orig_iat'] = calendar.timegm(
            datetime.datetime.utcnow().utctimetuple()
        )

    return payload


def jwt_response_payload_handler(token, user, request):
    """Response payload handler for valid JWT requests."""
    representation = UserSerializer(context={'request': request}).to_representation(user)
    return {
        'token': token,
        'user': representation,
    }
