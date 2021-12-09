from django.shortcuts import render

from .models import Topico

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
