from django.contrib import admin
from .models import Article, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # Para mostrar otros datos en el panel de admin > articulo
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configurar el titulo del panel de administración
site_title = "Curso de Django | Jota Contreras"
admin.site.site_header = site_title
admin.site.site_title = site_title
admin.site.index_title = "Panel de Gestión"