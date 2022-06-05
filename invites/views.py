from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    # res = send_mail(
    #     "Subject here",
    #     "Here is the message.",
    #     "robocosa@roboco.dev",
    #     ["marnixmeow@gmail.com"],
    #     fail_silently=False,
    # )
    # print(f"res: {res}")
    return render(request, "users/profile.html")
