from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return redirect('mensajes:inbox')
    else:
        form = MensajeForm()
    return render(request, 'mensajes_app/enviar_mensaje.html', {'form': form})

@login_required
def inbox(request):
    mensajes_recibidos = Mensaje.objects.filter(receptor=request.user).order_by('-creado_en')
    return render(request, 'mensajes_app/inbox.html', {'mensajes_recibidos': mensajes_recibidos})