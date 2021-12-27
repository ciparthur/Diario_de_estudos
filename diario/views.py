from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topico, Entrada
from .forms import FormularioTopico, FormularioEntrada, EditarEntrada

def index(request):
    """Página inicial"""
    return render(request, 'diario/index.html')


@login_required
def topicos(request):
    """Página de tópicos"""
    topicos = Topico.objects.filter(proprietario=request.user).order_by('data_pub')

    contexto = {'topicos': topicos}

    return render(request, 'diario/topicos.html', contexto)


@login_required
def topico(request, topico_id):
    """Página dos assuntos dos tópicos"""
    topicos = Topico.objects.get(id=topico_id)

    # Garante que assunto pertença ao usuário atual
    verificar_proprietario_topico(topicos.proprietario, request.user)

    entradas = topicos.entrada_set.order_by('-data_ent')

    contexto = {'topicos': topicos, 'entradas': entradas}

    return render(request, 'diario/topico.html', contexto)


@login_required
def novo_topico(request):
    """Adiciona um novo assunto"""

    if request.method == 'POST':
        """Dados de POST submetidos; processa os dados."""
        formulario = FormularioTopico(request.POST)

        if formulario.is_valid():
            topico = formulario.save(commit=False)
            topico.proprietario = request.user
            topico.save()

            return HttpResponseRedirect(reverse('topicos'))
    else:
        """Nenhum dado recebido; cria um formulário em branco."""
        formulario = FormularioTopico()

    contexto = {'formulario': formulario}

    return render(request, 'diario/novo_topico.html', contexto)


@login_required
def novo_assunto(request, topico_pk):
    novo_ass = get_object_or_404(Topico, pk=topico_pk)

    # Garante que o usuário atual seja o dono da conta
    verificar_proprietario_topico(novo_ass.proprietario, request.user)

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


@login_required
def editar_assunto(request, topico_pk):
    entrada = get_object_or_404(Entrada, pk=topico_pk)
    topico = entrada.topico

    # Garante que o usuário atual seja o dono da conta
    verificar_proprietario_topico(topico.proprietario, request.user)

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


def verificar_proprietario_topico(proprietario, usuario):
    if proprietario != usuario:
        raise Http404
