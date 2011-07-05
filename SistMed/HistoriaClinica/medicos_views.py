#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth #para login
from django.contrib.auth.models import User

import datetime

from GestionTurnos.models import Pacientes
from HistoriaClinica.models import *
from utils import *
from constantes import *



def nueva(request):
    """
        cargar datos base para nueva historia clinica
    """
    plantilla = get_template('medicos/historia_clinica/nueva.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Nuevo Medico'

    #si se realizo una consulta
    query = int(request.POST.get('query', '0'))
    dict['query'] = query

    if query:
        _paciente = Pacientes.objects.get(id=int(get_value(request, 'pac_id')))
        fecha_nac = date_split(get_value(request, 'fecha_nac', "01/01/01"))
        lugar_nac = date_split(get_value(request, 'lugar_nac', ""))
        grupo_sang = get_value(request, 'grupo_sanguineo', "--")
        est_civil = get_value(request, 'estado_civil', "-")
        _ocupacion = get_value(request, 'ocupacion', "-")
        _religion = get_value(request, 'religion', "-")
        motivo = get_value(request, 'motivo_consulta', "-")
        
        hist_clinica = InformacionBasica.objects.create(
                    paciente = _paciente, 
                    fecha_nacimiento = fecha_nac, 
                    lugar_nacimiento = lugar_nac, 
                    grupo_sanguineo = grupo_sang, 
                    estado_civil = est_civil, 
                    ocupacion = _ocupacion, 
                    religion = _religion, 
                    motivo_consulta = motivo
        )

    pacientes = []
    #mas adelante tengo q hacer un filtrado d datos...
    for pac in Pacientes.objects.all():
        pacientes.append((pac.id, pac.nombre_completo()))

    #en caso de no haber pacientes disponibles lanza error
    if len(pacientes) == 0:
        return HttpResponseRedirect('/error/$title="Invalid Request"&msj="no hay pacientes disponibles"')

    dict['pacientes'] = pacientes

    dict['grupos_sanguineos'] = GRUPOS_SANGUINEOS

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def mostrar_datos_paciente(request):
    """
        
    """
    
