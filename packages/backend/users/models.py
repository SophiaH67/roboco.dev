from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    invited_by = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    invites_left = models.IntegerField(default=0)
