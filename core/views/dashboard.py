from typing import Any, Dict, Optional
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser, AbstractBaseUser
from core.models import Boat, Operator, Review


def dashboard(request):
    boats_count = Boat.objects.all().count()
    operators_count = Operator.objects.all().count()
    reviews = Review.objects.all()
    reviews_count = reviews.count()
    reviews = reviews[:5]
    context = {
        "boats_count": boats_count,
        "operators_count": operators_count,
        "reviews_count": reviews_count,
        "reviews": reviews,
        "active": "dashboard",
    }
    return render(request, "dashboard/dashboard.html", context)


class OperatorViewSetup(LoginRequiredMixin):
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


@login_required
def delete_operator(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    operator.delete()
    return redirect(reverse("dashboard_operator_list"))


class BoatViewSetup(LoginRequiredMixin):
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
        "captain_certification",
        "captain_photo",
        "deckhand_name",
        "deckhand_photo",
        "operator",
        "niwa_approval_date",
        "laswa_approval_date",
        "certification_status",
    ]
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


class BoatUpdateView(BoatViewSetup, UpdateView):
    fields = [
        "name",
        "capacity",
        "captain_name",
        "captain_certification",
        "captain_photo",
        "deckhand_name",
        "deckhand_photo",
        "operator",
        "niwa_approval_date",
        "laswa_approval_date",
        "certification_status",
    ]
    template_name: str = "dashboard/boat_update_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "boats"
        return context


@login_required
def delete_boat(request, pk):
    boat = get_object_or_404(Boat, pk=pk)
    boat.delete()
    return redirect(reverse("dashboard_boat_list"))


class ReviewViewSetup(LoginRequiredMixin):
    model = Review
    success_url = reverse_lazy("dashboard_review_list")


class ReviewListView(ReviewViewSetup, ListView):
    context_object_name: Optional[str] = "reviews"
    template_name: str = "dashboard/review_list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "reviews"
        return context


class ReviewCreateView(ReviewViewSetup, CreateView):
    fields = ["reviewer_name", "rating", "content", "boat"]
    template_name: str = "dashboard/review_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "reviews"
        return context

    def form_invalid(self, form):
        print(form.errors.as_json())
        return super().form_invalid(form)


class ReviewDetailView(ReviewViewSetup, DetailView):
    context_object_name: Optional[str] = "review"
    template_name: str = "dashboard/review_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "reviews"
        return context


class ReviewUpdateView(ReviewViewSetup, UpdateView):
    fields = ["reviewer_name", "rating", "content", "boat"]
    template_name: str = "dashboard/review_update_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active"] = "reviews"
        return context


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect(reverse("dashboard_view_list"))


# TODO Change Password View


@login_required
def change_password(request):
    user: AbstractBaseUser | AnonymousUser = request.user
    if request.method == "post":
        # Do change
        return redirect(reverse("dashboard_settings"))

    return render(request, "dashboard/change_password.html")
