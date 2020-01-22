from rest_framework import serializers
from clientes.models import Cadastro
from produtos.models import Produto
from vendas.models import Venda
from produtos.serializers import ProdutoSerializer

class CadastroSerializer(serializers.Serializer):

    nome = serializers.CharField(max_length=255)
    telefone = serializers.CharField(max_length=15)
    cpf = serializers.CharField(max_length=15)
    email = serializers.EmailField()
    nascimento = serializers.CharField(max_length=12)
    idade = serializers.IntegerField()

    def create(self, validated_data):
        cadastro = Cadastro.objects.create(**validated_data)
        return cadastro

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.telefone = validated_data.get('telefone', instance.telefone)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.email = validated_data.get('email', instance.email)
        instance.nascimento = validated_data.get('nascimento', instance.nascimento)
        intancce.idade = validated_data.get('idade', instance.idade)
        instance.save()
        return instance

    