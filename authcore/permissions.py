"""Authcore permissions."""
from rest_framework import permissions


class IsOrgOwnerOrMemberReadOnly(permissions.BasePermission):
    """Object-level org permission representing ownership."""

    def has_object_permission(self, request, view, obj):
        # Only grant read access to users that are members of the Org.
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.users.all()

        # Requesting user must be one of the org's owners.
        return request.user.has_perm('org_owner', obj)
