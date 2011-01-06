#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    manejo de vistas de los pacientes
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth #para login

from GestionTurnos.models import Pacientes
from constantes import BASE_DIC


def nuevo_paciente(request):
    plantilla = get_template('pacientes/gestion_turnos/nuevo.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Nuevo Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['url_action'] = '/accounts/login/'

    #si se realizo una consulta
    query = int(request.POST.get('query', '0'))
    dict['query'] = query

    if query:
        username = request.POST.get('usuario', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')

        user = User.objects.create_user(username, email, password)
        user.first_name = request.POST.get('nombre', '')
        user.last_name = request.POST.get('apellido', '')
        user.is_staff = False
        user.is_active = True
        user.save()

        paciente = Pacientes(
            dni = request.POST.get('dni', ''),
            sexo = request.POST.get('sexo', ''),
            telefono = request.POST.get('telefono', ''),
            direccion = request.POST.get('direccion', ''),
            user = User.objects.get(username__exact=username)
        )
        paciente.save()
        
        
        
        

        







    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)

