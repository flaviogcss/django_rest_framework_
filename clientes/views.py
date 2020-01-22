from django.shortcuts import render
from rest_framework import viewsets
from clientes.models import Cadastro
from clientes.serializers import CadastroSerializer

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer

# def delete(request, id):
#     cliente = Cadastro.objects.get(id=id)
#     cliente.delete()
#     return cliente
