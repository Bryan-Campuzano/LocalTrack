from django import forms
from .models import Producto  # Asegúrate de que el modelo Product esté definido

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'stock']  # Ajusta los campos según tu modelo
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.Textarea(attrs={'class': 'form-control'}),
            'descripcion': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }
