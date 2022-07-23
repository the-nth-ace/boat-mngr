from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from core.services import is_owner_test


@user_passes_test(is_owner_test)
def dashboard(request):
    return render(request, "owner/dashboard.html")



