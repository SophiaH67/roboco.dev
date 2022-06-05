from typing import Union
from django.shortcuts import redirect, render
from django.core.signing import Signer
import base64
import time

from users.models import User


def invite_required(view_func):
    """
    Check if the ?invite=<invite_code> is in the URL and if so, check if that invite code is valid.
    """

    def wrapper(request, *args, **kwargs):
        invite_code = request.GET.get("invite")
        if is_invite_code_valid(invite_code)[0]:
            return view_func(request, *args, **kwargs)
        return render(request, "invites/invite_required.html", status=401)

    return wrapper


def minimum_invites_left(view_func):
    """
    Check if the user has invites left.
    """

    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.invites_left <= 0:
            return redirect("profile")
        return view_func(request, *args, **kwargs)

    return wrapper


def is_invite_code_valid(invite_code: str | None) -> Union[bool, str]:
    """
    Check if the invite code is valid.
    """
    if invite_code is None:
        return False, "No invite code provided."
    invite_code = base64.b64decode(invite_code)
    invite_code = invite_code.decode("utf-8")
    signer = Signer()
    invite_code = signer.unsign(invite_code)
    # Format is "user_id:expires_at"
    invite_code = invite_code.split(":")
    if len(invite_code) != 2:
        return False, "Split failed"
    try:
        user_id = int(invite_code[0])
        expires_at = int(invite_code[1])
    except ValueError:
        return False, "Conversion error"
    if expires_at < int(time.time()):
        return False, "Expired"
    # Check if the user exists
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return False, "User does not exist"
    # Check if the user has invites left
    if user.invites_left <= 0:
        return False, "No invites left"
    return True, user


def create_invite_code(user: User) -> str:
    """
    Create an invite code for the user.
    """
    signer = Signer()
    invite_code = f"{user.id}:{int(time.time()) + 60 * 60 * 24 * 7}"  # 7 days
    invite_code = signer.sign(invite_code)
    invite_code = base64.b64encode(invite_code.encode("utf-8"))
    invite_code = invite_code.decode("utf-8")
    return invite_code
