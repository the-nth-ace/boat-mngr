from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from core.services import is_admin_test

# Create your views here.

# TODO Login for everybody


# TODO Dashboard for admin


@user_passes_test(is_admin_test)
def dashboard(request):

    return render(request, "admin/dashboard.html", context={"active": "dashboard"})


@user_passes_test(is_admin_test)
def all_owners(request):
    return render(request, "admin/all_owners.html", context={"active": "businesses"})


@user_passes_test(is_admin_test)
def all_boats(request):
    return render(request, "admin/all_boats.html", context={"active": "boats"})


@user_passes_test(is_admin_test)
def all_reviews(request):
    return render(request, "admin/all_reviews.html", context={"active": "reviews"})
