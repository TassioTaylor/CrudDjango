from django.http import HttpResponse
from django.shortcuts import render, redirect

from crud.models import Clientes


def cadastro_cliente(request):
    id_cliente = request.GET.get('id')
    if id_cliente:
        cliente = Clientes.objects.get(id=id_cliente)
    return render(request, 'cadastro.html', {'cliente': cliente})


def editar_cliente(request, id):
    cliente = Clientes.objects.get(id=id)
    return render(request, 'cadastro.html', {'cliente': cliente})


def cadastrar_cliente(request):
    if request.POST:
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        fone = request.POST.get('fone')
        data_nascimento = request.POST.get('data_nascimento')
        id_cliente = request.POST.get('id_cliente')

        if id_cliente:
            Clientes.objects.filter(id=id_cliente).update(nome=nome,
                                                          endereco=endereco,
                                                          fone=fone,
                                                          data_nascimento=data_nascimento)

        else:
            novo_cliente = Clientes(nome=nome, endereco=endereco, fone=fone, data_nascimento=data_nascimento)
            novo_cliente.save()


    return redirect('/clientes')


def clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


def excluir(request, id):
    Clientes.objects.get(id=id).delete()
    return redirect('/clientes')
