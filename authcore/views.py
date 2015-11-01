"""Authcore views."""
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.permissions import IsAuthenticated


from authcore.models import Org
from authcore.models import OrgGroup
from authcore.permissions import IsOrgOwnerElseOrgReadOnly
from authcore.permissions import IsOrgOwnerForGroupCreation
from authcore.serializers import GroupSerializer
from authcore.serializers import OrgSerializer
from authcore.serializers import PermissionSerializer
from authcore.serializers import UserSerializer


class OrgViewSet(viewsets.ModelViewSet):
    """API endpoint that allows organizations to be viewed or edited."""
    queryset = Org.objects.none()
    serializer_class = OrgSerializer
    permission_classes = [
        IsAuthenticated,
        DjangoModelPermissions,
        IsOrgOwnerElseOrgReadOnly,
    ]

    def get_queryset(self):
        """Perform filtering based on authenticated user."""
        # Staff has full visibility.
        user = self.request.user
        if user.is_staff:
            return Org.objects.all()

        return user.orgs.all()

    def perform_create(self, serializer):
        """Overload perform_create to ensure requesting user is first Org member."""
        org = serializer.save()
        org.users.add(self.request.user)  # Add requesting user to Org.
        assign_perm('authcore.org_owner', self.request.user, org)


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""
    queryset = Group.objects.none()
    serializer_class = GroupSerializer
    permission_classes = [
        IsAuthenticated,
        IsOrgOwnerForGroupCreation,
    ]

    def get_queryset(self):
        """Perform filtering based on authenticated user."""
        # Staff has full visibility.
        user = self.request.user
        if user.is_staff:
            return Group.objects.all()

        visible_groups = set()
        for org in user.orgs.all():
            for group in org.groups.all():
                visible_groups.add(group.pk)

        return Group.objects.filter(id__in=visible_groups)

    def perform_create(self, serializer):
        """Perform group creation."""
        org = serializer.validated_data.pop("of_org")
        group = serializer.save()
        OrgGroup(org=org, group=group).save()


class PermissionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    # queryset = User.objects.none()
    queryset = User.objects.none()
    serializer_class = UserSerializer

    def get_queryset(self):
        """Perform filtering based on authenticated user."""
        # Staff has full visibility.
        user = self.request.user
        if user.is_staff:
            return User.objects.all()

        # Show all users based upon peer Org membership.
        visible_users = {user.id}
        for org in user.orgs.all():
            for org_user in org.users.all():
                visible_users.add(org_user.id)

        return User.objects.filter(id__in=visible_users)
