from django.shortcuts import render

def index(request):
    """Página inicial"""
    return render(request, 'diario/index.html')
