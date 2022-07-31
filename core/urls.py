from django.urls import path
from core.views import dashboard, main


# SECTION Main views
urlpatterns = [
    path("", main.homepage, name="homepage"),
    path("operators/<str:association>/", main.operator_list_page, name="operator_list"),
    # path("businesses/", main.business_list_page, name="business_list"),
    # path("businesses/<int:pk>/", main.one_business, name="business_detail"),
    path("login/", main.login_page, name="login_page"),
    path("logout/", main.logout_page, name="logout_page"),
    path("boat/<int:pk>/", main.one_boat_page, name="one_boat"),
]
# !SECTION


# SECTION Dashboard Views

# SECTION Businesses vIEWS

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

# !SECTION


# SECTION Boats
urlpatterns += [
    path(
        "dashboard/boats/",
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
        "dashboard/boats/<int:pk>/delete/",
        dashboard.delete_boat,
        name="dashboard_boat_delete",
    ),
    path(
        "dashboard/boats/<int:pk>/update/",
        dashboard.BoatUpdateView.as_view(),
        name="dashboard_boat_update",
    ),
]

# !SECTION

# SECTION Reviews
urlpatterns += [
    path(
        "dashboard/reviews/",
        dashboard.ReviewListView.as_view(),
        name="dashboard_review_list",
    ),
    path(
        "dashboard/reviews/add/",
        dashboard.ReviewCreateView.as_view(),
        name="dashboard_review_add",
    ),
    path(
        "dashboard/reviews/<int:pk>/",
        dashboard.ReviewDetailView.as_view(),
        name="dashboard_review_detail",
    ),
    path(
        "dashboard/reviews/<int:pk>/delete/",
        dashboard.delete_review,
        name="dashboard_review_delete",
    ),
    path(
        "dashboard/reviews/<int:pk>/update/",
        dashboard.ReviewUpdateView.as_view(),
        name="dashboard_review_update",
    ),
]

# !SECTION


# SECTION Change Password

urlpatterns += [
    path("dashboard/settings/", dashboard.change_password, name="dashboard_settings")
]

# !SECTION
# !SECTION
