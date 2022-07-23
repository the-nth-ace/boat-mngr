from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from core.services import is_admin_test

# Create your views here.

# TODO Login for everybody


# TODO Dashboard for admin


@user_passes_test(is_admin_test)
def dashboard(request):
    return render(request, "admin/dashboard.html")


#
