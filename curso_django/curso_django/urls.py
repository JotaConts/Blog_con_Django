"""curso_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mi_app.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mi_app.views.index),
    path('index/', mi_app.views.index, name="index"),
    path('saludo/', mi_app.views.saludo, name="saludo"),
    path('pagina/', mi_app.views.pagina, name="pagina"),
    path('years/', mi_app.views.years, name="years"), 
    #----------sección menú-----------
    path('intranet/', mi_app.views.intranet, name="intranet"),
    path('info/', mi_app.views.info, name="info"),
    path('contacto/', mi_app.views.contacto, name="contacto"),
    #----------url con 1 y 2 parámetros----------
    # configuramos para la misma view 3 formatos: sin parámetros, con 1 y con 2:
    path('agenda/', mi_app.views.agenda, name="agenda"),
    path('agenda/<str:nombre>', mi_app.views.agenda, name="agenda"),
    path('agenda/<str:nombre>/<str:apellido>', mi_app.views.agenda, name="agenda"),
    #----------url conectados con template----------
    path('index_2/', mi_app.views.index_2, name="index_2"),
    path('saludo_2/', mi_app.views.saludo_2, name="saludo_2"),
    path('pagina_2/', mi_app.views.pagina_2, name="pagina_2"),
    path('years_2/', mi_app.views.years_2, name="years_2"),
    #----------url conectados con template----------
    path('crear-articulo/<str:title>/<str:content>/<str:public>/', mi_app.views.crear_articulo, name="crear_articulo"),
    path('buscar-articulo/', mi_app.views.buscar_articulo, name='buscar_articulo'),
    path('editar-articulo/<int:id>/', mi_app.views.editar_articulo, name='editar_articulo'),
    path('mis-articulos/', mi_app.views.mis_articulos, name='mis_articulos'),
    path('borrar-articulo/<int:id>/', mi_app.views.borrar_articulo, name='borrar'),
    path('nuevo-articulo/', mi_app.views.nuevo_articulo, name='nuevo_articulo'),
    path('guardar-articulo/', mi_app.views.guardar_articulo, name='guardar_articulo'),
    path('nuevo-objeto-articulo/', mi_app.views.nuevo_objeto_articulo, name='nuevo_objeto_articulo')
]

