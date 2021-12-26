from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))

def cadastro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():
            novo_usuario = formulario.save()

            usuario_autenticado = authenticate(username=novo_usuario.username, password=request.POST['password1'])

            login(request, usuario_autenticado)

            return HttpResponseRedirect(reverse('index'))
    else:
        """Exibe um formulário de cadastro em branco"""
        formulario = UserCreationForm()

    contexto = {'formulario': formulario}
    
    return render(request, 'registration/cadastro.html', contexto)
