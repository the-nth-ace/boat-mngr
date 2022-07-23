from django.contrib import admin
from django.urls import path, include
from core.views import main, owner_dashboard, admin_dashboard


# Main Views
urlpatterns = [
    path("", main.homepage, name="homepage"),
    path("login/", main.login_page, name="login_page"),
    path("boat/", main.one_boat_page, name="one_boat"),
]


# Owner Dashboard Views
urlpatterns += [path("owner/", owner_dashboard.dashboard, name="owner_dashboard")]

# Admin Dashboard Views
# NOTE The url is '/appadmin so as not to conflict with Django's default '/admin'
urlpatterns += [
    path("appadmin/", admin_dashboard.dashboard, name="admin_dashboard"),
    path(
        "appadmin/businesses/",
        admin_dashboard.all_businesses,
        name="admin_all_businesses",
    ),
    path(
        "appadmin/businesses/add",
        admin_dashboard.add_businesses,
        name="admin_add_business",
    ),
    path("appadmin/boats/", admin_dashboard.all_boats, name="admin_all_boats"),
    path("appadmin/boats/add", admin_dashboard.add_boat, name="admin_add_boat"),
    path("appadmin/reviews/", admin_dashboard.all_reviews, name="admin_all_reviews"),
]
