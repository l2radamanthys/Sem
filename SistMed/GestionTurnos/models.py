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
class Usuarios(User):
    """
        Para el login y el manejo de secciones
    """
    dni = models.IntegerField('DNI')
    sexo = models.CharField('Sexo', max_length=1, choice=SEXO_CHOICE, default='-')
    telefono = models.CharField('Nro de telefono', max_length=20)
    
    #esta categoria sera utilizada solo en caso de q el tipo de usuario sea Medico
    matricula = models.CharField('Matricula Medica')

    #FK y PK
    tipo = models.ForeignKey(TipoUsuario)
    

    #renombrados para mayor comodidad
    nombre = first_name
    apellido = last_name

    #datos para recordar
    #username, password


    def nombre_completo(self):
        return self.first_name + self.last_name


    def __str__(self):
        return self.username


class TipoUsuario(models.Model):
    """
        En ves de crear las clases Medico, Paciente, Administrativo
        cree una clase categoria q le definira la clase al paciente
    """
    nombre = models.CharField('Nombre Tipo Usuario', max_length=30)


#remplazadas por la clase categoria
#class Medico(models.Model):
#    pass
#class Paciente(models.Model):
#    pass
#class Administrativo(models.Model):
#    pass


class Expecialidades(models.Model):
    """
        Clasificacion de las expecialidades de todos los medicos
    """
    nombre = models.CharField('Nombre')

    
    def __str__(self):
        return self.nombre


class ExpecialidadesMedicos(models.Model):
    """
        Clasificacion de las Distintas Expecialidades de los Medicos
    """
    #fk
    codigo_medico = models.ForeignKey(Usuarios)
    cod_expecialidad = models.ForeignKey(Expecialidades)


#sin usar por el momento
class Consultorios(models.Model):
    nombre = models.CharField()


    def __str__(self):
        return self.nombre


class HorarioAtencion(models.Model):
    """
        Definicion de Horarios de Atencion del Medico
    """
    dia = models.CharField()
    hora_inicio = models.CharField()
    hora_fin = models.CharField()
    duracion_turno = models.CharField() #duracion en minutos
    intervalo = models.CharField() #entretiempo entre turnos

    #FK
    cod_medico = models.ForeignKey(Usuarios)
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
    cant_turno = models.CharField() #total de turnos asignados

    #opcionales todavia no definidos si se agregaran
    duracion_turno = models.TimeField() #duracion en minutos
    intervalo = models.TimeField() #entretiempo entre turnos

    #fk
    cod_medico = models.ForeignKey(Usuarios)


class Turnos(models.Model):
    """
        Objecto q representa los turnos asignados
    """
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    comentarios = models.TextField()

    #fk
    cod_paciente = models.ForeignKey(Usuarios)
    cod_medico = models.ForeignKey(Usuarios)


class SolitudesTurnos(models.Model):
    """
        Solicitudes de Turnos q realizan los Pacientes
    """
    fecha_solicitud = models.DateField() #fecha en la q se solicito el turno
    fecha_requerida = models.DateField()#fecha para la cual se solicito turno
    estado = models.CharField(lechoice=SOLICITUD_ESTADO, max_length=1, default='P')
    comentarios = models.TextField()

    #fk
    cod_paciente = models.ForeignKey(Usuarios)
    cod_medico = models.ForeignKey(Usuarios)