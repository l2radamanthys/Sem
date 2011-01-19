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
from utils import get_field_css, sexo_choice_expand, get_POST_value
from constantes import BASE_DIC, PACIENTES


def nuevo_paciente(request):
    """
        Vista que Permite crear un nuevo paciente

        pueden acceder
        --------------
        - usuarios no registrados
        - medicos
        -administrativos

        sin acceso
        ----------
        - pacientes
    """
    plantilla = get_template('pacientes/gestion_turnos/nuevo.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Nuevo Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'

    #si se realizo una consulta
    query = int(request.POST.get('query', '0'))
    dict['query'] = query

    if query:
        username = request.POST.get('usuario', '')
        password = request.POST.get('password_1', '')
        email = request.POST.get('email', '')

        #para comprobar si el usuario ya existe
        #user = User.objects.get(username__exact=username)
        user = None
        if user is None:
            user = User.objects.create_user(username, email, password)
            user.first_name = request.POST.get('nombre', '-')
            user.last_name = request.POST.get('apellido', '-')
            user.email = request.POST.get('email', '@')
            user.is_staff = False #no es admin
            user.is_active = True #esta activo
            #lo agrego al grupo de los pacientes
            pac_group = Group.objects.get(name=PACIENTES)
            user.groups.add(pac_group)
            #guardamos
            user.save()
            paciente = Pacientes(
                dni = int(get_POST_value(request,'dni','0','0')),
                sexo = get_POST_value(request,'sexo','-','-'),
                telefono = request.POST.get('telefono', ''),
                direccion = request.POST.get('direccion', ''),
                user = User.objects.get(username__exact=username)
            )
            #guardamos
            paciente.save()
            dict['msj_class'] = 'msj_ok'
            dict['mensaje'] = "Se ha Agregado: %s" %username
            
        else:
            dict['msj_class'] = 'msj_error'
            dict['mensaje'] = "Error el nombre de usuario %s, no esta disponible" %username

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listado_pacientes(request):
    """
        Vista que permite mostrar el listado de pacientes

        pueden acceder
        --------------
        - medicos
        -administrativos

        sin acceso
        ----------
        - usuarios no registrados
        - pacientes
    """
    plantilla = get_template('pacientes/gestion_turnos/listado.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Listado Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
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


def datos_paciente(request, pac_id=-1):
    """
        Muestra los datos del Paciente ademas de las
        solicitudes y turnos q le fueron asignados

        pueden acceder
        --------------
        - medicos
        - administrativos
        - pacientes (unicamente a su propio perfil)

        sin acceso
        ----------
        - usuarios no registrados
    """
    plantilla = get_template('pacientes/gestion_turnos/datos.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Datos Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'


    pac_id = int(pac_id)
    if pac_id != -1:
        paciente = Pacientes.objects.get(id=pac_id)
        dict['pac_id'] = pac_id
        dict['username'] = paciente.username()
        dict['nombre'] = paciente.nombre_completo()
        dict['direccion'] = paciente.direccion
        dict['telefono'] = paciente.telefono
        dict['email'] = paciente.username()
        dict['sexo'] = sexo_choice_expand(paciente.sexo)

    else:
        pass

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_paciente(request, pac_id=-1):
    """
        Permite modificar algunos datos del paciente

        pueden acceder
        --------------
        - medicos
        - administrativos
        - pacientes (unicamente a su propio perfil)

        sin acceso
        ----------
        - usuarios no registrados
    """
    plantilla = get_template('pacientes/gestion_turnos/modificar.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Modificar Datos Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'

    pac_id = int(pac_id)
    if pac_id != -1:
        #query = int(get_POST_value(request,'query', '0'))
        #dict['query'] = query
        #si se envio un formulario modificado
        #if query:
        #    pass
        #caso q recien se muestre la pagina
        #else:
        dict['query'] = True
        paciente = Pacientes.objects.get(id=pac_id)
        dict['nombre'] = paciente.user.first_name
        dict['apellido'] = paciente.user.last_name
        dict['dni'] = paciente.dni
        dict['direccion'] = paciente.direccion
        dict['telefono'] = paciente.telefono
        dict['email'] = paciente.user.email
        dict['sexo'] = paciente.sexo

    else:
        dict['query'] = False
        dict['msj_class'] = 'msj_error'
        dict['mensaje'] = 'Error Datos Invalido'


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def guardar_cambios_paciente(request, pac_id=-1):
    """
        Permite modificar algunos datos del paciente

        pueden acceder
        --------------
        - medicos
        - administrativos
        - pacientes (unicamente a su propio perfil)

        sin acceso
        ----------
        - usuarios no registrados
    """
    plantilla = get_template('pacientes/gestion_turnos/guardar.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Guardar Datos Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'


    query = int(get_POST_value(request,'query', '0'))
    dict['query'] = query

    pac_id = int(pac_id)
    if pac_id != -1 and query:
        paciente = Pacientes.objects.get(id=pac_id)
        paciente.user.first_name = get_POST_value(request,'nombre','')
        paciente.user.last_name = get_POST_value(request,'apellido','')
        paciente.user.save()
        paciente.dni = int(get_POST_value(request,'dni','0','0'))
        paciente.direccion = get_POST_value(request,'direccion','')
        paciente.telefono = get_POST_value(request,'telefono','')
        paciente.email = get_POST_value(request,'email','')
        paciente.sexo = get_POST_value(request,'sexo','-','-')
        paciente.save()

        #redireciono a la pagina q muestra los datos del paciente
        HttpResponseRedirect("/pacientes/datos/%d/" %pac_id)
        

    else:
        dict['query'] = False
        dict['msj_class'] = 'msj_error'
        dict['mensaje'] = 'Error Datos Invalido'


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrar_paciente(request, pac_id=-1):
    """
        Vista de confirmacion de borrado de un paciente

        pueden acceder
        --------------
        - administrativos

        sin acceso
        ----------
        - medicos
        - pacientes
        - usuarios no registrados
    """
    plantilla = get_template('pacientes/gestion_turnos/borrar.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Borrar Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'

    pac_id = int(pac_id)

    if pac_id != -1:
        paciente = Pacientes.objects.get(id=pac_id)
        dict['query'] = True
        dict['nombre'] = paciente.nombre_completo()
        dict['pac_id'] = pac_id

    else:
        dict['query'] = False
        dict['msj_class'] = 'msj_error'
        dict['mensaje'] = 'Error Datos Invalido'


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrado_paciente(request, pac_id=-1):
    """
        Permite Borrar un paciente

        pueden acceder
        --------------
        - administrativos

        sin acceso
        ----------
        - medicos
        - pacientes
        - usuarios no registrados
    """
    plantilla = get_template('pacientes/gestion_turnos/borrar.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Borrar Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'

    pac_id = int(pac_id)

    if pac_id != -1:
        paciente = Pacientes.objects.get(id=pac_id)
        dict['query'] = True
        dict['nombre'] = paciente.nombre_completo()
        paciente.user.delete()
        paciente.delete()

    else:
        dict['query'] = False
        dict['msj_class'] = 'msj_error'
        dict['mensaje'] = 'Error Operacion No valida'



    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)