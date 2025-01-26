# from django import forms
# from .models import Producto, Usuario, Orden

# class ProductoForm(forms.ModelForm):
#     class Meta:
#         model = Producto
#         fields = ['titulo', 'descripcion', 'talle', 'color', 'precio']

# class UsuarioForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['nombre', 'email']

# class OrdenForm(forms.ModelForm):
#     class Meta:
#         model = Orden
#         fields = ['usuario', 'producto']

from django import forms
from .models import Producto, Usuario, Orden, Page

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

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content']
