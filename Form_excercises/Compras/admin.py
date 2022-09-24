from re import A
from django.contrib import admin
from .models import Compras

# Para agregar información de otros atributos del objeto
# en el Panel de administración:

class ComprasAdmin(admin.ModelAdmin):
    readonly_fields = ('purshased_date',)

# Registro de los modelos para que aparezcan en Panel de Administración
admin.site.register(Compras, ComprasAdmin)

# Configurar titulo del Panel
title = "DB and Forms | Jota Contreras"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Gestión Compras"

