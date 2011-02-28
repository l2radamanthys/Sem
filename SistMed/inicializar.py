#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Script para inicializar el Sistema
    ----------------------------------

    Ejecutar despues de haver creado las Tablas del Sistema

    Este Script Ejecuta Inserciones Basicas en Las Tablas por lo que
    es recomendable Ejecutarlo solo una ves.. posteriores ejecuciones pueden
    crear conflictos en la Base de Datos
"""

#from settings import *
from django.conf.urls.defaults import *
from GestionTurnos.models import TipoUsuario


#creo los tipo de usuario
t_pac = TipoUsuario(nombre='Paciente')
t_med = TipoUsuario(nombre='Medico')
t_adm = TipoUsuario(nombre='Administrativo')
t_pac.save()
t_med.save()
t_adm.save()