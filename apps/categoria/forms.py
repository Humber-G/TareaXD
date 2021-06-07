from django import forms
from django.forms import fields
from .models import Categoria


class CategoriaFormulario(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoriaFormulario, self).__init__(*args, **kwargs)

        for campoVisible in self.visible_fields():
            campoVisible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Categoria
        fields = '__all__'
