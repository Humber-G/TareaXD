from django import forms
from django.forms import fields
from .models import Producto


class ProductoFormulario(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductoFormulario, self).__init__(*args, **kwargs)

        for campoVisible in self.visible_fields():
            campoVisible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Producto
        fields = '__all__'
