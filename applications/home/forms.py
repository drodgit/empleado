from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
        )

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un Nro mayor a 10')

        return cantidad
    