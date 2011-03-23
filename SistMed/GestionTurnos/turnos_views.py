#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    manejo de vistas referente a la asignacion de turnos..
"""


from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context

from django.contrib import auth #para login
from django.contrib.auth.models import User#, Group

#from GestionTurnos.models import Administrativos, TipoUsuario
#from utils import get_field_css, sexo_choice_expand, get_POST_value, generar_base_dict
from constantes import BASE_DIC