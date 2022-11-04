from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, email=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default value for email
        self.fields["email"].initial = email
        self.fields["email"].widget.attrs["readonly"] = True

    def clean_email(self):
        email = self.cleaned_data["email"]
        # Make sure email is the same as the one passed in
        if email != self.fields["email"].initial:
            raise forms.ValidationError("Email must be the same as invite")
        return email

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
