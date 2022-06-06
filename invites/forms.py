from django import forms
from invites.lib import send_invite_email
from users.models import User


class InviteUserForm(forms.Form):
    email = forms.EmailField(label="Email")

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
        send_invite_email(self.inviter, email)
