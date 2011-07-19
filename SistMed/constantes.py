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
    'page_title': 'Sistemas de Gestion de Consultorio Medico',
}

#choices
#sexo del usuario
SEXO_CHOICE = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('-', 'No Definido'),
)

SEXO_CHOICE_DIC = {
    'M' : 'Masculino',
    'F' : 'Femenino',
    '-' : 'No Definido',
}

#solicitud turnos
SOLICITUD_ESTADO_CHOICE = (
    ('P','Pendiente'),
    ('A','Aceptado'),
    ('C','Cancelado'),
)


DATE_CHOICE = (
    ('LUN', 'Lunes'),
    ('MAR', 'Martes'),
    ('MIE', 'Miercoles'),
    ('JUE', 'Jueves'),
    ('VIE', 'Viernes'),
    ('SAB', 'Sabado'),
    ('DOM', 'Domingo'),
)

DATE_CHOICE_DIC = {
    'LUN': 'Lunes',
    'MAR': 'Martes',
    'MIE': 'Miercoles',
    'JUE': 'Jueves',
    'VIE': 'Viernes',
    'SAB': 'Sabado',
    'DOM': 'Domingo',
}


ESTADO_CIVIL_CHOICE = (
    ('-', 'No Definido'),
    ('S', 'Soltero'),
    ('C', 'Casado'),
    ('V', 'Viudo'),
    ('D', 'Divorciado'),
    ('U', 'Union Libre'),
)


GRUPO_SANGUINEO_CHOICE = (
    ("O+", "O+"),
    ("O-","O-"),
    ("A+","A+"),
    ("A-","A-"),
    ("B+","B+"),
    ("B-","B-"),
    ("AB+","AB+"),
    ("AB-","AB-"),
)


TIPO_DOSIS_CHOICE = (
    ("UNI","Unica Dosis"),
    ("1ra","1ra Dosis"),
    ("2da","2da Dosis"),
    ("3ra","3ra Dosis"),
    ("REF","Refuerzo"),
)

TIPO_DOSIS_DIC = {
    "UNI":"Unica Dosis",
    "1ra":"1ra Dosis",
    "2da":"2da Dosis",
    "3ra":"3ra Dosis",
    "REF":"Refuerzo",
}



GRUPOS_SANGUINEOS = (
    "O+",
    "O-",
    "A+",
    "A-",
    "B+",
    "B-",
    "AB+",
    "AB-",
)

#nombres grupos
PACIENTE = 'Paciente'
MEDICO = 'Medico'
ADMINISTRATIVO = 'Administrativo'

#permisos
NIVEL_0 = 0
NIVEL_1 = 1
NIVEL_2 = 2
NIVEL_3 = 3


#ruta del proyecto
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
_MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MI_TEMPLATE_DIR = os.path.join(PROJECT_PATH, 'templates')


#constantes relacionadas con la plantilla CSS
MSJ_ERROR = 'msj_error'
MSJ_OK = 'msj_ok'
MSJ_ALERT = 'msj_alert'