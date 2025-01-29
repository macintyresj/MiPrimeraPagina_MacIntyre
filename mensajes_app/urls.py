from django.urls import path
from . import views

app_name = 'mensajes'

urlpatterns = [
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('inbox/', views.inbox, name='inbox'),
]