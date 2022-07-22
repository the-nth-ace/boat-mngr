from django.contrib import admin
from django.urls import path, include
from core.views import main


# Main Views
urlpatterns = [
    path("", main.homepage, name="homepage"),
    path("login/", main.login_page, name="login_page"),
    path("boat/", main.one_boat_page, name="one_boat"),
]


# Owner Dashboard Views


# Admin Dashboard Views
