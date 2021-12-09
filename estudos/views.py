from django.shortcuts import render

def index(request):
    """Página inicial do projeto."""
    return render(request, 'estudos/index.html')
