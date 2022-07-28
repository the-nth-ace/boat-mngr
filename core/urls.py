from django.urls import path
from core.views import dashboard, main


# Main Views
urlpatterns = [
    path("", main.homepage, name="homepage"),
    path("businesses", main.business_list_page, name="business_list"),
    path("businesses/<int:pk>/", main.one_business, name="business_detail"),
    path("login/", main.login_page, name="login_page"),
    path("boat/<int:pk>/", main.one_boat_page, name="one_boat"),
]


# Dashboard Views
## ! Businesses
urlpatterns += [
    path("dashboard/", main.dashboard, name="dashboard"),
    path(
        "dashboard/businesses",
        dashboard.BusinessListView.as_view(),
        name="dashboard_business_list",
    ),
    path(
        "dashboard/businesses/add",
        dashboard.BusinessCreateView.as_view(),
        name="dashboard_business_add",
    ),
    path(
        "dashboard/businesses/update/<int:pk>/",
        dashboard.BusinessUpdateView.as_view(),
        name="dashboard_business_update",
    ),
    path(
        "dashboard/businesses/<int:pk>/delete",
        dashboard.delete_business,
        name="dashboard_business_delete",
    ),
    path(
        "dashboard/businesses/<int:pk>",
        dashboard.BusinessDetailView.as_view(),
        name="dashboard_business_detail",
    ),
]


# ! Boats
urlpatterns += [
    path(
        "dashboard/boats",
        dashboard.BoatListView.as_view(),
        name="dashboard_boat_list",
    ),
    path(
        "dashboard/boats/add/",
        dashboard.BoatCreateView.as_view(),
        name="dashboard_boat_add",
    ),
    path(
        "dashboard/boats/<int:pk>/",
        dashboard.BoatDetailView.as_view(),
        name="dashboard_boat_detail",
    ),
    path(
        "dashboard/boats/<int:pk>/delete",
        dashboard.delete_business,
        name="dashboard_boat_delete",
    ),
]


# Admin Dashboard Views
# FIXME The url is '/appadmin so as not to conflict with Django's default '/admin'
urlpatterns += [
    path("appadmin/reviews/", dashboard.all_reviews, name="admin_all_reviews"),
]
