#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Aqui se definiran las vistas Genericas de la Aplicaicion tales como:
    - indexs
    - login
    - logout
    - Error 404
    etc.
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth #para login

from GestionTurnos.models import Pacientes
from constantes import BASE_DIC


def index(request):
    plantilla = get_template('base.html')
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def login(request):
    """
        Autentificar usuarios
    """
    plantilla = get_template('login.html')
    dict = BASE_DIC.copy()
    dict['login_fail'] = True
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
    except: #arreglar esto
        user = None
        dict['login_fail'] = False
    
    if user is not None:
        if user.is_active:
            # Clave correcta, y el usuario está marcado "activo"
            auth.login(request, user)
            # Redirigir a una página de éxito.
            HttpResponseRedirect('/admin/')

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def logout(request):
    plantilla = get_template('logout.html')
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


