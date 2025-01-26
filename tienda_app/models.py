# from django.db import models


# class Producto(models.Model):
#   titulo = models.CharField(max_length=100)
#   descripcion = models.TextField()
#   talle = models.CharField(max_length=10)
#   color = models.CharField(max_length=20)
#   precio = models.DecimalField(max_digits=10, decimal_places=2)

#   def __str__(self):
#     return self.titulo


# class Usuario(models.Model):
#   nombre = models.CharField(max_length=100)
#   email = models.EmailField()

#   def __str__(self):
#     return self.nombre


# class Orden(models.Model):
#   usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#   producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#   fecha = models.DateTimeField(auto_now_add=True)

#   def __str__(self):
#     return f"Orden de {self.usuario.nombre} - {self.producto.titulo}"
from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    talle = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Orden(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden de {self.usuario.nombre} - {self.producto.titulo}"


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
