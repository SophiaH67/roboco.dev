from copy import deepcopy
from django.http import HttpResponse
from django.shortcuts import render
from nginx.services import services

routes = [
    ("https://c.roboco.dev/", "NextCloud"),
    ("https://c.roboco.dev/apps/", "Apps"),
    ("https://mail.roboco.dev/", "Email"),
]

# Sort routes by name
routes.sort(key=lambda x: x[1])


def index(request):
    services_clone = deepcopy(services)
    # Replace all [2](permission string) with a actual permission object
    for service in services_clone:
        service[2] = request.user.has_perm(f"nginx.{service[2]}")

    context = {
        "services": services_clone,
    }
    return render(request, "roboco/index.html", context)


def why(request):
    return render(request, "roboco/why.html")
