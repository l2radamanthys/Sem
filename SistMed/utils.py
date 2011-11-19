#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    listado de Funciones de Utilidad extendida
"""
import datetime
import time

from constantes import *


def get_field_css(band=True):
    """
        Retorna el nombre de la clases CSS correspondiente a la fila
        dependiendo del valor pasado por 'band'
    """
    if band:
        return "field_a"
    else:
        return "field_b"


def field_css(value):
    """
    """
    return get_field_css(value % 2)



def date_choice_expand(key):
    """
        Expande el identificador del choice dia
    """
    return DATE_CHOICE_DIC[key]


def sexo_choice_expand(key):
    """
        Expande el identificador del choice sexo
    """
    return SEXO_CHOICE_DIC[key]


def estado_civil_expand(key):
    return ESTADO_CIVIL_DIC[key]


def estado_solicitud_expand(key):
    return SOLICITUD_ESTADO_CHOICE_DIC[key.upper()]


def get_GET_value(request, key='', default='', blank=''):
    value = request.GET.get(key, default)
    if value == '':
        value = blank
    return value


def get_POST_value(request, key='', default='', blank=''):
     value = request.POST.get(key, default)
     if value == '':
        value = blank
     return value


def get_value(request=None, key='', default='', blank='', method=POST):
    """
        Obtiene valor de object request por los metodos POST/GET
    """
    if method == POST:
        return get_POST_value(request, key, default, blank)
    else:
        return get_GET_value(request, key, default, blank)


def generar_base_dict(request):
    """
        Genera el dicionario con la Info Basica
    """
    dict = BASE_DIC.copy()
    #usuario estado
    opc = request.session.get('area', "True")
    if opc == "True":
        opc = True
    else:
        opc = False
    dict['menu_area'] = opc
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
        dict['user_autenticado'] = True
        #nombre de usuario y rol del mismo
        dict['user'] = request.session.get('usuario', '')
        dict['user_id'] = request.session.get('usuario_id', '-1')
        #dict['user_rol'] = request.session.get('usuario_rol', '')
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'
        #request.session['usuario'] = ''
        #request.session['usuario_rol'] = ''
        dict['user'] = 'offline'
        dict['user_id'] = '-1'
        #dict['user_rol'] = ''
        dict['user_autenticado'] = False

    dict = insert_permisos_key(request, dict)
    return dict


def insert_permisos_key(request, dict):
    """
        define las variables de permisos

        - no registrado nivel_0
        - pacientes hasta nivel 1
        - medicos hasta nivel 2
        - admins hasta nivel 3

    """

    if request.session.get('usuario', '') == "admin":
        dict["super_admin"] = True
    else:
        dict["super_admin"] = False

    rol = request.session.get('usuario_rol', 'Anonimo')
    dict["user_rol"] = rol
    if rol == ANONIMO:
        dict['nivel_0'] = True
        dict['nivel_1'] = False
        dict['nivel_2'] = False
        dict['nivel_3'] = False

    elif rol == PACIENTE:
        dict['nivel_0'] = False
        dict['nivel_1'] = True
        dict['nivel_2'] = False
        dict['nivel_3'] = False

    elif rol == MEDICO:
        dict['nivel_0'] = False
        dict['nivel_1'] = True
        dict['nivel_2'] = True
        dict['nivel_3'] = False

    elif rol == ADMINISTRATIVO:
        dict['nivel_0'] = False
        dict['nivel_1'] = True
        dict['nivel_2'] = True
        dict['nivel_3'] = True

    return dict


def date_split(cad="01/01/1900"):
    """
        comvierte la cadena de texto en un objecto datetime
    """
    list = [int(n) for n in cad.split("/")]
    list.reverse()
    if len(list) == 3: # ejem 01/01/1920 completo
        fecha = datetime.datetime(year=list[0], month=list[1], day=list[2])
    elif len(list) == 2: # ejem 01/03 falta el anio por lo tanto anio=0 -.-
        fecha = datetime.datetime(year=0, month=list[0], day=list[1])
    return fecha


def time_split(str="00:00:00"):
    """
        comvierte la cadena de texto en un objecto time
    """
    list = [int(n) for n in cad.split(":")]
    hora = datetime.time(list[1], list[0])
    return hora


def date_to_str(date):
    """
        combierte un objeto date a "DD/MM/AAAA"
    """
    return date.strftime('%d/%m/%Y')


def true_false(val=True):
    """
        Combierte Booleano en tipo SI/NO
    """
    if val:
        return "Si"
    else:
        return "No"


def date_today_str():
    """
        Formatea la fecha Actual com Str
    """
    return datetime.datetime.today().strftime("%d/%m/%Y")



