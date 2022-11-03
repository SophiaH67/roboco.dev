import uuid
from django.conf import settings
from django.db import models

from users.models import User

# Create your models here.
class SharexImage(models.Model):
    image = models.ImageField(upload_to="sharex")
    title = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class SharexToken(models.Model):
    token = models.CharField(max_length=255, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sharex_tokens"
    )
