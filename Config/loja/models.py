from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50, blank=True, default="")
    cpf = models.CharField(max_length=50, blank=True, default="")

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    numeropedido = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valortotal = models.DecimalField(max_digits=10, decimal_places=2)
    produtos = models.ManyToManyField(Produto)
    
    def __str__(self):
        return self.numeropedido
