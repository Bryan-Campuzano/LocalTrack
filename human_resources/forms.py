from django import forms
from .models import Pqrs  # Asegúrate de que el modelo PQRS esté definido

class PQRSForm(forms.ModelForm):
    class Meta:
        model = Pqrs
        fields = ['asunto', 'fechaRadicado', 'contenidoPqrs', 'fkCliente']  # Ajusta los campos según tu modelo
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Personaliza el widget del campo
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asunto'].label = 'asunto'  # Personaliza la etiqueta del campo
        self.fields['fechaRadicado'].label = 'fechaRadicado'
        self.fields['contenidoPqrs'].label = 'contenidoPqrs'
        self.fields['fkCliente'].label = 'fkCliente'