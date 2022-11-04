from django.urls import path
from .views import upload, view_image, serve_image, create_token
from django.conf import settings

urlpatterns = [
    path("s/upload", upload, name="upload"),
    path("s/<str:id>/", view_image, name="view"),
    path("sharex/<str:filename>/", serve_image, name="serve"),
    path("s/create_token", create_token, name="create_token"),
]
