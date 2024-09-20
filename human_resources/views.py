from django.shortcuts import render, get_object_or_404, redirect
from .models import Pqrs  # Asegúrate de tener el modelo PQRS definido
from .forms import PQRSForm  # Asegúrate de tener un formulario definido para manejar PQRS

def pqrs_list(request):
    pqrs = Pqrs.objects.all()  # Obtener todos los registros PQRS
    return render(request, 'human_resources/pqrs_list.html', {'pqrs': pqrs})  # Asegúrate de que esta plantilla exista

def pqrs_new(request):
    if request.method == "POST":
        form = PQRSForm(request.POST)
        if form.is_valid():
            pqrs = form.save()  # Guardar el nuevo PQRS
            return redirect('human_resources:pqrs_list')  # Redirigir a la lista de PQRS
    else:
        form = PQRSForm()
    return render(request, 'human_resources/pqrs_new.html', {'form': form})  # Asegúrate de que esta plantilla exista

def pqrs_edit(request, id):
    pqrs = get_object_or_404(Pqrs, id=id)  # Obtener el PQRS por id
    if request.method == "POST":
        form = PQRSForm(request.POST, instance=pqrs)
        if form.is_valid():
            form.save()  # Guardar los cambios
            return redirect('human_resources:pqrs_list')  # Redirigir a la lista de PQRS
    else:
        form = PQRSForm(instance=pqrs)
    return render(request, 'human_resources/pqrs_edit.html', {'form': form})  # Asegúrate de que esta plantilla exista

def pqrs_delete(request, id):
    pqrs = get_object_or_404(Pqrs, id=id)  # Obtener el PQRS por id
    if request.method == "POST":
        pqrs.delete()  # Borrar el PQRS
        return redirect('human_resources:pqrs_list')  # Redirigir a la lista de PQRS
    return render(request, 'human_resources/pqrs_delete.html', {'pqrs': pqrs})  # Asegúrate de que esta plantilla exista
