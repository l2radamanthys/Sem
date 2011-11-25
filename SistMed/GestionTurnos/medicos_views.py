#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    manejo de vistas de los pacientes
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth #para login
from django.contrib.auth.models import User#, Group

import datetime

from GestionTurnos.models import Medicos, TipoUsuario, Expecialidades, ExpecialidadesMedicos, HorarioAtencion
from utils import *
from constantes import MSJ_OK, MSJ_ERROR


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
            medico = Medicos(
                dni = int(get_POST_value(request,'dni','0','0')),
                tipo_doc = get_POST_value(request,'tipo_doc','',''),
                sexo = get_POST_value(request,'sexo','-','-'),
                telefono = request.POST.get('telefono', ''),
                direccion = request.POST.get('direccion', ''),
                tipo_usuario = TipoUsuario.objects.get(nombre__exact='Medico'),
                user = User.objects.get(username__exact=username),
                matricula = request.POST.get('matricula', '0'),
            )
            #guardamos
            medico.save()
            dict['med_id'] = medico.id
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


def borrar_medico(request, med_id=-1):
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
    plantilla = get_template('medicos/gestion_turnos/borrar.html')
    dict =  generar_base_dict(request)
    dict['titulo'] = 'Borrar Medico'

    med_id = int(med_id)

    if med_id != -1:
        medico = Medicos.objects.get(id=med_id)
        dict['query'] = True
        dict['nombre'] = medico.nombre_completo()
        dict['med_id'] = med_id

    else:
        dict['query'] = False
        dict['msj_class'] = MSJ_ERROR
        dict['mensaje'] = 'Error Datos Invalido'

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrado_medico(request, med_id=-1):
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
    plantilla = get_template('medicos/gestion_turnos/borrado.html')
    dict =  generar_base_dict(request)
    dict['titulo'] = 'Borrar Medico'

    med_id = int(med_id)

    if med_id != -1:
        medico = Medicos.objects.get(id=med_id)
        dict['query'] = True
        dict['nombre'] = medico.nombre_completo()

        ### borrar datos en cascada
        #especialidades
        ExpecialidadesMedicos.objects.filter(codigo_medico__id=med_id).delete()
        #cuenta
        medico.user.delete()
        #usuario
        #medico.delete()

    else:
        dict['query'] = False
        dict['msj_class'] = MSJ_ERROR
        dict['mensaje'] = 'Error Operacion No valida'

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def datos_medico(request, med_id=-1):
    """
        Muestra los Datos del Medico
    """
    plantilla = get_template('medicos/gestion_turnos/datos.html')
    dict = dict = generar_base_dict(request)
    dict['titulo'] = 'Datos Medico'

    med_id = int(med_id)
    if med_id != -1:
        medico = Medicos.objects.get(id=med_id)
        dict['med_id'] = med_id
        dict['username'] = medico.username()
        dict['nombre'] = medico.nombre_completo()
        dict['matricula'] = medico.matricula
        dict['direccion'] = medico.direccion
        dict['telefono'] = medico.telefono
        dict['email'] = medico.user.email
        dict['sexo'] = sexo_choice_expand(medico.sexo)
        dict["doc"] = medico.doc()

        especialidades = []
        band = True
        for especialidad in ExpecialidadesMedicos.objects.filter(codigo_medico__id=med_id):
            especialidades.append((especialidad.cod_expecialidad.nombre, get_field_css(band)))
            band = not(band)
        dict['especialidades'] = especialidades

        hrs_atencion = []
        band = True
        for h in HorarioAtencion.objects.filter(medico__id=med_id):
            hrs_atencion.append((get_field_css(band), date_choice_expand(h.dia), str(h.hora_inicio), str(h.hora_fin), h.medico.nombre_completo()))
            band = not(band)
        dict['horarios_atencion'] = hrs_atencion
        
    else:
        pass

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_medico(request, med_id=-1):
    """
        Vista de Selecion de Modificacion de Datos del Medico
    """
    plantilla = get_template('medicos/gestion_turnos/modificar.html')
    dict = dict = generar_base_dict(request)
    dict['titulo'] = 'Medico Modificar Datos'

    med_id = int(med_id)
    dict["med_id"] = med_id

    dict["tipo_doc"] = TIPO_DOC_CHOICE
    
    if med_id != -1:
        #### datos  -------------------
        medico = Medicos.objects.get(id=med_id)
        dict['med_name'] = medico.nombre_completo()

        dict['nombre'] = medico.user.first_name
        dict['apellido'] = medico.user.last_name
        dict['dni'] = medico.dni
        dict['matricula'] = medico.matricula
        dict['direccion'] = medico.direccion
        dict['telefono'] = medico.telefono
        dict['email'] = medico.user.email
        dict['sexo'] = medico.sexo

        #### especialidades -------------------
        especialidades_disp = [] #las q pueden ser agregadas
        especialidades_no_disp = [] #las q ya tiene el medico

        #esp no disponibles
        band = True
        for especialidad in ExpecialidadesMedicos.objects.filter(codigo_medico__id=med_id):
            especialidades_no_disp.append((especialidad.id, especialidad.cod_expecialidad.nombre,get_field_css(band)))
            band = not(band)

        #esp disponibles
        #nota esta parte no se sire la mejor implementacion pero almenos funciona jejej
        list = []

        ### turnos  -------------------
        dict['horas'] = [str(n).zfill(2) for n in range(24)]
        dict['minutos'] = [str(n).zfill(2) for n in range(60)]


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def guardar_cambios_medico(request):
    """
        parsea los datos enviados por la accion de un form de la vista
        medicos_modificar
    """
    plantilla = get_template('medicos/gestion_turnos/guardar.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Medico Modificar Datos'

    med_id = int(get_value(request, 'med_id', "-1", "-1"))
    dict['med_id'] = med_id
    query = int(get_value(request, 'query', "0", "0"))
    
    if med_id != -1 and query:
        #define q formulario envio la consulta
        action = get_value(request, 'action', "")
        medico = Medicos.objects.get(id=med_id)
        esp_id = int(get_POST_value(request,'especialidad',-1,-1))
        if esp_id != -1:
            especialidad = Expecialidades.objects.get(id=esp_id)
        
        if action == "datos":
            medico.user.first_name = get_POST_value(request,'nombre','')
            medico.user.last_name = get_POST_value(request,'apellido','')
            medico.user.save()
            medico.dni = int(get_POST_value(request,'dni','0','0'))
            medico.tipo_doc = get_POST_value(request,'tipo_doc','',''),
            medico.direccion = get_POST_value(request,'direccion','')
            medico.telefono = get_POST_value(request,'telefono','')
            medico.email = get_POST_value(request,'email','')
            medico.sexo = get_POST_value(request,'sexo','-','-')
            medico.save()

            dict['msj_class'] = MSJ_OK
            dict['mensaje'] = 'Datos Modificados Correctamente'

        #esta parte tiene problemas por claves duplicadas
        elif action == "especialidades":
            #esp_id = int(get_POST_value(request,'especialidad','-1','-1'))
            #especialidad = Expecialidades.objects.get(id=esp_id)

            #if not(ExpecialidadesMedicos.objects.filter(codigo_medico=med_id, cod_expecialidad=esp_id)):
            esp_x_med = ExpecialidadesMedicos(codigo_medico=medico, cod_expecialidad=especialidad)
            esp_x_med.save()
            dict['msj_class'] = MSJ_OK
            dict['mensaje'] = 'Se Asigno la Especialidad %s' %especialidad.nombre

            #else:
            #dict['msj_class'] = MSJ_ERROR
            #dict['mensaje'] = 'ERROR: No se puede asignar la Especialidad %s' %especialidad.nombre

        elif action == "turnos":
            #falta comprobacion para evitar posibles errores de solapamiento
            #de horarios en uns mismo dia
            dia = get_POST_value(request, 'dia', 'LUN', 'LUN')
            ini_hh = int(get_POST_value(request, 'hora_ini_hh', '0'))
            ini_mm = int(get_POST_value(request, 'hora_ini_mm', '0'))
            fin_hh = int(get_POST_value(request, 'hora_fin_hh', '0'))
            fin_mm = int(get_POST_value(request, 'hora_fin_mm', '0'))
            ini = datetime.time(ini_hh, ini_mm)
            fin = datetime.time(fin_hh, fin_mm)
            dur_turn = int(get_POST_value(request, 'turno', '0'))
            dur_inter = int(get_POST_value(request, 'intervalo', '0'))
            exp_id = int(get_POST_value(request, 'especialidad', '0'))
            #especialidad = Expecialidades.objects.get(id=exp_id)
            horario_atencion = HorarioAtencion(
                dia = dia,
                hora_inicio = ini,
                hora_fin = fin,
                duracion_turno = dur_turn,
                intervalo = dur_inter,
                cod_medico = medico,
                cod_expecialidad = especialidad
            )
            horario_atencion.save()
            dict['msj_class'] = MSJ_OK
            dict['mensaje'] = 'Horario de Atencion Agregado Correctamente'

        

    else:
        dict['msj_class'] = MSJ_ERROR
        dict['mensaje'] = "Parametros Invalidos %s %s" %(med_id, action)

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
            esp_id = get_POST_value(request,'especialidad','-1','-1')
            medico = Medicos.objects.get(id=med_id)
            especialidad = Expecialidades.objects.get(id=esp_id)

            #pregunto si la especialidade no fue asignada al medico
            if not(ExpecialidadesMedicos.objects.filter(codigo_medico=med_id, cod_expecialidad=esp_id)):
                #medico = Medicos.objects.get(id=med_id)
                esp_x_med = ExpecialidadesMedicos(codigo_medico=medico, cod_expecialidad=especialidad)
                esp_x_med.save()
                dict['msj_class'] = MSJ_OK
                dict['mensaje'] = 'Se Asigno la Especialidad %s' %especialidad.nombre

            else:
                dict['msj_class'] = MSJ_ERROR
                dict['mensaje'] = 'ERROR: No se puede asignar la Especialidad %s' %especialidad.nombre

        especialidades_disp = [] #las q pueden ser agregadas
        especialidades_no_disp = [] #las q ya tiene el medico

        #esp no disponibles
        band = True
        for especialidad in ExpecialidadesMedicos.objects.filter(codigo_medico__id=med_id):
            especialidades_no_disp.append((especialidad.id, especialidad.cod_expecialidad.nombre,get_field_css(band)))
            band = not(band)

        #esp disponibles
        #nota esta parte no se sire la mejor implementacion pero almenos funciona jejej
        list = []
        for espxmed in ExpecialidadesMedicos.objects.filter(codigo_medico__id=med_id):
            list.append(espxmed.cod_expecialidad.id)

        for esp in Expecialidades.objects.exclude(id__in = list).order_by('nombre'):
            especialidades_disp.append((esp.id, esp.nombre))

        dict['med_exp'] = especialidades_no_disp
        dict['especialidades'] = especialidades_disp

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrar_expecialidad(request):
    """
        Desasigna una especialidar asignada al medico
    """
    plantilla = get_template('medicos/gestion_turnos/borrar-especialidad.html')
    dict = dict = generar_base_dict(request)
    dict['sin_titulo'] = True

    exp_med_id = int(get_GET_value(request, "exp_med_id", -1))

    especialidad = ExpecialidadesMedicos.objects.get(id=exp_med_id)
    dict["nombre"] = especialidad.cod_expecialidad.nombre
    dict["med_id"] = especialidad.codigo_medico.id
    especialidad.delete()
    
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def agregar_horario_atencion(request, med_id=-1):
    """
    """
    plantilla = get_template('medicos/gestion_turnos/agregar-dia-atencion.html')
    dict = dict = generar_base_dict(request)
    dict['titulo'] = 'Medico - Agregar Dia Atencion'

    query = int(request.POST.get('query', '0'))
    dict['query'] = query
    #id pasado por parametro
    med_id = int(med_id)

    if med_id != -1:
        _medico = Medicos.objects.get(id=med_id)
        dict['med_name'] = _medico.nombre_completo()

        dict['horas'] = [str(n).zfill(2) for n in range(24)]
        dict['minutos'] = [str(n).zfill(2) for n in range(60)]

        especialidades = []
        for esp in ExpecialidadesMedicos.objects.filter(codigo_medico__id=med_id):
            especialidades.append((esp.cod_expecialidad.id, esp.cod_expecialidad.nombre))
        dict['especialidades'] = especialidades

        if query: #si se envio un form 
            #falta comprobacion para evitar posibles errores de solapamiento
            #de horarios en uns mismo dia
            dia = get_POST_value(request, 'dia', 'LUN', 'LUN')
            ini_hh = int(get_POST_value(request, 'hora_ini_hh', '0'))
            ini_mm = int(get_POST_value(request, 'hora_ini_mm', '0'))
            fin_hh = int(get_POST_value(request, 'hora_fin_hh', '0'))
            fin_mm = int(get_POST_value(request, 'hora_fin_mm', '0'))
            ini = datetime.time(ini_hh, ini_mm)
            fin = datetime.time(fin_hh, fin_mm)
            dur_turn = int(get_POST_value(request, 'turno', '0'))
            dur_inter = int(get_POST_value(request, 'intervalo', '0'))
            
            horario_atencion = HorarioAtencion(
                dia = dia,
                hora_inicio = ini,
                hora_fin = fin,
                duracion_turno = dur_turn,
                intervalo = dur_inter,
                medico = _medico,
            )
            horario_atencion.save()
            dict['msj_class'] = MSJ_OK
            dict['mensaje'] = 'Horario de Atencion Agregado Correctamente'

        else:
            pass

        hrs_atencion = []
        band = True
        for h in HorarioAtencion.objects.filter(medico__id=med_id):
            hrs_atencion.append([get_field_css(band), date_choice_expand(h.dia), str(h.hora_inicio), str(h.hora_fin), h.medico.nombre_completo()])
            #band = not(band)
        dict['horarios_atencion'] = hrs_atencion
        
    else:
        pass

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)
   

def mostrar_dias_atencion(request, med_id=-1):
    """
    """
    pass


def buscar_medicos(request):
    """
        Permite Buscar un admin por nombre, apellido o usuario

        pueden acceder
        --------------
        - administrativos
        - medicos

        sin acceso
        ----------
        - admins
        - usuarios no registrados
    """
    plantilla = get_template('medicos/gestion_turnos/buscar.html')
    dict = generar_base_dict(request)
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
                medicos = Medicos.objects.filter(user__username__icontains=buscar_text)

            elif buscar_por == 1:
                medicos = Medicos.objects.filter(user__first_name__icontains=buscar_text)

            elif buscar_por == 2:
                medicos = Medicos.objects.filter(user__last_name__icontains=buscar_text)

        #si se ingreso text en blanco pongo todos
        else:
            medicos = Medicos.objects.all()


        _medicos = []
        band = True
        for med in medicos:
            id = med.id
            username = med.user.username
            nombre = med.nombre_completo()
            css = get_field_css(band)
            band = not(band)
            _medicos.append([id, username, nombre, css])
        dict['medicos'] = _medicos

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)

