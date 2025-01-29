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
        fields = ['title', 'content', 'imagen'] 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        
        }

        