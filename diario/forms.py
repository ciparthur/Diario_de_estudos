from django import forms

from .models import Topico

class FormularioTopico(forms.Form):
    texto = forms.CharField(max_length=200)
    
    def clean_data_texto(self):
        data = self.cleaned_data['texto']
        
        return data
