from django.db import models
from .services import services


class Nginx(models.Model):
    class Meta:
        permissions = [
            (service_permission, permission_description)
            for service_name, service_url, service_permission, permission_description in services
        ]
