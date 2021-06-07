from django.urls import path
from .views import vistaPrincipal, crearProducto, buscarProducto, edicionProducto, modificarProducto, eliminarProducto

urlpatterns = [
    path('', vistaPrincipal, name='listarProducto'),
    path('agregar/', crearProducto, name='agregarProducto'),
    path('buscar/<int:idProducto>', buscarProducto, name='buscarProducto'),
    path('editar/<int:idProducto>', edicionProducto, name='edicion'),
    path('modificar/<int:idProducto>', modificarProducto, name='modificar'),
    path('eliminar/<int:idProducto>', eliminarProducto, name='eliminar')
]
