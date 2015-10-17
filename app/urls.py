"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers
from rest_framework_expiring_authtoken.views import obtain_expiring_auth_token

from authcore import views

# Build up authcore router.
authcore_router = routers.DefaultRouter()
authcore_router.register(r'groups', views.GroupViewSet)
authcore_router.register(r'orgs', views.OrgViewSet)
authcore_router.register(r'permissions', views.PermissionViewSet)
authcore_router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [

    # Register the obtain token endpoint.
    url(r'^auth/tokens/?', obtain_expiring_auth_token),

    # Register the login URLs for the browsable API.
    url(r'^auth/login/?', include('rest_framework.urls', namespace='rest_framework')),

    # Register authcore router.
    url(r'^', include(authcore_router.urls)),

]
