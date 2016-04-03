"""Authcore permissions."""
from guardian.shortcuts import get_objects_for_user
from rest_framework import permissions


class IsOrgOwnerElseOrgReadOnly(permissions.BasePermission):
    """Org model instance permission check ensuring org owner status."""

    def has_object_permission(self, request, view, obj):
        """Ensure the requesting user is one of the org's owners for non-safe methods."""
        import ipdb;ipdb.set_trace()
        # Only grant read access to users that are members of the Org.
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.users.all()

        # Requesting user must be one of the org's owners.
        return request.user.has_perm('authcore.org_owner', obj)


class IsOrgOwnerForGroupCreation(permissions.BasePermission):
    """Group model permission check ensuring groups can only be created by org owners."""

    def has_permission(self, request, view):
        owned_orgs = get_objects_for_user(request.user, 'authcore.org_owner')
        return len(owned_orgs) > 0
