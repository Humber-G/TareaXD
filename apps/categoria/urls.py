from django.urls import path
from .views import vistaPrincipal, crearCategoria, buscarCategoria, edicionCategoria, modificarCategoria, eliminarCategoria

urlpatterns = [
    path('', vistaPrincipal, name='listarCategoria'),
    path('agregar/', crearCategoria, name='agregarCategoria'),
    path('buscar/<int:idCategoria>', buscarCategoria, name='buscarCategoria'),
    path('editar/<int:idCategoria>', edicionCategoria, name='edicion'),
    path('modificar/<int:idCategoria>', modificarCategoria, name='modificar'),
    path('eliminar/<int:idCategoria>', eliminarCategoria, name='eliminar')
]
