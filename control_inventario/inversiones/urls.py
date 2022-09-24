from django.urls import path
from . import views

urlpatterns = [
    path('proyectos-inversion', views.proyectos_inversion, name='proyectos_inversion'),
]
