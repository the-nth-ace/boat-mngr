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
    path("dashboard/", dashboard.dashboard, name="dashboard"),
    path(
        "dashboard/operators/",
        dashboard.OperatorListView.as_view(),
        name="dashboard_operator_list",
    ),
    path(
        "dashboard/operators/add/",
        dashboard.OperatorCreateView.as_view(),
        name="dashboard_operator_add",
    ),
    path(
        "dashboard/operators/update/<int:pk>/",
        dashboard.OperatorUpdateView.as_view(),
        name="dashboard_operator_update",
    ),
    path(
        "dashboard/operators/<int:pk>/delete/",
        dashboard.delete_operator,
        name="dashboard_operator_delete",
    ),
    path(
        "dashboard/operators/<int:pk>/",
        dashboard.OperatorDetailView.as_view(),
        name="dashboard_operator_detail",
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
        dashboard.delete_boat,
        name="dashboard_boat_delete",
    ),
]

# Reviews View
