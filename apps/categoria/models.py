from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre_categoria = models.CharField(
        'Nombre Categoria', max_length=50, blank=False, null=False)
    descripcion_categoria = models.TextField(
        'Descripción Categoria', max_length=150)
