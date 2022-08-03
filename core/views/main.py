from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse
from core.models import Boat, Operator, Review


def homepage(request):
    return render(request, "customer/index.html")


def one_boat_page(request, pk):
    boat = get_object_or_404(Boat, pk=pk)
    if request.method == "POST":
        content = request.POST.get("content")
        review = Review.objects.create(content=content, boat=boat)
        review.save()
        return redirect(reverse("one_boat", kwargs={"pk": boat.pk}))

    reviews = Review.objects.filter(boat=boat)
    context = {"boat": boat, "reviews": reviews}
    return render(request, "customer/boat_detail.html", context)


def operator_list_page(request, association):
    associations = {
        "atbowaton": {
            "acronym": "ATBOWATON",
            "name": "THE ASSOCIATION OF TOURIST BOAT OPERATORS AND WATER TRANSPORTERS OF NIGERIA",
            "model": "atbo",
        },
        "ufta": {
            "acronym": "UFTA",
            "name": "UNITED FERRY TRANSPORTERS' ASSOCIATION",
            "model": "ufta",
        },
        "iboa": {
            "acronym": "IBOA",
            "name": "INTEGRATED BOAT OPERATORS ASSOCIATION",
            "model": "iboa",
        },
    }
    association_desc = associations[association]
    name = association_desc["name"]
    acronym = association_desc["acronym"]
    operators = Operator.objects.filter(association=association_desc["model"])
    context = {"operators": operators, "name": name, "acronym": acronym}
    return render(request, "customer/operator_list.html", context)


def operator_detail(request, pk):
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
