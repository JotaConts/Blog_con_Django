from site import venv
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_login_page, name="home"),
    path('index/', views.index_login_page, name="index"),
    path('login/', views.index_login_page, name="login"),
    path('register/', views.register_page, name="register"),
]
