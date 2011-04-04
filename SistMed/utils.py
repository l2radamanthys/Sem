#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    listado de Funciones de Utilidad
"""

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

def sexo_choice_expand(key):
    """
        Expande el identificador del choice sexo
    """
    return SEXO_CHOICE_DIC[key]



def get_GET_value(request, key='', default='', blank=''):
    value = request.POST.get(key, default, blank)
    if value == '':
        value = default
    return value


def get_POST_value(request, key='', default='', blank=''):
     value = request.POST.get(key, default, blank)
     if value == '':
        value = default
     return value


def get_value(request=None, key='', default='', blank='', method=POST):
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
        dict['user'] = ''
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