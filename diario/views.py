from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topico
from .forms import FormularioTopico

def index(request):
    """Página inicial"""
    return render(request, 'diario/index.html')


def topicos(request):
    """Página de tópicos"""
    topicos = Topico.objects.order_by('data_pub')
    contexto = {'topicos': topicos}

    return render(request, 'diario/topicos.html', contexto)


def topico(request, topico_id):
    """Página dos assuntos dos tópicos"""
    topicos = Topico.objects.get(id=topico_id)
    entradas = topicos.entrada_set.order_by('-data_ent')
    contexto = {'topicos': topicos, 'entradas': entradas}

    return render(request, 'diario/topico.html', contexto)


def novo_topico(request):
    """Adiciona um novo assunto"""
    topico = Topico.objects.all()
    
    if request.method == 'POST':
        """Dados de POST submetidos; processa os dados."""
        formulario = FormularioTopico(request.POST)

        if formulario.is_valid():
            topico = Topico.objects.create()
            topico.texto = formulario.cleaned_data['texto']
            
            topico.save()
            
            return HttpResponseRedirect(reverse('topicos'))
    else:
        """Nenhum dado recebido; cria um formulário em branco."""
        formulario = FormularioTopico()

    contexto = {'formulario': formulario, 'topico': topico}

    return render(request, 'diario/novo_topico.html', contexto)
