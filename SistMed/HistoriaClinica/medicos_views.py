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


#nueva HC
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

    #forma basica de filtrado
    con_hc = []
    for hc in InformacionBasica.objects.all():
        con_hc.append(hc.paciente.id)

    for pac in Pacientes.objects.exclude(id__in=con_hc):
        pacientes.append((pac.id, pac.nombre_completo()))

    #en caso de no haber pacientes disponibles lanza error
    if len(pacientes) == 0:
        return HttpResponseRedirect('/error/?title="Invalid Request"&msj="Actulmente todos los Pacientes tienen asignada una Historia Clinica"')

    dict["hoy"] = date_today_str()
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
        hist_clinica = InformacionBasica.objects.get(paciente__id=pac_id)
        
        dict["nombre"] = _paciente.nombre_completo()
        dict["doc"] = _paciente.doc()
        dict['fecha_nacimiento'] =  date_to_str(hist_clinica.fecha_nacimiento)
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
        pac = Pacientes.objects.get(id=pac_id)
        dict['pac_nombre'] = pac.nombre_completo()
        dict['pac_dni'] = pac.dni
        hist_clinica = InformacionBasica.objects.get(paciente__id=pac_id)

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

    pac_id = int(get_GET_value(request, "pac_id", -1))
    dict['pac_id'] = pac_id
    
    if pac_id != -1:
        try:
            dict["antecedentes"] = AntecedentesPerinatales.objects.get(hist_clinica__paciente__id=pac_id)
        except:
            dict["antecedentes"] = False

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_antecedentes_perinatales(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/modificar-antece-perinatales.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    pac_id = int(get_GET_value(request, "pac_id", -1))
    dict['pac_id'] = pac_id
    
    if pac_id != -1:
        try:
            dict["antecedentes"] = AntecedentesPerinatales.objects.get(hist_clinica__paciente__id=pac_id)
        except:
            dict["antecedentes"] = False


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def agregar_antecedentes_perinatales(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/agregar-antece-perinatales.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    pac_id = int(get_GET_value(request, "pac_id", -1))
    dict['pac_id'] = pac_id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)



### - Vacunas - ###
def agregar_vacuna(request, pac_id=-1):
    """
    """
    plantilla = get_template('medicos/historia_clinica/vacunas/agregar-vacuna.html')
    dict = generar_base_dict(request)
    dict['sin_titulo'] = True #'Historia Clinica'

    query = int(request.POST.get('query', '0'))
    dict['query'] = query


    if pac_id != "" and pac_id != -1 and query:
        pac_id = int(pac_id)
        h_clinica = InformacionBasica.objects.get(paciente__id=pac_id)

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
    plantilla = get_template('medicos/historia_clinica/vacunas/listado-vacunas.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Historia Clinica'

    pac_id = get_GET_value(request, "pac_id", -1)
    if pac_id != "" and pac_id != -1:
        pac_id = int(pac_id)
        list_vac = []
        for vac in Vacuna.objects.filter(hist_clinica__paciente__id=pac_id):
            list_vac.append([vac.id, date_to_str(vac.fecha), vac.descripcion, TIPO_DOSIS_DIC.get(vac.tipo_dosis, 'ERROR'), field_css(vac.id)])

        dict['vacunas'] = list_vac
        dict['pac_id'] = pac_id
        
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_vacuna(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/vacunas/modificar-vacuna.html')
    dict = generar_base_dict(request)
    dict['sin_titulo'] = True #'Historia Clinica'

    query = int(request.POST.get('query', '0'))
    dict['query'] = query

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    vac_id = int(get_GET_value(request, "vac_id", -1))
    if vac_id != -1:
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

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrar_vacuna(request):
    """
    """
    plantilla = get_template('medicos/historia_clinica/vacunas/borrar-vacuna.html')
    dict = generar_base_dict(request)
    dict['sin_titulo'] = True #'Historia Clinica'

    pac_id = get_GET_value(request, "pac_id", -1)
    vac_id = int(get_GET_value(request, "vac_id", -1))
    if pac_id != -1 and vac_id != -1:
        vacuna = Vacuna.objects.get(id=vac_id)
        dict["nombre"] = vacuna.descripcion + " - " + vacuna.tipo_dosis
        dict["pac_id"] = pac_id
        dict["query"] = True
        vacuna.delete()

        contexto = Context(dict)
        html = plantilla.render(contexto)
        return HttpResponse(html)

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
        h_clinica = InformacionBasica.objects.get(paciente__id=pac_id)
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
    for exam in ExamenBase.objects.filter(hist_clinica__paciente__id=pac_id):
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

    eb = ExamenBase.objects.get(id=exam_id)
    
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

    #eb = ExamenBase.objects.get(id=exam_id)
    try:
        examen = Cabeza.objects.get(examen_fisico__id=exam_id)
        dict["examen"] = examen
    except:
        dict["examen"] = False

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def nuevo_examen_cabeza(request):
    plantilla = get_template('medicos/historia_clinica/examen_fisico/nuevo-examen-cabeza.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Examen Fisico'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    exam_id = int(get_GET_value(request, "exam_id", -1))
    dict["exam_id"] = exam_id

    query = int(get_value(request, "query", 0))
    dict["query"] = query
    if query:

        eb = ExamenBase.objects.get(id=exam_id)
        exa_cabeza = Cabeza(
            examen_fisico = eb,
            craneo = get_value(request, "craneo", '-'),
            fontanelas_y_suturas = get_value(request, "font_y_sut", '-'),
            facie = get_value(request, "facie", '-'),
            parpados = get_value(request, "parpados", '-'),
            conjuntivas =  get_value(request, "conjuntivas", '-'),
            globo_ocular_mov = get_value(request, "ojo_mov", '-'),
            vision = get_value(request, "vision", '-'),
            nariz_fosas_nasales = get_value(request, "nariz", '-'),
            labios = get_value(request, "labios", '-'),
            dientes = get_value(request, "dientes", '-'),
            lengua = get_value(request, "lengua", '-'),
            mucosa_bucofaringea = get_value(request, "mucosa_buco_far", 0),
            amigdalas = get_value(request, "amigdalas", '-'),
            pabellones_auriculares = get_value(request, "pab_aur", '-'),
            cond_audit_externo = get_value(request, "cond_aud_ext", '-'),
            timpanos = get_value(request, "timpanos", '-'),
            audicion = get_value(request, "audicion", '-'),
            observaciones = get_value(request, "observaciones", '-'),
        )
        exa_cabeza.save()
        dict["msj_class"] = "msj_ok"
        dict["mensaje"] = "Examen Cabeza Agregado"

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

    try:
        examen = Cuello.objects.get(examen_fisico__id=exam_id)
        dict["examen"] = examen
    except:
        dict["examen"] = False

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def nuevo_examen_cuello(request):
    plantilla = get_template('medicos/historia_clinica/examen_fisico/nuevo-examen-cuello.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Examen Fisico'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    exam_id = int(get_GET_value(request, "exam_id", -1))
    dict["exam_id"] = exam_id

    query = int(get_value(request, "query", 0))
    dict["query"] = query
    if query:
        eb = ExamenBase.objects.get(id=exam_id)
        cuello = Cuello(
            examen_fisico = eb,
            inspecion = get_value(request, "inspecion", '-'),
            palpacion = get_value(request, "palpacion", '-'),
            percucion = get_value(request, "percucion", '-'),
            ausculacion = get_value(request, "ausculacion", '-'),
            observaciones = get_value(request, "observaciones", '-'),
        )
        cuello.save()
        
        dict["msj_class"] = "msj_ok"
        dict["mensaje"] = "Examen de Cuello Agregado"

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

    dict["imagenes"] = Imagen.objects.filter(examen_fisico__id=exam_id)

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def mostrar_imagen(request):
    """
        Visualiza una imagen
    """
    plantilla = get_template('medicos/historia_clinica/examen_fisico/mostrar-imagen.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Examen Fisico'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    exam_id = int(get_GET_value(request, "exam_id", -1))
    dict["exam_id"] = exam_id

    img_id = int(get_GET_value(request, "img_id", -1))
    dict["imagen"] = Imagen.objects.get(id=img_id)

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def agregar_imagen(request):
    plantilla = get_template('medicos/historia_clinica/examen_fisico/agregar-imagen.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Examen Fisico'

    pac_id = get_GET_value(request, "pac_id", -1)
    dict['pac_id'] = int(pac_id)

    exam_id = int(get_GET_value(request, "exam_id", -1))
    dict["exam_id"] = exam_id

    query = int(get_value(request, "query", 0))
    dict["query"] = query
    if query:
        eb = ExamenBase.objects.get(id=exam_id)
        img = Imagen(
            examen_fisico = eb,
            titulo = get_value(request, "titulo", "<None>"),
            descripcion = get_value(request, "descripcion", "<None>"),
            imagen = request.FILES["imagen"]
        )
        img.save()

        dict["msj_class"] = "msj_ok"
        dict["mensaje"] = "Imagen Agregada"

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)



def mostrar_analisis_lab(request):
    plantilla = get_template('medicos/historia_clinica/examen_fisico/agregar-imagen.html')
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



