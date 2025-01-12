from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Usuario, Orden
from .forms import ProductoForm, UsuarioForm, OrdenForm

def index(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(titulo__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request, 'tienda_app/index.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'tienda_app/agregar_producto.html', {'form': form})

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'tienda_app/agregar_usuario.html', {'form': form})

def ver_pedidos(request):
    pedidos = Orden.objects.all()
    return render(request, 'tienda_app/ver_pedidos.html', {'pedidos': pedidos})

def realizar_pedido(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrdenForm(initial={'producto': producto})
    return render(request, 'tienda_app/realizar_pedido.html', {'form': form, 'producto': producto})
