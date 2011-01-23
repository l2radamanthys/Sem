#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    manejo de vistas de los Administrativos
"""


from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth #para login
from django.contrib.auth.models import User, Group

from GestionTurnos.models import Administrativos, TipoUsuario
from utils import get_field_css, sexo_choice_expand, get_POST_value
from constantes import BASE_DIC


def nuevo_admin(request):
    """
        Vista que Permite crear un nuevo Admin

        pueden acceder
        --------------
        -administrativos

        sin acceso
        ----------
        - pacientes
        - usuarios no registrados
        - medicos
    """
    plantilla = get_template('administrativo/gestion_turnos/nuevo.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Nuevo Admin'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'

    #si se realizo una consulta
    query = int(request.POST.get('query', '0'))
    dict['query'] = query

    if query:
        username = request.POST.get('usuario', '')
        password = request.POST.get('password_1', '')
        email = request.POST.get('email', '')

        #para comprobar si el usuario ya existe
        try:
            user = User.objects.get(username__exact=username)
        except:
            user = None

        if user is None:
            user = User.objects.create_user(username, email, password)
            user.first_name = request.POST.get('nombre', '-')
            user.last_name = request.POST.get('apellido', '-')
            user.email = request.POST.get('email', '@')
            user.is_staff = False #no es admin
            user.is_active = True #esta activo
            #lo agrego al grupo de los admins
            #pac_group = Group.objects.get(name=PACIENTES)
            #user.groups.add(pac_group)
            #guardamos
            user.save()
            admin = Administrativos(
                dni = int(get_POST_value(request,'dni','0','0')),
                sexo = get_POST_value(request,'sexo','-','-'),
                telefono = request.POST.get('telefono', ''),
                direccion = request.POST.get('direccion', ''),
                tipo_usuario = TipoUsuario.objects.get(nombre__exact='Administrativo'),
                user = User.objects.get(username__exact=username)

            )
            #guardamos
            admin.save()
            dict['msj_class'] = 'msj_ok'
            dict['mensaje'] = "Se ha Agregado: %s" %username

        else:
            dict['msj_class'] = 'msj_error'
            dict['mensaje'] = "Error el nombre de usuario %s, no esta disponible" %username

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listado_admins(request):
    """
        Vista que permite mostrar el listado de admins

        pueden acceder
        --------------
        -administrativos

        sin acceso
        ----------
        - medicos
        - usuarios no registrados
        - pacientes
    """
    plantilla = get_template('administrativo/gestion_turnos/listado.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Listado Admins'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'


    listado_admins = []
    band = True
    for admin in Administrativos.objects.all():
        id = admin.id
        username = admin.user.username
        nombre = admin.nombre_completo()
        css = get_field_css(band)
        band = not(band)
        listado_admins.append([id, username, nombre, css])


    dict['listado_admins'] = listado_admins

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def datos_admin(request, adm_id=-1):
    """
        Muestra los datos del Paciente ademas de las
        solicitudes y turnos q le fueron asignados

        pueden acceder
        --------------
        - administrativos
       
        sin acceso
        ----------
        - medicos
        - pacientes
        - usuarios no registrados
    """
    plantilla = get_template('administrativo/gestion_turnos/datos.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Datos Admin'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'


    adm_id = int(adm_id)
    if adm_id != -1:
        admin = Administrativos.objects.get(id=adm_id)
        dict['adm_id'] = adm_id
        dict['username'] = admin.username()
        dict['nombre'] = admin.nombre_completo()
        dict['direccion'] = admin.direccion
        dict['telefono'] = admin.telefono
        dict['email'] = admin.username()
        dict['sexo'] = sexo_choice_expand(admin.sexo)

    else:
        pass

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_admin(request, adm_id=-1):
    """
        Permite modificar algunos datos del admin

        pueden acceder
        --------------
        - administrativos
        

        sin acceso
        ----------
        - usuarios no registrados
        - pacientes
        - medicos
    """
    plantilla = get_template('administrativos/gestion_turnos/modificar.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Modificar Datos Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'

    adm_id = int(adm_id)
    if adm_id != -1:
        #query = int(get_POST_value(request,'query', '0'))
        #dict['query'] = query
        #si se envio un formulario modificado
        #if query:
        #    pass
        #caso q recien se muestre la pagina
        #else:
        dict['query'] = True
        dict['adm_id'] = adm_id
        admin = Administrativos.objects.get(id=adm_id)
        dict['nombre'] = admin.user.first_name
        dict['apellido'] = admin.user.last_name
        dict['dni'] = admin.dni
        dict['direccion'] = admin.direccion
        dict['telefono'] = admin.telefono
        dict['email'] = admin.user.email
        dict['sexo'] = admin.sexo

    else:
        dict['query'] = False
        dict['msj_class'] = 'msj_error'
        dict['mensaje'] = 'Error Datos Invalido'


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def guardar_cambios_admin(request, adm_id=-1):
    """
        Permite modificar algunos datos del admin

        pueden acceder
        --------------
        - medicos
        - administrativos
        - admins (unicamente a su propio perfil)

        sin acceso
        ----------
        - usuarios no registrados
    """
    plantilla = get_template('admins/gestion_turnos/guardar.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Guardar Datos Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'


    query = int(get_POST_value(request,'query', '0'))
    dict['query'] = query

    adm_id = int(adm_id)
    if adm_id != -1 and query:
        admin = Administrativos.objects.get(id=adm_id)
        admin.user.first_name = get_POST_value(request,'nombre','')
        admin.user.last_name = get_POST_value(request,'apellido','')
        admin.user.save()
        admin.dni = int(get_POST_value(request,'dni','0','0'))
        admin.direccion = get_POST_value(request,'direccion','')
        admin.telefono = get_POST_value(request,'telefono','')
        admin.email = get_POST_value(request,'email','')
        admin.sexo = get_POST_value(request,'sexo','-','-')
        admin.save()

        #redireciono a la pagina q muestra los datos del admin
        #HttpResponseRedirect("/admins/datos/%d/" %adm_id)
        dict['adm_id'] = adm_id
        dict['msj_class'] = 'msj_ok'
        dict['mensaje'] = 'Cambios Realizados Correctamente'

    else:
        #dict['query'] = False
        dict['msj_class'] = 'msj_error'
        dict['mensaje'] = 'Error Datos Invalido'


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrar_admin(request, adm_id=-1):
    """
        Vista de confirmacion de borrado de un admin

        pueden acceder
        --------------
        - administrativos

        sin acceso
        ----------
        - medicos
        - admins
        - usuarios no registrados
    """
    plantilla = get_template('admins/gestion_turnos/borrar.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Borrar Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'

    adm_id = int(adm_id)

    if adm_id != -1:
        admin = Administrativos.objects.get(id=adm_id)
        dict['query'] = True
        dict['nombre'] = admin.nombre_completo()
        dict['adm_id'] = adm_id

    else:
        dict['query'] = False
        dict['msj_class'] = 'msj_error'
        dict['mensaje'] = 'Error Datos Invalido'


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrado_admin(request, adm_id=-1):
    """
        Permite Borrar un admin

        pueden acceder
        --------------
        - administrativos

        sin acceso
        ----------
        - medicos
        - admins
        - usuarios no registrados
    """
    plantilla = get_template('admins/gestion_turnos/borrar.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Borrar Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'

    adm_id = int(adm_id)

    if adm_id != -1:
        admin = Administrativos.objects.get(id=adm_id)
        dict['query'] = True
        dict['nombre'] = admin.nombre_completo()
        admin.user.delete()
        admin.delete()

    else:
        dict['query'] = False
        dict['msj_class'] = 'msj_error'
        dict['mensaje'] = 'Error Operacion No valida'



    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def buscar_admins(request):
    """
        Permite Buscar un admin por nombre, apellido o usuario

        pueden acceder
        --------------
        - administrativos
        - medicos

        sin acceso
        ----------
        - admins
        - usuarios no registrados
    """
    plantilla = get_template('admins/gestion_turnos/buscar.html')
    dict = BASE_DIC.copy()

    dict['titulo'] = 'Buscar Paciente'
    #usuario estado
    if request.user.is_authenticated():
        dict['login_status'] = 'online'
        dict['login_img'] = 'online.png'
        dict['url_action'] = '/accounts/logout/'
    else:
        dict['login_status'] = 'offline'
        dict['login_img'] = 'offline.png'
        dict['url_action'] = '/accounts/login/'

    #tipo de busqueda
    #1 usuario
    #2 nombre
    #3 apellido
    query = int(request.POST.get('query', '0'))
    dict['query'] = query
    if query:
        buscar_text = request.POST.get('buscar_text', '')
        buscar_por = int(request.POST.get('buscar_por', '0'))

        if buscar_text != "":
            if buscar_por == 0:
                list_admins = Administrativos.objects.filter(user__username__icontains=buscar_text)

            elif buscar_por == 1:
                list_admins = Administrativos.objects.filter(user__first_name__icontains=buscar_text)

            elif buscar_por == 2:
                list_admins = Administrativos.objects.filter(user__last_name__icontains=buscar_text)

        #si se ingreso text en blanco pongo todos
        else:
            list_admins = Administrativos.objects.all()


        listado_admins = []
        band = True
        for admin in list_admins:
            id = admin.id
            username = admin.user.username
            nombre = admin.nombre_completo()
            css = get_field_css(band)
            band = not(band)
            listado_admins.append([id, username, nombre, css])
        dict['listado_admins'] = listado_admins

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)