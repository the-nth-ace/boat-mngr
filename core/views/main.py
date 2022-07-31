from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse
from core.models import Boat, Operator, Review


def homepage(request):
    return render(request, "customer/index.html")


def one_boat_page(request, pk):
    boat = get_object_or_404(Boat, pk=pk)
    reviews = Review.objects.filter(boat=boat)
    context = {"boat": boat, "reviews": reviews}
    return render(request, "customer/boat_detail.html", context)


def operator_list_page(request, association):
    associations = {
        "atbowaton": Operator.AssociationChoices.ATBOWATON,
        "ufta": Operator.AssociationChoices.UFTA,
        "iboa": Operator.AssociationChoices.IBOA,
    }
    association_filter = associations[association]
    operators = Operator.objects.filter(association=association_filter)
    context = {"operators": operators, "association": association_filter.name}
    return render(request, "customer/operator_list.html", context)


def one_operator(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    boats = Boat.objects.filter(operator=operator)
    context = {"operator": operator, "boats": boats}
    return render(request, "customer/operator_detail.html", context)


## Login Page


def login_page(request):

    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))

    context = {"error": False}
    if request.method == "POST":
        username: str = request.POST["username"]
        password: str = request.POST["password"]
        user: AbstractBaseUser | None = authenticate(
            username=username, password=password
        )
        if user is not None:
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            context = {"error": True}
            return render(request, "main/login.html", context)

    return render(request, "main/login.html", context)


def logout_page(request):
    logout(request)
    return redirect(reverse("homepage"))
