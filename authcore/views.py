from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from rest_framework import viewsets

from authcore.models import Org
from authcore.serializers import GroupSerializer
from authcore.serializers import OrgSerializer
from authcore.serializers import PermissionSerializer
from authcore.serializers import UserSerializer


class OrgViewSet(viewsets.ModelViewSet):
    """API endpoint that allows organizations to be viewed or edited."""
    queryset = Org.objects.all()
    serializer_class = OrgSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Overload perform_create to ensure password is set correctly."""
        user = serializer.save()
        user.set_password(serializer.validated_data["password"])
        user.save()
