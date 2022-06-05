from django.shortcuts import render


def invite_required(view_func):
    """
    Check if the ?invite=<invite_code> is in the URL and if so, check if that invite code is valid.
    """

    def wrapper(request, *args, **kwargs):
        invite_code = request.GET.get("invite")
        if invite_code:
            if invite_code == "roboco":
                return view_func(request, *args, **kwargs)
        return render(request, "invites/invite_required.html", status=401)

    return wrapper
