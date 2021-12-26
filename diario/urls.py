from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topicos/', views.topicos, name='topicos'),
    path('topicos/<int:topico_id>', views.topico, name='topico'),
    path('topicos/novo_topico/', views.novo_topico, name='novo_topico'),
    path('topicos/<int:topico_pk>/novo_assunto/', views.novo_assunto, name='novo_assunto'),
    path('topicos/<int:topico_pk>/editar_assunto/', views.editar_assunto, name='editar_assunto'),
]
