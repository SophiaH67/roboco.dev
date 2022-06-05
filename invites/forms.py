from django import forms
from invites.decorators import create_invite_code
from users.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class InviteUserForm(forms.Form):
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Message", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.inviter = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User already exists")
        return email

    def save(self):
        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]

        context = {
            "message": message,
            "invite_link": f"https://roboco.dev/register/?invite={create_invite_code(self.inviter)}",
            "inviter": self.inviter,
        }

        html_message = render_to_string("invites/email_body.html", context)
        plain_message = strip_tags(html_message)

        send_mail(
            "Invitation to join",
            plain_message,
            "robocosa@roboco.dev",
            [email],
            fail_silently=False,
            html_message=html_message,
        )
