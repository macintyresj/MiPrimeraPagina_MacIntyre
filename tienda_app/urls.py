# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
#     path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
#     path('ver_pedidos/', views.ver_pedidos, name='ver_pedidos'),
#     path('realizar_pedido/<int:producto_id>/',
#          views.realizar_pedido,
#          name='realizar_pedido'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('tienda', views.index, name='index'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
    path('ver_pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('realizar_pedido/<int:producto_id>/', views.realizar_pedido, name='realizar_pedido'),
    
    # Rutas para las páginas
    path('about/', views.about, name='about'),  # Página 'Acerca de'
    path('', views.pages, name='pages'),  # Página principal del blog
    path('pages/<int:pk>/', views.page_detail, name='page_detail'),  # Detalle de una página
    path('pages/create/', views.create_page, name='create_page'),  # Crear página
    path('pages/update/<int:pk>/', views.update_page, name='update_page'),  # Editar página
    path('pages/delete/<int:pk>/', views.delete_page, name='delete_page'),  # Borrar página
    
    # Login, Registro, Logout
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
