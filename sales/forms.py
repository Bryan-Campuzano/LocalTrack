# sales/forms.py

from django import forms
from .models import Cliente
from inventory.models import Remision  # Asegúrate de que estos modelos estén definidos

class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'telefono']  # Asegúrate de incluir los campos que necesites
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Remision
        fields = ['cliente_id', 'venta_id','fecha']  # Asegúrate de incluir los campos que necesites
        widgets = {
            'cliente_id': forms.Select(attrs={'class': 'form-control'}),
            'venta_id': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
