from django.db import models
from django.contrib.auth.models import User


class Topico(models.Model):
    """Criação dos tópicos."""
    texto = models.CharField(max_length=200)
    data_pub = models.DateTimeField(auto_now_add=True)
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Devolve o nome do tópico em strings."""
        return self.texto


class Entrada(models.Model):
    """Criação dos assuntos e relações com os tópicos."""
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    texto = models.TextField()
    data_ent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve o assunto em strings."""
        if len(self.texto) < 50:
            return self.texto
        else:
            return f'{self.texto[:50]}...'
