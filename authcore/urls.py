"""URL conf for the authcore app."""
from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers

from authcore import views

# Build up authcore router.
authcore_router = routers.DefaultRouter()
authcore_router.register(r'orgs', views.OrgViewSet)
authcore_router.register(r'groups', views.GroupViewSet)
authcore_router.register(r'permissions', views.PermissionViewSet)
authcore_router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^', include(authcore_router.urls)),
]
