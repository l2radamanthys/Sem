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

from constantes import BASE_DIC


def index(request):
    plantilla = get_template('base.html')

    dict = BASE_DIC.copy()
    #usuario estado
    dict['titulo'] = 'Inicio'
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['url_action'] = '/accounts/login/'

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def login(request):
    """
        Autentificar usuarios
    """

    if not(request.user.is_authenticated()):
        plantilla = get_template('login.html')
        dict = BASE_DIC.copy()
        
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                # Clave correcta, y el usuario est� marcado "activo"
                auth.login(request, user)
                dict['mensaje'] = username
                # Redirigir a una pagina de exito.
                return HttpResponseRedirect('/')
    
        if username != '':
            dict['login_fail'] = True
            dict['mensaje'] = "El Nombre de usuario o contraseña no son validos"
    
        contexto = Context(dict)
        html = plantilla.render(contexto)
        return HttpResponse(html)

    else:
        return HttpResponseRedirect('/')


def logout(request):
    """
        Salida de un usuario
    """
    auth.logout(request)
    plantilla = get_template('logout.html')
    dict = BASE_DIC.copy()
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


