from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topicos/', views.topicos, name='topicos'),
    path('topicos/<int:topico_id>', views.topico, name='topico'),
]
