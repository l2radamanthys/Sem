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
        return HttpResponseRedirect('/error/?title="Invalid Request"&msj="no hay pacientes disponibles"')

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
        pacientes.append([info.paciente.id, info.paciente.nombre_completo(), field_css(info.paciente.id)])
    
    dict['pacientes'] = pacientes
    
    
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)



def mostrar_datos_paciente(request):
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
    
    pac_id = get_GET_value(request, "pac_id", -1)
    if pac_id != "" and pac_id != -1:
        pac_id = int(pac_id)
        _paciente = Pacientes.objects.get(id=pac_id)
        hist_clinica = InformacionBasica.objects.get(paciente=_paciente)
        
        dict["nombre"] = _paciente.nombre_completo()
        dict["DNI"] = _paciente.dni
        dict['fecha_nacimiento'] =  hist_clinica.fecha_nacimiento
        dict["lugar_nacimiento"] = hist_clinica.lugar_nacimiento
        dict["padre"] = hist_clinica.padre
        dict["madre"] = hist_clinica.madre
        dict["obra_social"] = hist_clinica.obra_social
        dict["nro_afiliado"] = hist_clinica.nro_afiliado
        dict["sexo"] = sexo_choice_expand(_paciente.sexo)
        dict["grupo_sanguineo"] = hist_clinica.grupo_sanguineo
        dict['estado_civil'] = estado_civil_expand(hist_clinica.estado_civil)
        dict['pac_id'] = pac_id
        

        #grabamo en la session el id del paciente
        #request.session['hc_pac_id'] = pac_id #no es necesario
                      
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_datos_paciente(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/modificar-datos-base.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    pac_id = int(get_GET_value(request, "pac_id", -1))
    query = int(request.POST.get('query', '0'))
    dict['query'] = query

    if pac_id != "" and pac_id != -1:
        #pac_id = int(pac_id)
        
        

        pac = Pacientes.objects.get(id=pac_id)
        dict['pac_nombre'] = pac.nombre_completo()
        dict['pac_dni'] = pac.dni
        hist_clinica = InformacionBasica.objects.get(paciente=pac)

        if query:
            hist_clinica.lugar_nacimiento = get_value(request, 'lugar_nac', "")
            hist_clinica.fecha_nacimiento = date_split(get_value(request, 'fecha_nac', ""))
            hist_clinica.grupo_sanguineo = get_value(request, 'grupo_sanguineo', "--")
            hist_clinica.padre = get_value(request, 'padre', "")
            hist_clinica.madre = get_value(request, 'madre', "")
            hist_clinica.obra_social = get_value(request, 'obra_social', "")
            hist_clinica.nro_afiliado = get_value(request, 'nro_afiliado', "")
            hist_clinica.estado_civil = get_value(request, 'estado_civil', "-")
            hist_clinica.ocupacion = get_value(request, 'ocupacion', "-")
            hist_clinica.religion = get_value(request, 'religion', "-")
            hist_clinica.save()

            dict['msj_class'] = MSJ_OK
            dict['mensaje'] = 'Datos Modificados...'

        dict['hc'] = hist_clinica
        dict['pac_id'] = pac_id
        dict['grupos_sanguineos'] = GRUPOS_SANGUINEOS
        

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


### - Antecedentes perinatales - ###
def mostrar_antecedentes_perinatales(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/mostrar-antece-perinatales.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    pac_id = get_GET_value(request, "pac_id", -1)
    if pac_id != "" and pac_id != -1:
        pac_id = int(pac_id)
        _paciente = Pacientes.objects.get(id=pac_id)
        hist_clinica = InformacionBasica.objects.get(paciente=_paciente)

        dict['pac_id'] = pac_id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_antecedentes_perinatales(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/modificar-antece-perinatales.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    pac_id = get_GET_value(request, "pac_id", -1)
    if pac_id != "" and pac_id != -1:
        pac_id = int(pac_id)
        _paciente = Pacientes.objects.get(id=pac_id)
        hist_clinica = InformacionBasica.objects.get(paciente=_paciente)

        dict['pac_id'] = pac_id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


### - Vacunas - ###
def agregar_vacuna(request, pac_id=-1):
    """
    """
    plantilla = get_template('medicos/historia_clinica/agregar-vacuna.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    query = int(request.POST.get('query', '0'))
    dict['query'] = query


    if pac_id != "" and pac_id != -1 and query:
        pac_id = int(pac_id)
        _paciente = Pacientes.objects.get(id=pac_id)
        h_clinica = InformacionBasica.objects.get(paciente=_paciente)

        vac = Vacuna.objects.create(
            hist_clinica=h_clinica,
            fecha=date_split(get_value(request, 'fecha', '01/01/1900')),
            descripcion=get_value(request, 'descripcion', ''),
            tipo_dosis=get_value(request, 'tipo_dosis', '')
        )
        dict['msj_class'] = MSJ_OK
        dict['mensaje'] = 'Vacuna Agregada'


    dict['tipo_dosis'] = TIPO_DOSIS_CHOICE
    dict['pac_id'] = pac_id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listado_vacunas(request):
    """
        Muestra el listado de vacunacion al estilo carnet jaja
    """
    plantilla = get_template('medicos/historia_clinica/listado-vacunas.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    pac_id = get_GET_value(request, "pac_id", -1)
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


def modificar_vacuna(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/modificar-vacuna.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    query = int(request.POST.get('query', '0'))
    dict['query'] = query

    pac_id = get_GET_value(request, "pac_id", -1)
    vac_id = get_GET_value(request, "vac_id", -1)
    if pac_id != -1 and vac_id != -1:
        vacuna = Vacuna.objects.get(id=vac_id)
        dict['vacuna'] = vacuna
        dict['tipo_dosis'] = TIPO_DOSIS_CHOICE

        if query:
            vacuna.fecha = date_split(get_value(request, 'fecha', '01/01/1900'))
            vacuna.descripcion = get_value(request, 'descripcion', '')
            vacuna.tipo_dosis = get_value(request, 'tipo_dosis', '')
            vacuna.save()

            dict['msj_class'] = MSJ_OK
            dict['mensaje'] = 'Cambios Modificados'

    dict['pac_id'] = pac_id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrar_vacuna(request):
    """
    """
    pac_id = get_GET_value(request, "pac_id", -1)
    vac_id = get_GET_value(request, "vac_id", -1)
    if pac_id != -1 and vac_id != -1:
        vacuna = Vacuna.objects.get(id=vac_id)
        vacuna.delete()
        return HttpResponseRedirect("/historia-clinica/listado-vacunas/?pac_id=%s" %pac_id)
    else:
        return HttpResponseRedirect('/error/?title="Invalid Request"&msj="Parametros invalidos..."')


### - Examen Fisico - ###
def nuevo_examen_base(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/examen_fisico/nuevo-examen-base.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'
    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)
    
    dict["date_hoy"] = date_today_str()
    
    query = int(get_value(request, "query", 0))
    dict["query"] = query
 
    if pac_id != "" and pac_id != -1 and query:
        h_clinica = InformacionBasica.objects.get(paciente=Pacientes.objects.get(id=pac_id))
        examen = ExamenBase(
            hist_clinica = h_clinica,
            fecha = date_split(get_value(request, "fecha", "01/01/2000")),
            temp_corporal = float(get_value(request, "temp_corporal", "0.0")),
            pres_art_sist = int(get_value(request, "pres_art_sist", "0")),
            pres_art_diast = int(get_value(request, "pres_art_diast", "0")),
            frec_respiratoria = int(get_value(request, "frec_respiratoria", "0")),
            pulso = int(get_value(request, "pulso", "0")),
            peso_medio = float(get_value(request, "peso_medio", "0.0")),
            altura_media = float(get_value(request, "altura_media", "0.0")),
            peso = float(get_value(request, "peso", "0.0")),
            altura = float(get_value(request, "altura", "0.0")),
            talla = get_value(request, "talla", "0.0"),
            bmi = float(get_value(request, "bmi", "0.0")),
            imprecion_general = get_value(request, "imprecion_general", "")
        )
        examen.save()
        
        dict["msj_class"] = "msj_ok"
        dict["mensaje"] = "Examen Fisico Agregado"

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listado_examenes_fisicos(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/examen_fisico/listado.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    examenes = []
    _paciente = Pacientes.objects.get(id=pac_id)
    hc = InformacionBasica.objects.get(paciente=_paciente)
    for exam in ExamenBase.objects.filter(hist_clinica=hc):
        examenes.append([exam.id, exam])
    dict["examenes"] = examenes

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def mostrar_examen_base(request):
    plantilla = get_template('medicos/historia_clinica/examen_fisico/mostrar-examen-base.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Examen Fisico'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    exam_id = int(get_GET_value(request, "exam_id", -1))
    dict["exam_id"] = exam_id

    examen = ExamenBase.objects.get(id=exam_id)
    dict["examen"] = examen

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def mostrar_examen_cardio_vascular(request):
    plantilla = get_template('medicos/historia_clinica/examen_fisico/mostrar-examen-cardio-vascular.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Examen Fisico'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    exam_id = int(get_GET_value(request, "exam_id", -1))
    dict["exam_id"] = exam_id

    eb = ExamenBase.objects.get(id=exam_id)
    #model no implementado

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def mostrar_examen_aparato_respiratorio(request):
    plantilla = get_template('medicos/historia_clinica/examen_fisico/mostrar-examen-aparato-respiratorio.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Examen Fisico'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    exam_id = int(get_GET_value(request, "exam_id", -1))
    dict["exam_id"] = exam_id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def mostrar_examen_cabeza(request):
    plantilla = get_template('medicos/historia_clinica/examen_fisico/mostrar-examen-cabeza.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Examen Fisico'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    exam_id = int(get_GET_value(request, "exam_id", -1))
    dict["exam_id"] = exam_id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def mostrar_examen_cuello(request):
    plantilla = get_template('medicos/historia_clinica/examen_fisico/mostrar-examen-cuello.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Examen Fisico'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    exam_id = int(get_GET_value(request, "exam_id", -1))
    dict["exam_id"] = exam_id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def mostrar_imagenes(request):
    plantilla = get_template('medicos/historia_clinica/examen_fisico/mostrar-imagenes.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Examen Fisico'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    exam_id = int(get_GET_value(request, "exam_id", -1))
    dict["exam_id"] = exam_id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def mostrar_analisis_lab(request):
    plantilla = get_template('medicos/historia_clinica/examen_fisico/mostrar-analisis-lab.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Examen Fisico'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    exam_id = int(get_GET_value(request, "exam_id", -1))
    dict["exam_id"] = exam_id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


### - Consultas Medicas - ###
def listado_consultas_medicas(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/consultas_medicas/listado-consultas-medicas.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = pac_id

    consultas = ConsultaMedica.objects.all();
    dict["consultas"] = consultas

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def nueva_consulta_medica(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/consultas_medicas/nueva-consulta-medica.html')
    dict = generar_base_dict(request)
    dict['sin_titulo'] = True #'Historia Clinica'
    pac_id = int(get_GET_value(request, "pac_id", -1))
    dict['pac_id'] = pac_id

    dict["fecha_hoy"] = date_today_str()

    medicos = Medicos.objects.all()
    dict["medicos"] = medicos

    if dict['nivel_2'] and not(dict['nivel_3']):
        dict["med_name"] = Medicos.objects.get(id=dict['user_id']).nombre_completo()

    dict['pac_name'] = Pacientes.objects.get(id=pac_id).nombre_completo()

    query = int(get_value(request, "query", 0))
    dict["query"] = query
    if query:
        pac_id = int(get_value(request, "pac_id", 0))
        dict['pac_id'] = pac_id
        pac = Pacientes.objects.get(id=pac_id)
        med_id = int(get_value(request, 'med_id', -1))
        if med_id != -1:
            med = Medicos.objects.get(id=med_id)
        else:
            med = Medicos.objects.get(id=dict['user_id'])

        consulta = ConsultaMedica(
            hist_clinica = InformacionBasica.objects.get(paciente=pac),
            fecha = date_split(get_value(request, "fecha", "")),
            observaciones = get_value(request, "observaciones", "<none>"),
            medico = med
        )
        consulta.save()

        dict["msj_class"] = "msj_ok"
        dict["mensaje"] = "Consulta Medica Agregada"


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def mostrar_consulta_medica(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/consultas_medicas/mostrar-consulta-medica.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = pac_id
    
    cons_id = int(get_GET_value(request, "cons_id", -1))
    dict["consulta"] = ConsultaMedica.objects.get(id=cons_id)


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)