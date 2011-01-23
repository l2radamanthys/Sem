#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls.defaults import *

#admni
from django.contrib import admin
admin.autodiscover()

#propios
from settings import MEDIA_ROOT

import generics_views
from GestionTurnos import pacientes_views


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
    #(r'/accounts/change_password/$' generics_views.cambiar_contrasenia),

    #Gestion Turnos
    # - Pacientes Views
    (r'^pacientes/buscar/$', pacientes_views.buscar_pacientes),
    (r'^pacientes/listado/$', pacientes_views.listado_pacientes),
    (r'^pacientes/nuevo/$', pacientes_views.nuevo_paciente),
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
    
    
)


#paginas personalizadas para los errores 404 y 505
#handler404 = 'generics_views.error404'
#handler500 = 'generics_views.error500'
