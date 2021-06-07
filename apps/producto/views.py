from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoFormulario  # CREAR ARCHIVO FORMS

from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def vistaPrincipal(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'producto/listarProductos.html', context)


def crearProducto(request):
    formulario = ProductoFormulario()
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarProducto')
    context = {
        "formulario": formulario
    }
    return render(request, 'producto/agregarProducto.html', context)


def buscarProducto(request, idProducto):
    productoEncontrado = None
    try:
        productoEncontrado = Producto.objects.get(pk=idProducto)
    except ObjectDoesNotExist:
        pass
    context = {
        "productoEncontrado": productoEncontrado
    }
    return render(request, '', context)


def edicionProducto(request, idProducto):
    productoEncontrado = None
    try:
        productoEncontrado = Producto.objects.get(pk=idProducto)
    except ObjectDoesNotExist:
        pass
    formularioProducto = ProductoFormulario(instance=productoEncontrado)
    context = {
        'formulario': formularioProducto,
        'producto': productoEncontrado
    }
    return render(request, '', context)


def modificarProducto(request, idProducto):
    if request.method == 'POST':
        productoEncontrado = None
        try:
            productoEncontrado = Producto.objects.get(pk=idProducto)
        except ObjectDoesNotExist:
            pass
        formulario = ProductoFormulario(
            request.POST, instance=productoEncontrado)
        if(formulario.is_valid()):
            formulario.save()
            return redirect('listarProducto')


def eliminarProducto(request, idProducto):
    productoEncontrado = None
    try:
        productoEncontrado = Producto.objects.get(pk=idProducto)
        productoEncontrado.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('listarProducto')
