#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    listado de Funciones de Utilidad
"""

from constantes import SEXO_CHOICE_DIC, POST, GET


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