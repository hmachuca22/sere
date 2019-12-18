from django.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views

from generales.views import Home
from generales.views import Home_user
from generales.views import HomeSinPrivilegios

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('home_user/', Home_user.as_view(template_name='generales/home_user.html'), name='home_user'),
    path('login/', auth_views.LoginView.as_view(template_name='generales/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='generales/login.html'), name='logout'),
    path('sin_privilegios/', HomeSinPrivilegios.as_view(), name='sin_privilegios'),
]
