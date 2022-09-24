from tabnanny import verbose
from django.db import models

# VAMOS A CREAR EL MODELO DE DATOS PARA UN BLOG:
# 1) Creamos los modelos Article y Category
# 2) Una vez terminados los modelos en la terminal confirmamos los cambios:
#       - python manage.py makemigrations (para preparar las modificaciones)
#       - python manage.py sqlmigrate (para ver el codigo sql que se genera)
#       - python manage.py migrate (para confirmar definitivamente las modificaciones en la db)

# CLASE META EN DJANGO (meta class)
#       - Permite configurar metadatos de los modelos


# Creamos una clase para los modelos articulo categoría.
# Y heredamos models.Modell desde la librería django.db

class Article(models.Model):
    # definimos los datos que contendrá cada articulo:
    title = models.CharField(max_length=100, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    public = models.BooleanField(verbose_name="Público")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado") 
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['created_at']

    def __str__(self):
        if self.public == True:
            public = "(Publicado)"
        else:
            public = "(Privado)"

        return f"{self.title} {public}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateField()

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
