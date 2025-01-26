# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Producto, Usuario, Orden
# from .forms import ProductoForm, UsuarioForm, OrdenForm

# def index(request):
#     query = request.GET.get('q')
#     if query:
#         productos = Producto.objects.filter(titulo__icontains=query)
#     else:
#         productos = Producto.objects.all()
#     return render(request, 'tienda_app/index.html', {'productos': productos})

# def agregar_producto(request):
#     if request.method == 'POST':
#         form = ProductoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ProductoForm()
#     return render(request, 'tienda_app/agregar_producto.html', {'form': form})

# def agregar_usuario(request):
#     if request.method == 'POST':
#         form = UsuarioForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = UsuarioForm()
#     return render(request, 'tienda_app/agregar_usuario.html', {'form': form})

# def ver_pedidos(request):
#     pedidos = Orden.objects.all()
#     return render(request, 'tienda_app/ver_pedidos.html', {'pedidos': pedidos})

# def realizar_pedido(request, producto_id):
#     producto = get_object_or_404(Producto, id=producto_id)
#     if request.method == 'POST':
#         form = OrdenForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = OrdenForm(initial={'producto': producto})
#     return render(request, 'tienda_app/realizar_pedido.html', {'form': form, 'producto': producto})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Producto, Usuario, Orden, Page
from .forms import ProductoForm, UsuarioForm, OrdenForm, PageForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

# Vistas para el Blog (Pages)
def about(request):
    return render(request, 'tienda_app/about.html')

def pages(request):
    pages = Page.objects.all()
    return render(request, 'tienda_app/pages.html', {'pages': pages})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'tienda_app/page_detail.html', {'page': page})

@login_required
def create_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.save()
            return redirect('pages')
    else:
        form = PageForm()
    return render(request, 'tienda_app/create_page.html', {'form': form})

@login_required
def update_page(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.user != page.author:
        return redirect('pages')
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('page_detail', pk=page.pk)
    else:
        form = PageForm(instance=page)
    return render(request, 'tienda_app/update_page.html', {'form': form, 'page': page})

@login_required
def delete_page(request, pk):
    page = get_object_or_404(Page, pk=pk)
    
    if request.method == 'POST':
        page.delete()
        return redirect('pages')
    if request.user == page.author:
        return render(request, 'tienda_app/confirm_delete.html', {'page': page})
        # page.delete()
    
    return redirect('pages')



# Login y Logout
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('pages')
    else:
        form = AuthenticationForm()
    return render(request, 'tienda_app/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tienda_app/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('pages')
