from django.urls import path
from . import views

urlpatterns = [
    path('lista-compras/', views.lista_compras, name='lista_compras'),
]
