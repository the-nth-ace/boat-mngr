from typing import Any, Dict, Optional
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from core.forms import BoatForm
from core.models import Boat, Operator

from core.services import is_admin_test


def dashboard(request):
    return render(request, "dashboard/dashboard.html", context={"active": "dashboard"})

# FIXME 
# @user_passes_test(is_admin_test)
# def all_reviews(request):
#     return render(request, "dashboard/all_reviews.html", context={"active": "reviews"})



class OperatorViewSetup:
    model = Operator
    success_url = reverse_lazy("dashboard_operator_list")


class OperatorListView(OperatorViewSetup, ListView):
    context_object_name: Optional[str] = "operators"
    template_name: str = "dashboard/operator_list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "operators"
        return context


class OperatorCreateView(OperatorViewSetup, CreateView):
    fields = ["name", "contact_info", "operation_commenced", "association"] 
    template_name: str = "dashboard/operator_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "operators"
        return context


class OperatorUpdateView(OperatorViewSetup, UpdateView):
    fields = ["name", "contact_info", "operation_commenced", "association"] 
    template_name: str = "dashboard/operator_update_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "operators"
        return context


class OperatorDetailView(OperatorViewSetup, DetailView):
    context_object_name: Optional[str] = "operator"
    template_name: str = "dashboard/operator_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "operators"
        return context


def delete_operator(request, pk):
    Operator = get_object_or_404(Operator, pk=pk)
    Operator.delete()
    return redirect(reverse("dashboard_operator_list"))


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
    fields = ["name", "capacity", "captain_name", "captain_certification", "captain_photo", "deckhand_name", 
    "deckhand_photo", "operator", "niwa_approval_date", "laswa_approval_date", "certification_status"]
    template_name: str = "dashboard/boat_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "boats"
        return context

    def form_invalid(self, form):
        print(form.errors.as_json())
        return super().form_invalid(form)


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
        "Operator",
    ]

    template_name: str = "dashboard/boat_update_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "boats"
        return context

def delete_boat(request, pk):
    boat = get_object_or_404(Boat, pk=pk)
    boat.delete()
    return redirect(reverse("dashboard_boat_list"))
