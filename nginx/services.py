# [service_name, service_url, service_permission, permission_description]
services = [
    ["sonarr", "https://sonarr.roboco.dev/", "can_access_sonarr", "Can access Sonarr"],
    ["radarr", "https://radarr.roboco.dev/", "can_access_radarr", "Can access Radarr"],
    ["lidarr", "https://lidarr.roboco.dev/", "can_access_lidarr", "Can access Lidarr"],
    [
        "qbittorrent",
        "https://qbittorrent.roboco.dev/",
        "can_access_qbittorrent",
        "Can access QBittorrent",
    ],
    [
        "nextcloud",
        "https://c.roboco.dev/",
        "can_access_nextcloud",
        "Can access Nextcloud",
    ],
]

# Sort the services by name
services.sort(key=lambda x: x[0])
