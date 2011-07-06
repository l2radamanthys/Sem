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
        hist_clinica = InformacionBasica.objects.create(
                    paciente = Pacientes.objects.get(id=int(get_value(request, 'pac_id'))),
                    fecha_nacimiento = date_split(get_value(request, 'fecha_nac', "01/01/01")), 
                    lugar_nacimiento = get_value(request, 'lugar_nac', ""), 
                    grupo_sanguineo = get_value(request, 'grupo_sanguineo', "--"), 
                    padre = get_value(request, 'padre', ""),
                    madre = get_value(request, 'madre', ""),
                    obra_social = get_value(request, 'obra_social', ""),
                    nro_afiliado = get_value(request, 'nro_afiliado', ""),
                    estado_civil = get_value(request, 'estado_civil', "-"), 
                    ocupacion = get_value(request, 'ocupacion', "-"), 
                    religion = get_value(request, 'religion', "-"), 
                    motivo_consulta = get_value(request, 'motivo_consulta', "-")
        )#guarda automaticament
        dict['msj_class'] = MSJ_OK
        dict['mensaje'] = 'Historia Clinica Creada'
        
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


def mostrar_datos_paciente(request, pac_id=-1):
    """
        
    """
    plantilla = get_template('medicos/historia_clinica/mostrar-datos-base.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica' 
    
    pac_id = int(pac_id)
    if pac_id != -1:
        _paciente = Pacientes.objects.get(id=pac_id)
        hist_clinica = InformacionBasica.objects.get(paciente=_paciente)
        
        dict["nombre"] = _paciente.nombre_completo()
        dict["DNI"] = _paciente.dni
        dict["lugar_nacimiento"] = hist_clinica.lugar_nacimiento
        dict["padre"] = hist_clinica.padre
        dict["madre"] = hist_clinica.madre
        dict["obra_social"] = hist_clinica.obra_social
        dict["nro_afiliado"] = hist_clinica.nro_afiliado
        dict["sexo"] = sexo_choice_expand(_paciente.sexo)
        dict["grupo_sanguineo"] = hist_clinica.grupo_sanguineo
              
    
    
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)

