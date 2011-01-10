#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Listado de constantes q se usaran en el Sistema
"""

import os

GET = 0
POST = 1

#dicionario base
BASE_DIC = {
    'css_template': '/site_media/css/base.css',
    'page_title': 'Sistemas Medico',
}

#choices
#sexo del usuario
SEXO_CHOICE = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('-', '-----'),
)

SEXO_CHOICE_DIC = {
    'M' : 'Masculino',
    'F' : 'Femenino',
    '-' : '-----',
}

#solicitud turnos
SOLICITUD_ESTADO_CHOICE = (
    ('P','Pendiente'),
    ('A','Aceptado'),
    ('C','Cancelado'),
)


#nombres grupos
PACIENTES = 'Pacientes'
MEDICOS = 'Medicos'
ADMINISTRATIVOS = 'Administrativos'


#ruta del proyecto
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
_MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MI_TEMPLATE_DIR = os.path.join(PROJECT_PATH, 'templates')


#constantes relacionadas con la plantilla CSS
MSJ_ERROR = 'msj_error'
MSJ_OK = 'msj_ok'
MSJ_ALERT = 'msj_alert'