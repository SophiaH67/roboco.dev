from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return render(request, "users/register.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(request, "users/register.html", {"form": form})


# def login(request):
#     if request.method == "POST":
