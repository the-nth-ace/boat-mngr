
from typing import Any, Dict, Optional
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from core.forms import BoatForm
from core.models import Boat, Business

from core.services import is_admin_test

# Create your views here.

# TODO Login for everybody


# TODO Dashboard for admin


@user_passes_test(is_admin_test)
def dashboard(request):

    return render(request, "dashboard/dashboard.html", context={"active": "dashboard"})


@user_passes_test(is_admin_test)
def all_boats(request):
    return render(request, "dashboard/all_boats.html", context={"active": "boats"})


@user_passes_test(is_admin_test)
def add_boat(request):
    return render(request, "dashboard/boat_form.html", context={"active": "boats"})


@user_passes_test(is_admin_test)
def all_reviews(request):
    return render(request, "dashboard/all_reviews.html", context={"active": "reviews"})


# * Business Views


class BusinessViewSetup:
    model = Business
    success_url = reverse_lazy("dashboard_business_list")


class BusinessListView(BusinessViewSetup, ListView):
    context_object_name: Optional[str] = "businesses"
    template_name: str = "dashboard/business_list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "businesses"
        return context


class BusinessCreateView(BusinessViewSetup, CreateView):
    fields = ["name", "owner", "operation_commenced"]
    template_name: str = "dashboard/business_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "businesses"
        return context


class BusinessUpdateView(BusinessViewSetup, UpdateView):
    fields = ["name", "owner", "operation_commenced"]
    template_name: str = "dashboard/business_update_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "businesses"
        return context


class BusinessDetailView(BusinessViewSetup, DetailView):
    context_object_name: Optional[str] = "business"
    template_name: str = "dashboard/business_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "businesses"
        return context


def delete_business(request, pk):
    business = get_object_or_404(Business, pk=pk)
    business.delete()
    return redirect(reverse("dashboard_business_list"))


class BoatViewSetup:
    model = Boat
    success_url = reverse_lazy("dashboard_boat_list")


class BoatListView(BoatViewSetup, ListView):
    context_object_name: Optional[str] = "boats"
    template_name: str = "dashboard/boat_list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "boats"
        return context


class BoatCreateView(BoatViewSetup, CreateView):
    fields = [
        "name",
        "capacity",
        "captain_name",
        "captain_photo",
        "deckhand",
        "business",
    ]
    template_name: str = "dashboard/boat_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "boats"
        return context


class BoatDetailView(BoatViewSetup, DetailView):
    context_object_name: Optional[str] = "boat"
    template_name: str = "dashboard/boat_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "boats"
        return context


# FIXME fix form
class BoatUpdateView(BoatViewSetup, UpdateView):
    fields = [
        "name",
        "capacity",
        "captain_name",
        "captain_photo",
        "deckhand",
        "business",
    ]

    template_name: str = "dashboard/boat_update_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "businesses"
        return context


def delete_business(request, pk):
    boat = get_object_or_404(Boat, pk=pk)
    boat.delete()
    return redirect(reverse("dashboard_boat_list"))
