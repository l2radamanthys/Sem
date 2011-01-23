#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from GestionTurnos import models


#establesco las tablas que seran modificadas por el admin
admin.site.register(models.TipoUsuario)
admin.site.register(models.Expecialidades)
admin.site.register(models.Medicos)
admin.site.register(models.Pacientes)
admin.site.register(models.Administrativos)
admin.site.register(models.ExpecialidadesMedicos)
admin.site.register(models.Consultorios)
admin.site.register(models.HorarioAtencion)
admin.site.register(models.DiasAtencion)
admin.site.register(models.Turnos)
admin.site.register(models.SolitudesTurnos)


