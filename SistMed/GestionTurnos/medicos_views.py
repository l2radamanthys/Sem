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

from GestionTurnos.models import Medicos, TipoUsuario, Expecialidades, ExpecialidadesMedicos
from utils import get_field_css, sexo_choice_expand, get_POST_value, generar_base_dict
from constantes import BASE_DIC, MSJ_OK, MSJ_ERROR

def nuevo_medico(request):
    """
        Vista que Permite crear un nuevo paciente

        pueden acceder
        ------------
        -administrativos

        sin acceso
        ----------
        - usuarios no registrados
        - pacientes
        - medicos

    """
    plantilla = get_template('medicos/gestion_turnos/nuevo.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Nuevo Medico'

    #si se realizo una consulta
    query = int(request.POST.get('query', '0'))
    dict['query'] = query

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
            medico = Medicos(
                dni = int(get_POST_value(request,'dni','0','0')),
                sexo = get_POST_value(request,'sexo','-','-'),
                telefono = request.POST.get('telefono', ''),
                direccion = request.POST.get('direccion', ''),
                tipo_usuario = TipoUsuario.objects.get(nombre__exact='Paciente'),
                user = User.objects.get(username__exact=username),
                matricula = request.POST.get('matricula', '0'),
            )
            #guardamos
            medico.save()
            dict['msj_class'] = MSJ_OK
            dict['mensaje'] = "Se ha Agregado: %s" %username

        else:
            dict['msj_class'] = MSJ_ERROR
            dict['mensaje'] = "Error el nombre de usuario %s, no esta disponible" %username

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listado_medicos(request):
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
    plantilla = get_template('medicos/gestion_turnos/listado.html')
    dict = dict = generar_base_dict(request)
    dict['titulo'] = 'Listado Medicos'

    listado_medicos = []
    band = True
    for medico in Medicos.objects.all():
        id = medico.id
        username = medico.username()
        nombre = medico.nombre_completo()
        css = get_field_css(band)
        band = not(band)
        listado_medicos.append([id, username, nombre, css])


    dict['listado_medicos'] = listado_medicos

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def agregar_especialidad(request, med_id=-1):
    """
    """
    plantilla = get_template('medicos/gestion_turnos/agregar-especialidad.html')
    dict = dict = generar_base_dict(request)
    dict['titulo'] = 'Medico - Agregar Expecialidad'

    #si se realizo una consulta
    query = int(request.POST.get('query', '0'))
    dict['query'] = query
    #id pasado
    med_id = int(med_id)

    if med_id != -1:
        medico = Medicos.objects.get(id=med_id)
        dict['med_name'] = medico.nombre_completo()

        #agregamos la especialidad al medico
        if query:
            #medico = Medicos.objects.get(id=med_id)
            especialidad = Expecialidades.objects.get(id=get_POST_value(request,'especialidad','-1','-1'))
            esp_x_med = ExpecialidadesMedicos(codigo_medico=medico, cod_expecialidad=especialidad)
            esp_x_med.save()

            dict['msj_class'] = MSJ_OK
            dict['mensaje'] = 'Se Asigno la Especialidad %s' %especialidad.nombre
            


        
        especialidades_disp = [] #las q pueden ser agregadas
        especialidades_no_disp = [] #las q ya tiene el medico

        #esp no disponibles
        band = True
        for especialidad in ExpecialidadesMedicos.objects.filter(codigo_medico__id=med_id):
            especialidades_no_disp.append((especialidad.id, especialidad.cod_expecialidad.nombre,get_field_css(band)))
            band = not(band)

        #esp disponibles
        for esp in Expecialidades.objects.all().order_by('nombre'):
            especialidades_disp.append((esp.id, esp.nombre))

        dict['med_exp'] = especialidades_no_disp
        dict['especialidades'] = especialidades_disp

    else:
        pass


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)