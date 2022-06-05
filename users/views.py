from django.shortcuts import redirect, render
from invites.decorators import create_invite_code, invite_required
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


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

            return redirect("login")
    else:
        form = UserRegisterForm(email=email)
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "users/profile.html")
