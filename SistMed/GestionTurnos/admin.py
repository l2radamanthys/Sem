#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from GestionTurnos.models import *


#establesco las tablas que seran modificadas por el admin
admin.site.register(Expecialidades)
admin.site.register(Medicos)
admin.site.register(Pacientes)
admin.site.register(Administrativos)
admin.site.register(ExpecialidadesMedicos)
admin.site.register(Consultorios)
admin.site.register(HorarioAtencion)
admin.site.register(DiasAtencion)
admin.site.register(Turnos)
admin.site.register(SolitudesTurnos)


