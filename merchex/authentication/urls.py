from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from authentication import views
from django.shortcuts import redirect

urlpatterns = [
    # path('login/', views.login_page, name="login"),
    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('hello/', views.hello),
    path('logout/', views.logout_user, name='logout'),
]
