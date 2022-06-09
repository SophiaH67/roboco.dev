from django.urls import path

from nginx.views import nginx_redirect, return_nginx_response

urlpatterns = [
    path(
        "redirectback",
        nginx_redirect,
    ),
    path(
        "<service>",
        return_nginx_response,
    ),
]
