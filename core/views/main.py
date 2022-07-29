
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.models import Boat, Operator, Review


def homepage(request):
    return render(request, "customer/home.html")




def one_boat_page(request, pk):
    boat = get_object_or_404(Boat, pk=pk)
    reviews = Review.objects.filter(boat=boat)
    context = {"boat": boat, "reviews": reviews}
    return render(request, "customer/boat_detail.html", context)


def business_list_page(request):
    operatores = Operator.objects.all()
    context = {"businesses": operatores}
    return render(request, "customer/Operator_list.html", context)


def one_business(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    boats = Boat.objects.filter(operator=Operator)
    context = {"business": Operator, "boats": boats}
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
