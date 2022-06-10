from django.urls import path
from .views import upload, view_image, serve_image
from django.conf import settings

urlpatterns = [
    path("s/upload", upload, name="index"),
    path("s/<str:id>/", view_image, name="view"),
    # MEDIA_ROOT
    path("sharex/<str:filename>/", serve_image, name="serve"),
]
