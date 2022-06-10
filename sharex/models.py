import uuid
from django.db import models

from users.models import User

# Create your models here.
class SharexImage(models.Model):
    image = models.ImageField(upload_to="sharex")
    title = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # uploader = models.ForeignKey(User, on_delete=models.CASCADE)
