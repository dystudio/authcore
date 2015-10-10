# from makash.models import Group
from makash.models import Org
# from makash.models import Permission
# from makash.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from makash.serializers import GroupSerializer
from makash.serializers import OrgSerializer
from makash.serializers import PermissionSerializer
from makash.serializers import UserSerializer
from rest_framework import viewsets


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
