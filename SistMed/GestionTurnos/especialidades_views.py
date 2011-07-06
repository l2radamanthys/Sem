#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth #para login
from django.contrib.auth.models import User, Group

from GestionTurnos.models import Expecialidades
from utils import get_field_css, get_value, generar_base_dict
from constantes import *


def agregar(request):
    """
        Agrega una nueva expecialidad de Medico
    """
    plantilla = get_template('especialidades/nueva.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Agregar Expecialidad'

    query = int(request.POST.get('query', '0'))
    dict['query'] = query

    if query:
        nombre = get_value(request, 'nombre', '')
        if nombre != '':
            if not(Expecialidades.objects.filter(nombre=nombre)):
                exp = Expecialidades(nombre=nombre)
                exp.save()
                dict['msj_class'] = MSJ_OK
                dict['mensaje'] = 'Se a Agregado %s' %nombre
            else:
                dict['msj_class'] = MSJ_ERROR
                dict['mensaje'] = 'Error la expecialidad ya existe %s' %nombre
                

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listado(request):
    """
        Muestra el Listado de Expecialidades
    """
    plantilla = get_template('especialidades/listado.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Listado Expecialidad Medicas'

    lista = []
    band = True
    for esp in Expecialidades.objects.all().order_by('nombre'):
        lista.append((esp.id, esp.nombre, get_field_css(band)))
        band = not(band)
    dict['especialidades'] = lista
    
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrar(request, esp_id=-1):
    """
        Borrar una Expecialidad Medica
    """
    plantilla = get_template('especialidades/borrar.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Borrar Especialidad Medica'

    esp_id = int(esp_id)
    if esp_id != -1:
        especialidad = Expecialidades.objects.get(id=esp_id)
        dict['query'] = True
        dict['nombre'] = especialidad.nombre
        dict['esp_id'] = esp_id

    else:
        dict['query'] = False
        dict['msj_class'] = MSJ_ERROR
        dict['mensaje'] = 'Error Datos Invalido'

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrado(request, esp_id=-1):
    """
        Permite Borrar una Especialidad

        pueden acceder
        --------------
        - administrativos
        - medicos

        sin acceso
        ----------
        - pacientes
        - usuarios no registrados
    """
    plantilla = get_template('especialidades/borrado.html')
    dict =  generar_base_dict(request)
    dict['titulo'] = 'Borrar Especialidad Medica'

    esp_id = int(esp_id)

    if esp_id != -1:
        especialidad = Expecialidades.objects.get(id=esp_id)
        dict['query'] = True
        dict['nombre'] = especialidad.nombre
        #borramos
        Expecialidades.objects.filter(id=esp_id).delete()
        
    else:
        dict['query'] = False
        dict['msj_class'] = MSJ_ERROR
        dict['mensaje'] = 'Error Operacion No valida'

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)