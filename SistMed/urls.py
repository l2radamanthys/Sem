#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls.defaults import *

#admni
from django.contrib import admin
admin.autodiscover()

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

    #sessiones
    (r'^accounts/login/$', generics_views.login),
    (r'^accounts/logout/$', generics_views.logout),

    #gestion turnos
    #(r'^pacientes/listado/$', pacientes_views.listado_paciente),
    (r'^pacientes/nuevo/$', pacientes_views.nuevo_paciente),
    #(r'^pacientes/modificar/$', pacientes_views.modificar_paciente),
    #(r'^pacientes/borrar/$', pacientes_views.borrar_paciente),
)
