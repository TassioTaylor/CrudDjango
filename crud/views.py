from django.http import HttpResponse
from django.shortcuts import render, redirect

from crud.models import Clientes


def cadastro_cliente(request):
    return render(request, 'cadastro.html')


def cadastrar_cliente(request):
    nome = request.POST.get('nome')
    endereco = request.POST.get('endereco')
    fone = request.POST.get('fone')
    data_nascimento = request.POST.get('data_nascimento')

    novo_cliente = Clientes(nome=nome, endereco=endereco, fone=fone, data_nascimento=data_nascimento)
    novo_cliente.save()
    return redirect('/clientes')


def clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})
