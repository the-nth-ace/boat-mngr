import imp
from django.shortcuts import render
from core.services import get_user_by_username
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


# TODO

## Homepage
def homepage(request):
    return render(request, "main/home.html")


## One Boat Page


def one_boat_page(request):
    return render(request, "main/one_boat.html")


## Login Page


def login_page(request):
    if request.method == "POST":
        username: str = request.POST["username"]
        password: str = request.POST["password"]
        user: User | None = authenticate(username=username, password=password)
        # Todo
        if user is not None:
            login(request, user)
            if user.is_staff:
                print("Redirect to admin")
            else:
                print("Redirect to owner dashboard")
        else:
            print("Error occurred!")

        # Authenticate user here

    return render(request, "main/login.html")
