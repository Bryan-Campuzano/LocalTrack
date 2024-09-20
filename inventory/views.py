from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto  # Asegúrate de tener un modelo Product definido
from .forms import ProductForm  # Importa el formulario que hayas creado para manejar productos

def inventory_list(request):
    products = Producto.objects.all()
    return render(request, 'inventory/inventory.html', {'products': products})

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('inventory:inventory_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/product_new.html', {'form': form})

def product_edit(request, id):
    product = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('inventory:inventory_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/product_edit.html', {'form': form})

def product_delete(request, id):
    product = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        product.delete()
        return redirect('inventory:inventory_list')
    return render(request, 'inventory/product_delete.html', {'product': Producto})
