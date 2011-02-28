#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    listado de Funciones de Utilidad
"""

from constantes import SEXO_CHOICE_DIC, POST, GET, BASE_DIC


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
    value = request.POST.get(key, default)
    if value == '':
        value = default
    return value


def get_POST_value(request, key='', default='', blank=''):
     value = request.POST.get(key, default)
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
        #dict['user_rol'] = request.session.get('usuario_rol', '')
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'
        #request.session['usuario'] = ''
        #request.session['usuario_rol'] = ''
        dict['user'] = ''
        #dict['user_rol'] = ''
        dict['user_autenticado'] = False
    return dict