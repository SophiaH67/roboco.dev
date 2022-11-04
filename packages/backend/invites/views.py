from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from invites.decorators import minimum_invites_left

from invites.forms import InviteUserForm


@login_required
@minimum_invites_left
def invite_user(request):
    if request.method == "POST":
        form = InviteUserForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = InviteUserForm(user=request.user)
    return render(request, "invites/invite_user.html", {"form": form})
