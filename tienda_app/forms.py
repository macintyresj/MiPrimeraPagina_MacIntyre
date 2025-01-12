from django import forms
from .models import Producto, Usuario, Orden

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo', 'descripcion', 'talle', 'color', 'precio']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email']

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['usuario', 'producto']