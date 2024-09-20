from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from inventory.models import Remision  # Asegúrate de que estos modelos estén definidos
from .forms import ClientForm, OrderForm  # Asegúrate de que estos formularios existan

def clients_list(request):
    clients = Cliente.objects.all()
    return render(request, 'sales/clients.html', {'clients': clients})

def clients_new(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales:clients_list')
    else:
        form = ClientForm()
    return render(request, 'sales/clients_new.html', {'form': form})

def clients_edit(request, id):
    client = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('sales:clients_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'sales/clients_edit.html', {'form': form})

def clients_delete(request, id):
    client = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        client.delete()
        return redirect('sales:clients_list')
    return render(request, 'sales/clients_delete.html', {'client': client})

def orders_list(request):
    orders = Remision.objects.all()
    return render(request, 'sales/orders.html', {'orders': Remision})

def orders_new(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales:orders_list')
    else:
        form = OrderForm()
    return render(request, 'sales/orders_new.html', {'form': form})

def orders_edit(request, id):
    order = get_object_or_404(Remision, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=Remision)
        if form.is_valid():
            form.save()
            return redirect('sales:orders_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'sales/orders_edit.html', {'form': form})

def orders_delete(request, id):
    order = get_object_or_404(Remision, id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('sales:orders_list')
    return render(request, 'sales/orders_delete.html', {'order': Remision})
