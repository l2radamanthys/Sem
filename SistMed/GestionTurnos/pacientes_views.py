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

from GestionTurnos.models import Pacientes, TipoUsuario
from utils import get_field_css, sexo_choice_expand, get_POST_value, generar_base_dict
from constantes import *


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
    dict = generar_base_dict(request)
    dict['titulo'] = 'Nuevo Paciente'

    #si se realizo una consulta
    query = int(request.POST.get('query', '0'))
    dict['query'] = query

    dict["tipo_doc"] = TIPO_DOC_CHOICE

    if query:
        username = request.POST.get('usuario', '')
        password = request.POST.get('password_1', '')
        email = request.POST.get('email', '@')

        #para comprobar si el usuario ya existe
        user = User.objects.filter(username__exact=username)
        if user != None:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = request.POST.get('nombre', '-')
            user.last_name = request.POST.get('apellido', '-')
            user.email = request.POST.get('email', '@')
            user.is_staff = False #no es admin
            user.is_active = True #esta activo
            #lo agrego al grupo de los pacientes
            #pac_group = Group.objects.get(name=PACIENTES)
            #user.groups.add(pac_group)
            #guardamos
            user.save()
            paciente = Pacientes(
                dni = int(get_POST_value(request,'dni','0','0')),
                tipo_doc = get_POST_value(request,'tipo_doc','',''),
                sexo = get_POST_value(request,'sexo','-','-'),
                telefono = request.POST.get('telefono', ''),
                direccion = request.POST.get('direccion', ''),
                tipo_usuario = TipoUsuario.objects.get(nombre__exact='Paciente'),
                user = User.objects.get(username__exact=username)

            )
            #guardamos
            paciente.save()
            dict['msj_class'] = MSJ_OK
            dict['mensaje'] = "Se ha Agregado: %s" %username
            
        else:
            dict['msj_class'] = MSJ_ERROR
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
    dict = dict = generar_base_dict(request)
    dict['titulo'] = 'Listado Paciente'
    
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
    dict = dict = generar_base_dict(request)
    dict['titulo'] = 'Datos Paciente'

    pac_id = int(pac_id)
    if pac_id != -1:
        paciente = Pacientes.objects.get(id=pac_id)
        dict['pac_id'] = pac_id
        dict['username'] = paciente.username()
        dict['nombre'] = paciente.nombre_completo()
        dict['direccion'] = paciente.direccion
        dict['telefono'] = paciente.telefono
        dict['email'] = paciente.user.email
        dict["doc"] = paciente.doc()
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
    dict = generar_base_dict(request)
    dict['titulo'] = 'Modificar Datos Paciente'

    dict["tipo_doc"] = TIPO_DOC_CHOICE

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
        dict['pac_id'] = pac_id
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
        dict['msj_class'] = MSJ_ERROR
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
    dict = generar_base_dict(request)
    dict['titulo'] = 'Guardar Datos Paciente'
   
    query = int(get_POST_value(request,'query', '0'))
    dict['query'] = query

    pac_id = int(pac_id)
    if pac_id != -1 and query:
        paciente = Pacientes.objects.get(id=pac_id)
        paciente.user.first_name = get_POST_value(request,'nombre','')
        paciente.user.last_name = get_POST_value(request,'apellido','')
        paciente.user.save()
        paciente.dni = int(get_POST_value(request,'dni','0','0'))
        paciente.tipo_doc = get_POST_value(request,'tipo_doc','--','--')
        paciente.direccion = get_POST_value(request,'direccion','')
        paciente.telefono = get_POST_value(request,'telefono','')
        paciente.email = get_POST_value(request,'email','')
        paciente.sexo = get_POST_value(request,'sexo','-','-')
        paciente.save()

        #redireciono a la pagina q muestra los datos del paciente
        #HttpResponseRedirect("/pacientes/datos/%d/" %pac_id)
        dict['pac_id'] = pac_id
        dict['msj_class'] = MSJ_OK
        dict['mensaje'] = 'Cambios Realizados Correctamente'

    else:
        #dict['query'] = False
        dict['msj_class'] = MSJ_ERROR
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
    dict =  generar_base_dict(request)
    dict['titulo'] = 'Borrar Paciente'
 
    pac_id = int(pac_id)

    if pac_id != -1:
        paciente = Pacientes.objects.get(id=pac_id)
        dict['query'] = True
        dict['nombre'] = paciente.nombre_completo()
        dict['pac_id'] = pac_id

    else:
        dict['query'] = False
        dict['msj_class'] = MSJ_ERROR
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
    dict =  generar_base_dict(request)
    dict['titulo'] = 'Borrar Paciente'
   
    pac_id = int(pac_id)
    if pac_id != -1:
        paciente = Pacientes.objects.get(id=pac_id)
        dict['query'] = True
        dict['nombre'] = paciente.nombre_completo()
        paciente.user.delete() #se eliminan datos en cascada
        #paciente.delete()

    else:
        dict['query'] = False
        dict['msj_class'] = MSJ_ERROR
        dict['mensaje'] = 'Error Operacion No valida'

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def buscar_pacientes(request):
    """
        Permite Buscar un paciente por nombre, apellido o usuario

        pueden acceder
        --------------
        - administrativos
        - medicos

        sin acceso
        ----------
        - pacientes
        - usuarios no registrados
    """
    plantilla = get_template('pacientes/gestion_turnos/buscar.html')
    dict =  generar_base_dict(request)
    dict['sin_titulo'] = True
   
    #tipo de busqueda
    #1 usuario
    #2 nombre
    #3 apellido
    query = int(request.POST.get('query', '0'))
    dict['query'] = query
    if query:
        buscar_text = request.POST.get('buscar_text', '')
        buscar_por = int(request.POST.get('buscar_por', '0'))

        if buscar_text != "":
            if buscar_por == 0:
                list_pacientes = Pacientes.objects.filter(user__username__icontains=buscar_text)

            elif buscar_por == 1:
                list_pacientes = Pacientes.objects.filter(user__first_name__icontains=buscar_text)

            elif buscar_por == 2:
                list_pacientes = Pacientes.objects.filter(user__last_name__icontains=buscar_text)

        #si se ingreso text en blanco pongo todos
        else:
            list_pacientes = Pacientes.objects.all()

            
        listado_pacientes = []
        band = True
        for paciente in list_pacientes:
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