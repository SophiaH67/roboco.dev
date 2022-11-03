from django.shortcuts import redirect


def logout_required(view_func):
    """
    Check if the user is logged in.
    """

    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("index")
        return view_func(request, *args, **kwargs)

    return wrapper
