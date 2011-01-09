#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    manejo de vistas de los pacientes
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth #para login
from django.contrib.auth.models import User, Group

from GestionTurnos.models import Pacientes
from utils import get_field_css
from constantes import BASE_DIC


def nuevo_paciente(request):
    """
        Vista que Permite crear un nuevo paciente

        pueden acceder a esta vista
        - usuarios no registrados
        - medicos
        -administrativos

        sin acceso
        - pacientes
    """
    plantilla = get_template('pacientes/gestion_turnos/nuevo.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Nuevo Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['url_action'] = '/accounts/login/'

    #si se realizo una consulta
    query = int(request.POST.get('query', '0'))
    dict['query'] = query

    if query:
        username = request.POST.get('usuario', '')
        password = request.POST.get('password_1', '')
        email = request.POST.get('email', '')

        user = User.objects.create_user(username, email, password)
        user.first_name = request.POST.get('nombre', '')
        user.last_name = request.POST.get('apellido', '')
        user.is_staff = False #no es admin
        user.is_active = True #esta activo
        #lo agrego al grupo de los pacientes
        pac_group = Group.objects.get(name='Pacientes')
        user.groups.add(pac_group)
        #guardamos
        user.save()

        paciente = Pacientes(
            dni = int(request.POST.get('dni', '')),
            sexo = request.POST.get('sexo', '-'),
            telefono = request.POST.get('telefono', ''),
            direccion = request.POST.get('direccion', ''),
            user = User.objects.get(username__exact=username)
        )
        paciente.save()
        dict['msj_class'] = 'msj_ok'
        dict['mensaje'] = "Se ha Agregado, %s" %username


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listado_pacientes(request):
    """
        Vista que permite mostrar el listado de pacientes

        pueden acceder a esta vista
        - medicos
        -administrativos

        sin acceso
        - usuarios no registrados
        - pacientes
    """
    plantilla = get_template('pacientes/gestion_turnos/listado.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Listado Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['url_action'] = '/accounts/login/'


    listado_pacientes = []
    band = True
    for paciente in Pacientes.objects.all():
        id = paciente.id
        username = paciente.user.username
        nombre = paciente.nombre_completo()
        css = get_field_css(band)
        band = not(band)
        listado_pacientes.append([id, username, nombre, css])


    dict['listado_pacientes'] = listado_pacientes

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)

