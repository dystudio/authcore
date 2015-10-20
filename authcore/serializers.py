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
        )
        extra_kwargs = {
            "groups": {
                "view_name": "group-detail",
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
