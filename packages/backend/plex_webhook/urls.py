from django.urls import path
from django.conf import settings
from .views import plex_webhook

urlpatterns = [
    path("", plex_webhook, name="plex_webhook"),
]
