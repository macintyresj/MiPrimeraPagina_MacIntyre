from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
    path('ver_pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('realizar_pedido/<int:producto_id>/',
         views.realizar_pedido,
         name='realizar_pedido'),
]
