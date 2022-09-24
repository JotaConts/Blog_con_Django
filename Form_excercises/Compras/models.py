from tabnanny import verbose
from django.db import models

# Create your models here.

class Compras(models.Model):
    product = models.CharField(max_length=100, verbose_name="Producto")
    price = models.IntegerField(verbose_name="Precio")
    units = models.IntegerField(verbose_name="Cantidad")
    comment = models.TextField(verbose_name="Comentarios")
    purshased = models.BooleanField(default=False, verbose_name="Comprado")
    purshased_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    class Meta:
        #db_table = "nuevo_nombre_de_tabla"
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ['-purshased']

    # Esta función mágica cambia el nombre por defecto de cada compra en el Panel    
    def __str__(self):
        if self.purshased:
            purshase = "Comprado"
        else:
            purshase = "Pendiente"

        return f"{self.product} - {purshase}"


