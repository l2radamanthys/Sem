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
from django.contrib.auth.models import User
from GestionTurnos.models import *


print "Inicializando Datos de Interfaz...",
#creo los tipo de usuario
t_pac = TipoUsuario(nombre='Paciente')
t_pac.save()
t_med = TipoUsuario(nombre='Medico')
t_med.save()
t_adm = TipoUsuario(nombre='Administrativo')
t_adm.save()
print "OK"

#crea el usuario administrativo interno del sistema
print "Comfigurando el usuario admin...",
adm = User.objects.get(username="admin")
n_adm = Administrativos(
    dni = 123,
    sexo = "M",
    telefono = "1234",
    direccion = "Admin Ksa",
    tipo_usuario=t_adm,
    user=adm
)
n_adm.save()
print "Ok"


