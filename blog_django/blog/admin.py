from django.contrib import admin
from .models import Category, Article

class Category_admin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields = ('name', 'description') # activa un buscador
    list_display = ('name', 'created_at') # Agrega más detalles en listados de articulos


class Article_admin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated_at')
    # Para acceder a datos de tablas relacionadas usaremos doble guión bajo:
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display = ('title', 'user', 'public', 'created_at')
    list_filter = ('public', 'user', 'categories__name')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

# Register your models here.
admin.site.register(Category, Category_admin)
admin.site.register(Article, Article_admin)
