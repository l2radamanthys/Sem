#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls.defaults import *

#admni
from django.contrib import admin
admin.autodiscover()

#propios
from settings import MEDIA_ROOT

import generics_views
from GestionTurnos import pacientes_views, admin_views
from GestionTurnos import medicos_views, especialidades_views

urlpatterns = patterns('',
    # Example:
    # (r'^TurnGest/', include('TurnGest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include('django.contrib.admin.urls')),
    (r'^admin/', include(admin.site.urls)),

    #media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes':True }),

    #pagina inicio
    (r'^/?$', generics_views.index),

    #sesiones
    (r'^accounts/login/$', generics_views.login),
    (r'^accounts/logout/$', generics_views.logout),
    (r'^accounts/change_password/$', generics_views.cambio_contrasenia),
    (r'^accounts/datos-personales/$', generics_views.datos_personales),
    (r'^accounts/modificar-datos-personales/$', generics_views.datos_personales_modificar),

    ## - Gestion Turnos - ##
    # - Pacientes Views
    (r'^pacientes/nuevo/$', pacientes_views.nuevo_paciente),
    (r'^pacientes/listado/$', pacientes_views.listado_pacientes),
    (r'^pacientes/datos/$', pacientes_views.datos_paciente),
    (r'^pacientes/datos/(\d{1,2})/$', pacientes_views.datos_paciente),
    (r'^pacientes/modificar/$', pacientes_views.modificar_paciente),
    (r'^pacientes/modificar/(\d{1,2})/$', pacientes_views.modificar_paciente),
    (r'^pacientes/guardar/$', pacientes_views.guardar_cambios_paciente),
    (r'^pacientes/guardar/(\d{1,2})/$', pacientes_views.guardar_cambios_paciente),
    (r'^pacientes/borrar/$', pacientes_views.borrar_paciente),
    (r'^pacientes/borrar/(\d{1,2})/$', pacientes_views.borrar_paciente),
    (r'^pacientes/borrado/$', pacientes_views.borrado_paciente),
    (r'^pacientes/borrado/(\d{1,2})/$', pacientes_views.borrado_paciente),
    (r'^pacientes/buscar/$', pacientes_views.buscar_pacientes),

    # - Medicos Views
    (r'^medicos/nuevo/$', medicos_views.nuevo_medico),
    (r'^medicos/listado/$', medicos_views.listado_medicos),
    (r'^medicos/agregar-especialidades/$', medicos_views.agregar_especialidad),
    (r'^medicos/agregar-especialidades/(\d{1,2})/$', medicos_views.agregar_especialidad),
    #(r'^medicos/datos/$', medicos_views.datos_medico),
    #(r'^medicos/datos/(\d{1,2})/$', medicos_views.datos_medico),
    #(r'^medicos/modificar/$', medicos_views.modificar_medico),
    #(r'^medicos/modificar/(\d{1,2})/$', medicos_views.modificar_medico),
    #(r'^medicos/guardar/$', medicos_views.guardar_cambios_medico),
    #(r'^medicos/guardar/(\d{1,2})/$', medicos_views.guardar_cambios_medico),
    #(r'^medicos/borrar/$', medicos_views.borrar_medico),
    #(r'^medicos/borrar/(\d{1,2})/$', pacientes_views.borrar_medico),
    #(r'^medicos/borrado/$', medicos_views.borrado_medico),
    #(r'^medicos/borrado/(\d{1,2})/$', medicos_views.borrado_medico),
    #(r'^medicos/buscar/$', medicos_views.buscar_pacientes),

    # - Medicos - Especialidades
    (r'^medicos/especialidades/agregar/$', especialidades_views.agregar),
    (r'^medicos/especialidades/listado/$', especialidades_views.listado),
    #(r'^medicos/especialidades/modificar/$', ),
    #(r'^medicos/especialidades/borrar/$', ),
    #(r'^medicos/especialidades/asignar/$', ),


    # - Administrativos Views
    (r'^administrativos/nuevo/$', admin_views.nuevo_admin),
    (r'^administrativos/listado/$', admin_views.listado_admins),
    (r'^administrativos/datos/$', admin_views.datos_admin),
    (r'^administrativos/datos/(\d{1,2})/$', admin_views.datos_admin),
    (r'^administrativos/modificar/$', admin_views.modificar_admin),
    (r'^administrativos/modificar/(\d{1,2})/$', admin_views.modificar_admin),
    (r'^administrativos/guardar/$', admin_views.guardar_cambios_admin),
    (r'^administrativos/guardar/(\d{1,2})/$', admin_views.guardar_cambios_admin),
    (r'^administrativos/borrar/$', admin_views.borrar_admin),
    (r'^administrativos/borrar/(\d{1,2})/$', admin_views.borrar_admin),
    (r'^administrativos/borrado/$', admin_views.borrado_admin),
    (r'^administrativos/borrado/(\d{1,2})/$', admin_views.borrado_admin),
    (r'^administrativos/buscar/$', admin_views.buscar_admins),



    # - Turnos

    ## - Historia Clinica - ##

    ## - Otras Views - ##
    (r'^usuario-no-autorizado/$', generics_views.no_autorizado),
    
)

#paginas personalizadas para los errores 404 y 505
handler404 = 'generics_views.error404'
#handler500 = 'generics_views.error500'
