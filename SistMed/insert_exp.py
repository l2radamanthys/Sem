#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from GestionTurnos.models import *

#agrega las expecialidades por defecto
expec = [
    'Odontologo',
    'Traumatologo',
    'Psicologo',
    'Pediatra',
    'Neurologo',
    'Oftalmologo',
    'Podologo',
    'Psiquiatra',
    'Nutricionista',
    'Cardiologo',
]

print "Agregando Expecialidades...",
for name in expec:
    exp = Expecialidades(nombre=name)
    exp.save()
print "OK"
    
