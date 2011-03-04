#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    manejo de vistas de los pacientes
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth #para login
from django.contrib.auth.models import User, Group

from GestionTurnos.models import Medicos, TipoUsuario
from utils import get_field_css, sexo_choice_expand, get_POST_value, generar_base_dict
from constantes import BASE_DIC

def nuevo_medico(request):
    """
        Vista que Permite crear un nuevo paciente

        pueden acceder
        ------------
        -administrativos

        sin acceso
        ----------
        - usuarios no registrados
        - pacientes
        - medicos

    """
    plantilla = get_template('medicos/gestion_turnos/nuevo.html')
    dict = generar_base_dict(request)
    dict['titulo'] = 'Nuevo Medico'

    #si se realizo una consulta
    query = int(request.POST.get('query', '0'))
    dict['query'] = query

    if query:
        username = request.POST.get('usuario', '')
        password = request.POST.get('password_1', '')
        email = request.POST.get('email', '@')

        #para comprobar si el usuario ya existe
        user = User.objects.filter(username__exact=username)
        if user != None:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = request.POST.get('nombre', '-')
            user.last_name = request.POST.get('apellido', '-')
            user.email = request.POST.get('email', '@')
            user.is_staff = False #no es admin
            user.is_active = True #esta activo
            #lo agrego al grupo de los pacientes
            #pac_group = Group.objects.get(name=PACIENTES)
            #user.groups.add(pac_group)
            #guardamos
            user.save()
            medico = Medicos(
                dni = int(get_POST_value(request,'dni','0','0')),
                sexo = get_POST_value(request,'sexo','-','-'),
                telefono = request.POST.get('telefono', ''),
                direccion = request.POST.get('direccion', ''),
                tipo_usuario = TipoUsuario.objects.get(nombre__exact='Paciente'),
                user = User.objects.get(username__exact=username),
                matricula = request.POST.get('matricula', '0'),
            )
            #guardamos
            medico.save()
            dict['msj_class'] = 'msj_ok'
            dict['mensaje'] = "Se ha Agregado: %s" %username

        else:
            dict['msj_class'] = 'msj_error'
            dict['mensaje'] = "Error el nombre de usuario %s, no esta disponible" %username

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)