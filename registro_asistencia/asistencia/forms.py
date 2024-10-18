from django import forms
from django.contrib.auth.models import User
from .models import Asistencia
import datetime

class AsistenciaForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    hora_entrada = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        initial=datetime.datetime.now().time(),
        required=True
    )
    hora_salida = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        required=False
    )

    class Meta:
        model = Asistencia
        fields = ['usuario', 'hora_entrada', 'hora_salida']
        
    def clean_hora_salida(self):
        hora_salida = self.cleaned_data.get('hora_salida')
        hora_entrada = self.cleaned_data.get('hora_entrada')
        
        if hora_salida and hora_entrada and hora_salida <= hora_entrada:
            raise forms.ValidationError("La hora de salida debe ser después de la hora de entrada.")
        
        return hora_salida
