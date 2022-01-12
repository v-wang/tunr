from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  # Log in and log out
  path('accounts/login/',
    auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
  path('accounts/logout/',
    auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
  # Sign up
  path('accounts/signup', views.sign_up, name="signup")

]