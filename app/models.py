from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Lavagem(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField()
    tipo = models.CharField(max_length=50)  # ex: Completa, Simples, Motor
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente.nome} - {self.data.strftime('%d/%m/%Y %H:%M')}"

