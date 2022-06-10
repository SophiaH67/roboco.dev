from django import forms
from django.forms import ModelForm
from sharex.models import SharexImage


class ImageUploadForm(ModelForm):
    class Meta:
        model = SharexImage
        fields = ["image", "title"]
