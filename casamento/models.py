from django.db import models


class Convidado(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    codigo_convite = models.CharField(max_length=20, unique=True)
    na_lista = models.BooleanField(default=False)
    presenca_confirmada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Presente(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='presentes/')

    def __str__(self):
        return self.nome

class Compra(models.Model):
    convidado = models.ForeignKey(Convidado, on_delete=models.CASCADE)
    presente = models.ForeignKey(Presente, on_delete=models.CASCADE)
    data_compra = models.DateTimeField(auto_now_add=True)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    status_pagamento = models.CharField(max_length=20, default='pendente')

    def __str__(self):
        return f'{self.convidado.nome} - {self.presente.nome}'
