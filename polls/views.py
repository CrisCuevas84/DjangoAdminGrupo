from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import * # Esta importando todos los modelos con el *


def index(request):
    clientes = Client.objects.all()
    context = {
        'client_list' : clientes,
    }
    return render(request, 'polls/home.html', context)


def clientes(request):
    clientes = Client.objects.all()
    context = {
        'client_list' : clientes,
    }
    return render(request, 'polls/cliente.html', context)


def sitios(request):
    sitios = Site.objects.all()
    context = {
        'sites_list' : sitios,
    }
    return render(request, 'polls/sites.html', context)


def oportunidades(request):
    oportunidades = Lead.objects.all()
    context = {
        'leads_list' : oportunidades,
    }
    return render(request, 'polls/leads.html', context)


def documentos(request):
    documentos = Documento.objects.all()
    context = {
        'documents_list' : documentos,
    }
    return render(request, 'polls/documents.html', context)


def libros_publicadores(request):
    libros = Libro.objects.all()
    publicadores = Publicador.objects.all()
    context = {
        'lista_libros': libros,
        'lista_publicadores': publicadores, 
    }
    return render(request, 'polls/libros_publicadores.html' ,context)


def editar(request):
    publicador = Publicador.objects.get(id=request.POST['id'])
    context = {
        "publicador": publicador
    }
    return render(request,'polls/edit.html', context)


def update(request):
    publicador = Publicador.objects.get(id=request.POST['id'])
    publicador.nombre = request.POST['publicador']
    publicador.save()
    return redirect('libros_publicadores')
