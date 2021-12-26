from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Topico, Entrada

class FormularioTopico(forms.ModelForm):
    def clean_data_texto(self):
        data = self.cleaned_data['texto']
        
        return data
    
    class Meta:
        model = Topico
        fields = ['texto']
        labels = {'texto': _('Novo tópico')}


class FormularioEntrada(forms.ModelForm):
    def clean_data_texto(self):
        data = self.cleaned_data['texto']

        return data

    class Meta:
        model = Entrada
        fields = ['texto']
        labels = {'texto': ''}


class EditarEntrada(forms.ModelForm):
    def clean_data_texto(self):
        data = self.cleaned_data['texto']

        return data

    def clean_data_topico(self):
        data = self.cleaned_data['topico']

        return data

    class Meta:
        model = Entrada
        fields = ['texto']
        labels = {'texto': ''}
