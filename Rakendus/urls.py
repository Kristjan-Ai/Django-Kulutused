from django.urls import path
from . import views

urlpatterns = [
    path("praegu/", views.praegu, name="praegu"),  
    path("sisestus/", views.sisestus, name="sisestus"),
    path("tegele/", views.tegele, name="tegele"),
    path("avaleht/", views.index, name="index"),
    path("", views.login_form, name="login_form"),
    path("login/", views.login_, name="login_"),
    path("logout/", views.logout_, name="logout_"),
]