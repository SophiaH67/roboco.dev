from django.shortcuts import redirect, render
from users.forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


# def login(request):
#     if request.method == "POST":
