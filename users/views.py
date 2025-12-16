from django.shortcuts import redirect, render
from invites.decorators import invite_required
from invites.lib import send_invite_accepted_email, send_user_registered_email
from .decorators import logout_required
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django_otp import devices_for_user

@logout_required
@invite_required
def register(request, inviter=None, email=None):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, email=email)
        if form.is_valid():
            user = form.save()

            user.invited_by = inviter
            user.save()

            inviter.invites_left -= 1
            inviter.save()

            send_invite_accepted_email(user, inviter)
            send_user_registered_email(user)

            return redirect("login")
    else:
        form = UserRegisterForm(email=email)
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "users/profile.html")

@login_required
def profile_security(request):
    otp_devices = devices_for_user(request.user)
    otp_devices_list = list(otp_devices)

    context = {
        'devices': otp_devices_list,
    }
    return render(request, "users/profile/security.html", context)
