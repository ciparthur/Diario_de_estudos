from django.shortcuts import render

from .models import Topico

def index(request):
    """Página inicial do projeto."""
    return render(request, 'estudos/index.html')


def topicos(request):
    topicos = Topico.objects.order_by('-data_pub')
    contexto = {'topicos': topicos}

    return render(request, 'estudos/topicos.html', contexto)
