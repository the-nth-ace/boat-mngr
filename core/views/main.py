from django.shortcuts import render


# TODO

## Homepage
def homepage(request):
    return render(request, "main/index.html")


## One Boat Page


def one_boat_page(request):
    return render(request, "main/one_boat.html")


## Login Page


def login_page(request):
    return render(request, "main/login.html")
