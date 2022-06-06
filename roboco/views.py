from django.http import HttpResponse
from django.shortcuts import render

routes = [
    ("https://c.roboco.dev/", "NextCloud"),
    ("https://c.roboco.dev/apps/", "Apps"),
    ("https://mail.roboco.dev/", "Email"),
]

# Sort routes by name
routes.sort(key=lambda x: x[1])


def index(request):
    context = {
        "routes": routes,
    }
    return render(request, "roboco/index.html", context)


def why(request):
    return render(request, "roboco/why.html")
