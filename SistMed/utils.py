#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    listado de Funciones de Utilidad extendida
"""
import datetime

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
    rol = request.session.get('usuario_rol', '')
    dict['nivel_0'] = True
    dict['nivel_1'] = False
    dict['nivel_2'] = False
    dict['nivel_3'] = False

    if rol == PACIENTE:
        dict['nivel_0'] = False
        dict['nivel_1'] = True

    elif rol == MEDICO:
        dict['nivel_0'] = False
        dict['nivel_1'] = True
        dict['nivel_2'] = True

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
    list = [int(n) for n in cad.split("/")].reverse()
    if len(list) == 3: # ejem 01/01/1920 completo
        fecha = datetime.datetime(list[2], list[1], list[0])
    elif len(list) == 2: # ejem 01/03 falta el anio por lo tanto anio=0 -.-
        fecha = datetime.datetime(0, list[1], list[0])
    return fecha


def time_split(str="00:00:00"):
    """
        comvierte la cadena de texto en un objecto time
    """
    list = [int(n) for n in cad.split(":")]
    hora = datetime.time(list[1], list[0])
    return hora