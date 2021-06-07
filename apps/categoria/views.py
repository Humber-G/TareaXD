from django.shortcuts import render, redirect
from .forms import CategoriaFormulario  # CREAR ARCHIVO FORMS
from .models import Categoria

from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def vistaPrincipal(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'categoria/listarCategorias.html', context)


def crearCategoria(request):
    formulario = CategoriaFormulario()
    if request.method == 'POST':
        formulario = CategoriaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarCategoria')
    context = {
        "formulario": formulario
    }
    return render(request, 'categoria/agregarCategoria.html', context)


def buscarCategoria(request, idCategoria):
    categoriaEncontrada = None
    try:
        categoriaEncontrada = Categoria.objects.get(pk=idCategoria)
    except ObjectDoesNotExist:
        pass
    context = {
        "categoriaEncontrada": categoriaEncontrada
    }
    return render(request, '', context)


def edicionCategoria(request, idCategoria):
    categoriaEncontrada = None
    try:
        categoriaEncontrada = Categoria.objects.get(pk=idCategoria)
    except ObjectDoesNotExist:
        pass
    formularioCategoria = CategoriaFormulario(instance=categoriaEncontrada)
    context = {
        'formulario': formularioCategoria,
        'categoria': categoriaEncontrada
    }
    return render(request, '', context)


def modificarCategoria(request, idCategoria):
    if request.method == 'POST':
        categoriaEncontrada = None
        try:
            categoriaEncontrada = Categoria.objects.get(pk=idCategoria)
        except ObjectDoesNotExist:
            pass
        formulario = CategoriaFormulario(
            request.POST, instance=categoriaEncontrada)
        if(formulario.is_valid()):
            formulario.save()
            return redirect('listarCategoria')


def eliminarCategoria(request, idCategoria):
    categoriaEncontrada = None
    try:
        categoriaEncontrada = Categoria.objects.get(pk=idCategoria)
        categoriaEncontrada.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('listarCategoria')
