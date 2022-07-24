from django.contrib import admin
from django.urls import path, include
from core.views import main, owner_dashboard, admin_dashboard


# Main Views
urlpatterns = [
    path("", main.homepage, name="homepage"),
    path("login/", main.login_page, name="login_page"),
    path("boat/", main.one_boat_page, name="one_boat"),
]


# Dashboard Views
## ! Businesses
urlpatterns += [
    path(
        "dashboard/businesses",
        admin_dashboard.BusinessListView.as_view(),
        name="dashboard_business_list",
    ),
    path(
        "dashboard/businesses/add",
        admin_dashboard.BusinessCreateView.as_view(),
        name="dashboard_business_add",
    ),
    path(
        "dashboard/businesses/update/<int:pk>/",
        admin_dashboard.BusinessUpdateView.as_view(),
        name="dashboard_business_update",
    ),
    path(
        "dashboard/businesses/<int:pk>/delete",
        admin_dashboard.delete_business,
        name="dashboard_business_delete",
    ),
    path(
        "dashboard/businesses/<int:pk>",
        admin_dashboard.BusinessDetailView.as_view(),
        name="dashboard_business_detail",
    ),
]


# ! Boats
urlpatterns += [
    path(
        "dashboard/boats",
        admin_dashboard.BoatListView.as_view(),
        name="dashboard_boat_list",
    ),
    path(
        "dashboard/boats/add/",
        admin_dashboard.BoatCreateView.as_view(),
        name="dashboard_boat_add",
    ),
    path(
        "dashboard/boats/<int:pk>/",
        admin_dashboard.BoatDetailView.as_view(),
        name="dashboard_boat_detail",
    ),
    path(
        "dashboard/boats/<int:pk>/delete",
        admin_dashboard.delete_business,
        name="dashboard_boat_delete",
    ),
]


# Admin Dashboard Views
# NOTE The url is '/appadmin so as not to conflict with Django's default '/admin'
urlpatterns += [
    path("appadmin/", admin_dashboard.dashboard, name="admin_dashboard"),
    path("appadmin/boats/", admin_dashboard.all_boats, name="admin_all_boats"),
    path("appadmin/boats/add", admin_dashboard.add_boat, name="admin_add_boat"),
    path("appadmin/reviews/", admin_dashboard.all_reviews, name="admin_all_reviews"),
]
