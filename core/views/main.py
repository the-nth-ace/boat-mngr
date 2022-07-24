import imp
from django.shortcuts import get_list_or_404, get_object_or_404, render
from core.services import get_user_by_username
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from core.models import Boat, Business, Review


# TODO

## Homepage
def homepage(request):
    return render(request, "customer/home.html")


## One Boat Page


def one_boat_page(request, pk):
    boat = get_object_or_404(Boat, pk=pk)
    reviews = Review.objects.filter(boat=boat)
    context = {"boat": boat, "reviews": reviews}
    return render(request, "customer/boat_detail.html", context)


def business_list_page(request):
    businesses = Business.objects.all()
    context = {"businesses": businesses}
    return render(request, "customer/business_list.html", context)


def one_business(request, pk):
    business = get_object_or_404(Business, pk=pk)
    boats = get_list_or_404(Boat, business=business)
    context = {"business": business, "boats": boats}
    return render(request, "customer/business_detail.html", context)


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
