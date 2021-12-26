from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topico, Entrada
from .forms import FormularioTopico, FormularioEntrada, EditarEntrada

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
    topico = get_object_or_404(Topico)
    
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

def novo_assunto(request, topico_pk):
    novo_ass = get_object_or_404(Topico, pk=topico_pk)
    
    if request.method == 'POST':
        formulario = FormularioEntrada(request.POST)
        
        if formulario.is_valid():
            novo_ass = novo_ass.entrada_set.create()
            
            novo_ass.texto = formulario.cleaned_data['texto']
            
            novo_ass.save()
            
            return HttpResponseRedirect(reverse('topicos'))
    else:
        formulario = FormularioEntrada()
    
    contexto = {'formulario': formulario, 'novo_ass': novo_ass}
    
    return render(request, 'diario/novo_assunto.html', contexto)

def editar_assunto(request, topico_pk):
    entrada = get_object_or_404(Entrada, pk=topico_pk)
    
    if request.method == 'POST':
        formulario = EditarEntrada(instance=entrada, data=request.POST)
        
        if formulario.is_valid():
            entrada.texto = formulario.cleaned_data['texto']
            
            entrada.save()
            
            return HttpResponseRedirect(reverse('topicos'))
    else:
        formulario = EditarEntrada(instance=entrada)

    contexto = {'formulario': formulario, 'entrada': entrada}
    
    return render(request, 'diario/editar_assunto.html', contexto)
