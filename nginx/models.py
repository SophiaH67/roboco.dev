from django.db import models

permissions = [
    ("can_access_sonarr", "Can access Sonarr", "sonarr"),
    ("can_access_radarr", "Can access Radarr", "radarr"),
    ("can_access_lidarr", "Can access Lidarr", "lidarr"),
    ("can_access_qbittorrent", "Can access QBittorrent", "qbittorrent"),
]


class Nginx(models.Model):
    class Meta:
        permissions = [(code, name) for code, name, service in permissions]
