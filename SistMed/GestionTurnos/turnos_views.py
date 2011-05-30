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

        cad = get_GET_value(request, "dia", "1.1.11")
        dia, mes, anio = cad.split(".")
        dia, mes, anio = int(dia), int(mes), int(anio)
        
        #filtra todos los turnos referente a la fecha y medico actual
        turnos = Turnos.objects.filter(codigo_medico=medico, \
                    fecha__day=dia, fecha__mounth=mes, fecha__year=anio)


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def nuevo_turno(request):
    pass


def modificar_turno(request):
    pass


def borrar_turno(request):
    pass


def nueva_solicitud_turno(request):
    """
        Crea una nueva solicitud de turno
    """
    pass


def cancelar_solicitud(request):
    """
        Solo para pacientes
    """
    pass


def listado_solicitudes(request):
    """
        listado de solicitudes de turno para un
        medico en particular
    """
    pass


def listado_solicitudes_pac(request):
    """
        listado de solicitudes de turnos q realizo un paciente
    """
    pass


def modificar_solicitud(request):
    """
        Modifica, confirmacion o cancelacion del turno solicitado
    """
    pass

