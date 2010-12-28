#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


#choices

#sexo del usuario
SEXO_CHOICE = (
    ('M','Masculino'),
    ('F', 'Femenino'),
    ('-','-----'),
)

#solicitud turnos
SOLICITUD_ESTADO = (
    ('P','Pendiente'),
    ('A','Aceptado'),
    ('C','Cancelado'),
)

#modelos
#class TipoUsuario(models.Model):
#    """
#        En ves de crear las clases Medico, Paciente, Administrativo
#        cree una clase categoria q le definira la clase al paciente
#    """
#    nombre = models.CharField(max_length=30)


class Expecialidades(models.Model):
    """
        Clasificacion de las expecialidades de todos los medicos
    """
    nombre = models.CharField(max_length=30)


    def __str__(self):
        return self.nombre


class Usuarios(User):
    """
        Para el login y el manejo de secciones
    """
    dni = models.IntegerField()
    sexo = models.CharField(max_length=1, default='-', choices=SEXO_CHOICE)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=60)
    
    #FK
    #tipo = models.ForeignKey(TipoUsuario)

    #datos utiles para recordar
    #username, password, first_name, last_name


    def nombre_completo(self):
        return self.first_name + self.last_name


    def __str__(self):
        return self.username


class Medicos(Usuarios):
    matricula = models.CharField(max_length=30)


class Pacientes(Usuarios):
    pass


class Administrativos(Usuarios):
    pass


class ExpecialidadesMedicos(models.Model):
    """
        Clasificacion de las Distintas Expecialidades de los Medicos
    """
    #fk
    codigo_medico = models.ForeignKey(Medicos)
    cod_expecialidad = models.ForeignKey(Expecialidades)


#sin usar por el momento
class Consultorios(models.Model):
    nombre = models.CharField(max_length=30)


    def __str__(self):
        return self.nombre


class HorarioAtencion(models.Model):
    """
        Definicion de Horarios de Atencion del Medico
    """
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    duracion_turno = models.TimeField() #duracion en minutos
    intervalo = models.TimeField() #entretiempo entre turnos por defecto es 0

    #FK
    cod_medico = models.ForeignKey(Medicos)
    cod_expecialidad = models.ForeignKey(Expecialidades)


    def __str__(self):
        f_cad = "[ %s | Desde: %s | Hasta: %s ]" %(str(self.dia), str(self.hora_inicio), str(self.hora_fin))
        return f_cad


class DiasAtencion(models.Model):
    """
        Horario de Atencion en un dia Particular
    """
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cant_turno = models.IntegerField() #total de turnos asignados

    #opcionales todavia no definidos si se agregaran
    duracion_turno = models.TimeField() #duracion en minutos
    intervalo = models.TimeField() #entretiempo entre turnos

    #fk
    cod_medico = models.ForeignKey(Medicos)


class Turnos(models.Model):
    """
        Objecto q representa los turnos asignados
    """
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    comentarios = models.TextField()

    #fk
    codigo_paciente = models.ForeignKey(Pacientes)
    codigo_medico = models.ForeignKey(Medicos)


class SolitudesTurnos(models.Model):
    """
        Solicitudes de Turnos q realizan los Pacientes
    """
    fecha_solicitud = models.DateField() #fecha en la q se solicito el turno
    fecha_requerida = models.DateField()#fecha para la cual se solicito turno
    estado = models.CharField(max_length=1, default='P' ,choices=SOLICITUD_ESTADO)
    comentarios = models.TextField()

    #fk
    codigo_paciente = models.ForeignKey(Pacientes)
    codigo_medico = models.ForeignKey(Medicos)