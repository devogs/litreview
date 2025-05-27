# accounts/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), # Built-in LoginView
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # Built-in LogoutView
]