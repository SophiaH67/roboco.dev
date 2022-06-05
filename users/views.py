from django.shortcuts import redirect, render
from invites.decorators import create_invite_code, invite_required
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


@invite_required
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    context = {
        "invite_code": create_invite_code(request.user),
    }
    return render(request, "users/profile.html")
