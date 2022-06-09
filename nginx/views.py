from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .services import services

service_names = [
    service_name
    for service_name, service_url, service_permission, permission_description in services
]


def return_nginx_response(request, service):
    # If user is not logged in, return 401
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)
    try:
        index = service_names.index(service)
    except ValueError:
        return HttpResponse("Service not found", status=404)
    permission = services[index][0]
    # Check if the user has the permission to access the service
    if request.user.has_perm(f"nginx.{permission}"):
        return HttpResponse("OK", status=200)
    else:
        return HttpResponse("Forbidden", status=403)


@login_required
def nginx_redirect(request):
    # Get redirect out of GET parameters
    redirect_url = request.GET.get("redirect", "https://roboco.dev/")
    # Redirect to the redirect_url
    return HttpResponseRedirect(redirect_url)
