from re import sub
from django.contrib import admin
from .models import Page

# Configuraciones extra para el panel
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content') # activa un buscador
    list_filter = ('visible',) # Crea menú lateral con un filtro
    list_display = ('title', 'visible',  'created_at') # Agrega más detalles en listados de articulos
    ordering = ('-created_at',) # Orden de la lista por defecto

# Register your models here.
admin.site.register(Page, PageAdmin)

# Configuración del Panel
subtitle = "Panel de Gestión"
title = "Blog Jota Contreras"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle

