#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    manejo de vistas referente a la asignacion de turnos..
"""


from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context

from django.contrib import auth #para login
from django.contrib.auth.models import User#, Group

from GestionTurnos.models import *
from utils import *
from constantes import MSJ_OK, MSJ_ERROR

import datetime


def mostrar_agenda_por_dia(request):
    """
        Muestra la Agenda del Medico de Acuerdo a un dia
    """
    plantilla = get_template('medicos/gestion_turnos/agenda-dia.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Agenda - '

    med_id = int(get_GET_value(request, "medico", "-1"))
    if med_id != -1:
        medico = Medicos.objects.get(med_id)

        cad = get_GET_value(request, "dia", "01/01/01")
        dia, mes, anio = cad.split("/")
        dia, mes, anio = int(dia), int(mes), int(anio)
        
        #filtra todos los turnos referente a la fecha y medico actual
        turnos = Turnos.objects.filter(codigo_medico=medico, fecha__day=dia, fecha__mounth=mes, fecha__year=anio)


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def nuevo_turno(request, med_id=-1):
    plantilla = get_template('medicos/gestion_turnos/nuevo-turno.html')
    dict = generar_base_dict(request)
    dict['sin_titulo'] = True #'Turnos - Nuevo'

    dict["med_name"] = Medicos.objects.get(id=int(med_id)).nombre_completo()

    dict["pacientes"] = Pacientes.objects.all()

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def nuevo_turno_adm(request, med_id=-1):
    plantilla = get_template('medicos/gestion_turnos/nuevo-turno-adm.html')
    dict = generar_base_dict(request)
    dict['sin_titulo'] = True #'Turnos - Nuevo'

    dict["medicos"] = Medicos.objects.all()
    dict["pacientes"] = Pacientes.objects.all()

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def nuevo_turno_pac(request):
    plantilla = get_template('medicos/gestion_turnos/nuevo-turno-pac.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Turnos - Nuevo'

    query = int(get_POST_value(request, 'query', '0'))
    dict['query'] = query

    med_id = int(get_GET_value(request, "med_id", 0))
    pac_id = int(get_GET_value(request, "pac_id", 0))

    if med_id and pac_id:
        dict['med_id'] = med_id
        dict['med_name'] = Medicos.objects.get(id=med_id).nombre_completo()
        dict['pac_id'] = pac_id
        dict['pac_name'] = Pacientes.objects.get(id=pac_id).nombre_completo()

    if query:
        fecha = get_value(request, "fecha", "00:00:00")
        #falta parsear la fecha
        
        med_id = int(get_POST_value(request, "med_id", 0))
        pac_id = int(get_POST_value(request, "pac_id", 0))
        comentarios = get_value(request, "comentarios", "")


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_turno(request):
    pass


def borrar_turno(request):
    pass


def nueva_solicitud_turno(request):
    """
        Crea una nueva solicitud de turno
    """
    plantilla = get_template('pacientes/gestion_turnos/nueva-solicitud-turno.html')
    dict = generar_base_dict(request)
    dict['sin_titulo'] = True #'Turnos - Solicitar Turno'

    dict['username'] = Pacientes.objects.get(id=request.session['usuario_id']).nombre_completo()
    dict["hoy"] = date_today_str()
    dict['pacientes'] = Pacientes.objects.all()
    dict['medicos'] = Medicos.objects.all()

    
    query = int(get_value(request, 'query', '0'))
    dict['query'] = query

    if query:
        if get_value(request, 'request', 'pac') == "pac":
            paciente = Pacientes.objects.get(id=request.session['usuario_id'])
        else:
            paciente = Pacientes.objects.get(id=int(get_value(request, 'pac_id', '-1')))


        medico = Medicos.objects.get(id=int(get_value(request, 'med_id', '-1')))
        fecha = date_split(get_value(request, 'fecha', '01/01/1900'))

        solicitud = SolitudesTurnos(
            fecha_requerida=fecha,
            estado="p",
            comentarios="",
            codigo_paciente=paciente,
            codigo_medico=medico
        )
        solicitud.save()
        dict['msj_class'] = MSJ_OK
        dict['mensaje'] = 'Solicitud de Turno Creada'

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def cancelar_solicitud(request):
    """
        Solo para pacientes
    """
    pass


def listado_solicitudes_turno(request, user_id):
    """
        listado de solicitudes de turno de  un paciente
    """
    plantilla = get_template('medicos/gestion_turnos/listado-solicitudes-turno.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Turnos - Listado de Solicitud de Turnos'


    medico = Medicos.objects.get(id=user_id)
    solicitudes = []
    band = True
    for sol in SolitudesTurnos.objects.filter(codigo_medico=medico): #por el momento todas, hay que filtrarlas por usuario
        solicitudes.append([get_field_css(band), date_to_str(sol.fecha_requerida), sol.codigo_paciente.nombre_completo(), estado_solicitud_expand(sol.estado), sol.id])
        band = not(band)

    dict["solicitudes"] = solicitudes


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listado_solicitudes_turno_pac(request):
    """
        listado de solicitudes de turnos q realizo un paciente
    """
    plantilla = get_template('pacientes/gestion_turnos/listado-solicitudes-turno.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Turnos - Listado de Solicitud de Turnos'

    paciente = Pacientes.objects.get(id=request.session.get('usuario_id', '-1'))
    solicitudes = []
    band = True
    for sol in SolitudesTurnos.objects.filter(codigo_paciente=paciente): #por el momento todas, hay que filtrarlas por usuario
        solicitudes.append([get_field_css(band), date_to_str(sol.fecha_requerida), sol.codigo_medico.nombre_completo(), estado_solicitud_expand(sol.estado), sol.id])
        band = not(band)

    dict["solicitudes"] = solicitudes


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def detalle_solicitud_turno_pac(request):
    """
    """
    plantilla = get_template('pacientes/gestion_turnos/mostrar-solicitud-turno.html')
    dict = generar_base_dict(request)
    dict['sin_titulo'] = True

    sol_id = int(get_GET_value(request, "sol_id", -1))
    if sol_id != -1:
        dict["sol"] = SolitudesTurnos.objects.get(id=sol_id)


    else:
        #HttpResponseRedirect("error")
        pass
    

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)



def modificar_solicitud(request):
    """
        Modifica, confirmacion o cancelacion del turno solicitado
    """
    pass

