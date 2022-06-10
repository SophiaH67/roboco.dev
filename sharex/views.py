import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

from sharex.forms import ImageUploadForm
from sharex.models import SharexImage

# Create your views here.


@csrf_exempt
def upload(request):
    if request.method == "GET":
        return render(request, "sharex/upload.html")
    if request.method != "POST":
        return HttpResponse(status=405)
    form = ImageUploadForm(request.POST, request.FILES)
    if not form.is_valid():
        return HttpResponse(status=400)
    upload = form.save()

    # Get base url from request
    url = request.build_absolute_uri("/")
    print(url)
    url += f"s/{upload.id}/"
    print(url)

    return HttpResponse(
        json.dumps(
            {
                "url": url,
            }
        )
    )


def view_image(request, id):
    upload = SharexImage.objects.get(id=id)
    return render(request, "sharex/view.html", {"upload": upload})


def serve_image(request, filename):
    file_path = settings.MEDIA_ROOT / "sharex" / filename
    if not os.path.exists(file_path):
        return HttpResponse(status=404)
    return HttpResponse(content=open(file_path, "rb").read(), content_type="image/png")
