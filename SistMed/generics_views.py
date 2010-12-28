#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Aqui se definiran las vistas Genericas de la Aplicaicion tales como:
    - login
    - logout
    - Error 404
    etc.
"""

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from GestionTurnos.models import Pacientes


BASE_DIC = {
    'css_template': '',
    'page_title': '',
}


def login(request):
    plantilla = get_template('login.html')
    contexto = Context(dict)
    xhtml = plantilla.render(contexto)
    return HttpResponse(xhtml)


def logout(request):
    pass