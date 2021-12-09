from django.shortcuts import render

from .models import Topico

def index(request):
    """Página inicial"""
    return render(request, 'diario/index.html')


def topicos(request):
    """Página de tópicos"""
    topicos = Topico.objects.order_by('-data_pub')
    contexto = {'topicos': topicos}

    return render(request, 'diario/topicos.html', contexto)
