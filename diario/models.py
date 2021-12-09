from django.db import models


class Topico(models.Model):
    texto = models.CharField(max_length=200)
    data_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em strings do modelo."""
        return self.texto


class Entrada(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    texto = models.TextField()
    data_entrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em strings do modelo."""
        if len(self.texto) < 50:
            return self.texto
        else:
            return f'{self.texto[:50]}...'
