from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("about", views.about, name="about"),
    path("contest", views.contest, name="contest"),
    path("contest/<str:slug>", views.singleContest, name="contest-deatil"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("login", views.login, name="register"),
]
