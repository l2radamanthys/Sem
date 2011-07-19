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


def listado_pacientes(request):
    """
        
    """
    plantilla = get_template('medicos/historia_clinica/listado-pacientes.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Listado Historias Clinicas'

    pacientes = []
    
    for info in InformacionBasica.objects.all():
        pacientes.append([info.paciente.id, info.paciente.nombre_completo()])
    
    dict['pacientes'] = pacientes
    
    
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)



def mostrar_datos_paciente(request, pac_id=-1):
    """
        
    """
    plantilla = get_template('medicos/historia_clinica/mostrar-datos-base.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica' 

    #if pac_id != "":
    #    pac_id = int(pac_id)
    #else:
    #    pac_id = -1
    #if pac_id == -1: #no es necesario
    #    pac_id = int(request.session.get('hc_pac_id', -1))
    
    #if pac_id != -1:
    if pac_id != "" and pac_id != -1:
        pac_id = int(pac_id)
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
        dict['pac_id'] = pac_id
              
        #grabamo en la session el id del paciente
        #request.session['hc_pac_id'] = pac_id #no es necesario
                      
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def mostrar_antecedentes_perinatales(request, pac_id=-1):
    """

    """
    plantilla = get_template('medicos/historia_clinica/mostrar-antece-perinatales.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    if pac_id != "" and pac_id != -1:
        pac_id = int(pac_id)
        _paciente = Pacientes.objects.get(id=pac_id)
        hist_clinica = InformacionBasica.objects.get(paciente=_paciente)

        dict['pac_id'] = pac_id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)



#vacunas
def agregar_vacuna(request, pac_id=-1):
    """
    """
    plantilla = get_template('medicos/historia_clinica/agregar-vacuna.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    if pac_id != "" and pac_id != -1:
        pac_id = int(pac_id)
        _paciente = Pacientes.objects.get(id=pac_id)
        h_clinica = InformacionBasica.objects.get(paciente=_paciente)

        vac = Vacuna.objects.create(
            hist_clinica=h_clinica,
            fecha=date_split(get_value(request, 'fecha', '01/01/1900')),
            descripcion=get_value(request, 'descripcion', ''),
            tipo_dosis=get_value(request, 'tipo_dosis', '')
        )


    dict['tipo_dosis'] = TIPO_DOSIS_CHOICE

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listado_vacunas(request, pac_id=-1):
    """
        Muestra el listado de vacunacion al estilo carnet jaja
    """
    plantilla = get_template('medicos/historia_clinica/listado-vacunas.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    if pac_id != "" and pac_id != -1:
        pac_id = int(pac_id)
        _paciente = Pacientes.objects.get(id=pac_id)
        _hist_clinica = InformacionBasica.objects.get(paciente=_paciente)
        #vacunas = Vacuna.objects.filter(hist_clinica=_hist_clinica)

        list_vac = []
        for vac in Vacuna.objects.filter(hist_clinica=_hist_clinica):
            list_vac.append([vac.id, date_to_str(vac.fecha), vac.descripcion, TIPO_DOSIS_DIC.get(vac.tipo_dosis, 'ERROR'), field_css(vac.id)])

        dict['vacunas'] = list_vac
        dict['pac_id'] = pac_id
        
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_vacuna(request, pac_id=-1):
    """
    """
    plantilla = get_template('medicos/historia_clinica/mostrar-antece-perinatales.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrar_vacuna(request, pac_id=-1):
    """
    """
    plantilla = get_template('medicos/historia_clinica/mostrar-antece-perinatales.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)