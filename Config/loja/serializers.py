from rest_framework import serializers
from loja.models import Cliente,Pedido,Produto

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields =  ['nome', 'valor']


class PedidoSerializer(serializers.ModelSerializer):

    produtos = ProdutoSerializer(many=True)  # Usando o ProdutoSerializer para serializar os produtos

    class Meta:
        model = Pedido
        fields = '__all__'