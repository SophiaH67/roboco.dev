import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings
from dns import reversename, resolver

from sharex.forms import ImageUploadForm
from sharex.models import SharexImage, SharexToken
from sharex.token import generate_sharex_token, validate_sharex_token
from users.models import User

# Create your views here.


@csrf_exempt
def upload(request):
    if request.method == "GET":
        return render(request, "sharex/upload.html")
    if request.method != "POST":
        return HttpResponse(status=405)

    user_id = validate_sharex_token(request.POST.get("token"))
    if user_id is None:
        return HttpResponse(status=403)

    form = ImageUploadForm(request.POST, request.FILES)

    if not form.is_valid():
        return HttpResponse(status=400)
    user = User.objects.get(id=user_id)
    upload = form.save(user)

    # Get base url from request
    url = request.build_absolute_uri("/")
    url += f"s/{upload.id}/"

    return HttpResponse(
        json.dumps(
            {
                "url": url,
            }
        )
    )


def view_image(request, id):
    upload = SharexImage.objects.get(id=id)
    image_url = request.build_absolute_uri(f"/{upload.image}")
    # Either x-forwarded-for or remote_addr
    ip = request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR"))
    # Reverse lookup the IP
    try:
        ip = reversename.from_address(ip)
        ip = resolver.query(ip, "PTR")[0].to_text()
    except:
        ip = "Unknown"
    print(f"{ip} requested {image_url}")
    if "discord" in ip.lower() or "googleusercontent" in ip.lower():
        return redirect(image_url)

    return render(
        request, "sharex/view.html", {"upload": upload, "image_url": image_url}
    )


def serve_image(request, filename):
    file_path = settings.MEDIA_ROOT / "sharex" / filename
    if not os.path.exists(file_path):
        return HttpResponse(status=404)
        # accept-ranges: bytes
    return HttpResponse(content=open(file_path, "rb").read(), content_type="image/png")


@login_required
def create_token(request):
    if request.method != "POST":
        return redirect("upload")
    token = SharexToken.objects.create(
        user=request.user, token=generate_sharex_token(request.user.id)
    )
    return HttpResponse(token.token, content_type="text/plain; charset=utf-8")
