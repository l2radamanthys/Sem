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

from utils import *
from constantes import *


def area(request):
    """
        Cambia los Menu q se van a mostrar
    """
    opcion = request.GET.get('opcion', 'gt')
    if opcion == 'gt':
        request.session['area'] = "True"
    else:
        request.session['area'] = "False"
    return HttpResponseRedirect('/')


def index(request):
    """
        Pagina de Inicio
    """
    plantilla = get_template('index.html')
    dict = generar_base_dict(request)
    dict['sin_titulo'] = True # 'Sistema de Gestion de Consultorio Medico'

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
                # Clave correcta, y el usuario est� marcado "activo"
                auth.login(request, user)
                dict['mensaje'] = username

                #datos de seccion
                usuario = Usuarios.objects.get(user__username__exact=username)
                request.session['usuario'] = usuario.username()
                request.session['usuario_rol'] = usuario.tipo_usuario.nombre
                request.session['usuario_id'] = usuario.id

                # Redirigir a una pagina de Inicio.
                return HttpResponseRedirect('/')

            else:
                dict['query'] = True
                dict['msj_class'] = 'msj_error'
                dict['mensaje'] = "Error: El Nombre de usuario o contraseña no son validos"


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
    request.session['usuario_id'] = '-1'

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
            old_password = request.POST.get('password_old', '')
            new_password = request.POST.get('password_new', '')
            #controla q la contrase�a anterior sea valida
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                dict['mensaje'] = 'Contrasenia Actualizada'
                dict['msj_class'] = MSJ_OK
            else:
                dict['mensaje'] = 'Error Contrasenia Invalida %s - %s' %(old_password, new_password)
                dict['msj_class'] = MSJ_ERROR

        contexto = Context(dict)
        html = plantilla.render(contexto)
        return HttpResponse(html)
    else:
        return HttpResponseRedirect('/')


def datos_personales(request):
    """
        Muestra los datos personales del usuario q actualmente esta logueado
    """
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
            url = '/administrativos/datos/%d/' %adm.id

        else:
            url = '/usuario-no-autorizado/[%s]' %rol

        return HttpResponseRedirect(url)


def datos_personales_modificar(request):
    if request.user.is_authenticated():
        rol = request.session.get('usuario_rol', '')
        username = request.session.get('usuario', '')

        if rol == PACIENTE:
            pac = Pacientes.objects.get(id=request.session.get('usuario_id', '-1'))
            url = '/pacientes/modificar/%d/' %pac.id

        elif rol == MEDICO:
            med = Medicos.objects.get(id=request.session.get('usuario_id', '-1'))
            url = '/medicos/modificar/%d/' %med.id

        elif rol == ADMINISTRATIVO:
            adm = Administrativos.objects.get(id=request.session.get('usuario_id', '-1'))
            url = '/administrativos/modificar/%d/' %adm.id

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


def page_error(request):
    """
        Pagina para mostrar error de operacion..
    """
    plantilla = get_template('error.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Aplicacion Error - ' + get_GET_value(request, "title", "")
    dict['msj_error'] = get_GET_value(request, "msj", "")
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)
