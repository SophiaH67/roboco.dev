from django import forms
from django.forms import ModelForm
from sharex.models import SharexImage, SharexToken


class ImageUploadForm(ModelForm):
    class Meta:
        model = SharexImage
        fields = ["image", "title"]

    def save(self, user):
        self.instance.uploader = user
        return super().save()
