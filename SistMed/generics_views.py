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
from django.contrib.auth.models import User
from GestionTurnos.models import Usuarios, Pacientes, Medicos, Administrativos

from utils import generar_base_dict
from constantes import *


def index(request):
    """
        Pagina de Inicio
    """
    plantilla = get_template('base.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Inicio'

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

        query = int(request.POST.get('query', '0'))
        dict['query'] = query

        if query:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
        
            if (user is not None) and user.is_active:
                # Clave correcta, y el usuario estï¿½ marcado "activo"
                auth.login(request, user)
                dict['mensaje'] = username

                #datos de seccion
                usuario = Usuarios.objects.get(user__username__exact=username)
                request.session['usuario'] = usuario.username()
                request.session['usuario_rol'] = usuario.tipo_usuario.nombre
                
                # Redirigir a una pagina de Inicio.
                return HttpResponseRedirect('/')
    
            else:
                dict['query'] = True
                dict['msj_class'] = 'msj_error'
                dict['mensaje'] = "Error: El Nombre de usuario o contraseÃ±a no son validos"

    
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
    request.session['usuario'] = ''
    request.session['usuario_rol'] = ''


def cambio_contrasenia(request):
    """
        Permite cambiar la contrasenia del usuario
    """

    if request.user.is_authenticated():
        plantilla = get_template('cambio_contrasenia.html')

        dict = BASE_DIC.copy()

        query = int(request.POST.get('query', '0'))
        dict['query'] = query
        if query:
            user = User.objects.get(username__exact=request.session.get('usuario', ''))
            old_password = request.POST.get('old_password', '')
            new_password = request.POST.get('new_password', '')
            #controla q la contraseña anterior sea valida
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                dict['mensaje'] = 'Contrasenia Actualizada'
                dict['msj_class'] = MSJ_OK
            else:
                dict['mensaje'] = 'Error Contrasenia Invalida'
                dict['msj_class'] = MSJ_ERROR

        contexto = Context(dict)
        html = plantilla.render(contexto)
        return HttpResponse(html)
    else:
        return HttpResponseRedirect('/')


def datos_personales(request):
    if request.user.is_authenticated():
        rol = request.session.get('usuario_rol', '')
        username = request.session.get('usuario', '')

        if rol == PACIENTE:
            pac = Pacientes.objects.get(user__username=username)
            url = '/pacientes/datos/%d/' %pac.id

        #elif rol == MEDICO:
        #    med = Medicos.objects.get(user__username__exact=username)
        #    url = '/medicos/datos/%d/' %pac.id

        elif rol == ADMINISTRATIVO:
            adm = Administrativos.objects.get(user__username__exact=username)
            url = '/administrativos/datos/%d/' %pac.id
        
        else:
            url = '/usuario-no-autorizado/[%s]' %rol
            
        return HttpResponseRedirect(url)



def datos_personales_modificar(request):
    if request.user.is_authenticated():
        rol = request.session.get('usuario_rol', '')
        username = request.session.get('usuario', '')

        if rol == PACIENTE:
            pac = Pacientes.objects.get(user__username=username)
            url = '/pacientes/modificar/%d/' %pac.id

        #elif rol == MEDICO:
        #    med = Medicos.objects.get(user__username__exact=username)
        #    url = '/medicos/modificar/%d/' %pac.id

        #elif rol == ADMINISTRATIVO:
        #    adm = Administrativos.objects.get(user__username__exact=username)
        #    url = '/administrativos/modificar/%d/' %pac.id

        else:
            url = '/usuario-no-autorizado/[%s]' %rol

        return HttpResponseRedirect(url)


def no_autorizado(request):
    plantilla = get_template('no_autorizado.html')
    dict = BASE_DIC.copy()
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def error404(request):
    plantilla = get_template('404.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Error 404'
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)