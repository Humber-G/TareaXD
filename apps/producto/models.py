from django.db import models
from apps.categoria.models import Categoria

# LA RELACION ES DESDE PRODUCTO A CATEGORIA, OSEA QUE AL INGRESAR UN PRODUCTO VA A PEDIR EL ID DE CATEGORIA
# Create your models here.


class Producto(models.Model):
    nombre_producto = models.CharField(
        'Nombre del producto', max_length=50, blank=False, null=False)
    precio_producto = models.SmallIntegerField(
        'Precio del producto', blank=False, null=False)
    codigo_barra = models.CharField(
        'Codigo de barra', blank=False, null=False, max_length=150)
    # Uno a Uno
    # on_delete CASCADE = me llevo a todos
    # on_delete RESTRICT = Protege el borrado si hay relaciones usadas
    # on_delete SET NULL = TODOS LOS PRODUCTOS PASAN A NULL
    # on_delete set_default = VA ATOMAR EL VALOR POR DEFECTO DE LA RELACION

    #categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE)
    # UNO A MUCHOS
    categoria_uno_muchos = models.ForeignKey(
        Categoria, on_delete=models.CASCADE)
    # MUCHOS A MUCHOS
    #categoria_muchos_muchos = models.ManyToManyField(Categoria)
