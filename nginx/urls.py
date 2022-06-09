from django.urls import path

from nginx.views import nginx_redirect, return_nginx_response
from .models import permissions as nginx_permissions

services = [service for code, name, service in nginx_permissions]
urlpatterns = [
    path(
        "redirectback",
        nginx_redirect,
    ),
    path(
        "<service>",
        return_nginx_response,
    )
]
