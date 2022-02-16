from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('' , views.loginfn , name = "login"),
    path('registration' , views.register , name = "registration"),
    path('validation' , views.validation),
    path('login_redirect' , views.loginre),
    path('logout' , views.logoutfn),
]