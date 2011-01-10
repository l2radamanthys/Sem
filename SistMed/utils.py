#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    listado de Funciones de Utilidad
"""

from constantes import SEXO_CHOICE_DIC


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
