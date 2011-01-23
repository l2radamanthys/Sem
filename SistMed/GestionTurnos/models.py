#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from constantes import SEXO_CHOICE, SOLICITUD_ESTADO_CHOICE


#modelos
class TipoUsuario(models.Model):
    """
        En ves de crear las clases Medico, Paciente, Administrativo
       cree una clase categoria q le definira la clase al paciente
    """
    nombre = models.CharField("Tipo",max_length=15)


    def __str__(self):
        return self.nombre


class Expecialidades(models.Model):
    """
        Clasificacion de las expecialidades de todos los medicos
    """
    nombre = models.CharField(max_length=30)


    def __str__(self):
        return self.nombre


class Usuarios(models.Model):
    """
        Para el login y el manejo de secciones
    """
    dni = models.IntegerField()
    sexo = models.CharField(max_length=1, default='-', choices=SEXO_CHOICE)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=60)

    #FK
    #tipo usuario (paciente, medico, administrativo)
    tipo_usuario = models.ForeignKey(TipoUsuario)
    #segun django.es de esta forma anda con la clase user
    #yo queria usar herencia :(
    user = models.ForeignKey(User, unique=True)


    def username(self):
        """
            devuelve el nombre de usuario
        """
        return self.user.username


    def nombre_completo(self):
        """
            Nombre completo del paciente
        """
        return self.user.first_name + " " + self.user.last_name

        
    def tipo(self):
        return self.tipo_usuario.nombre


    def tipo_id(self):
        return self.tipo_usuario.id


    def __str__(self):
        return self.username()


class Medicos(Usuarios):
    matricula = models.CharField(max_length=30)

    def __str__(self):
        return "Med - %s" %self.username()


class Pacientes(Usuarios):
    #por el momento no tiene canpos adjuntos mas adelantes tendra mas..
    #cuando implemente la parte de Historia Clinica :P
    pass


    def __str__(self):
        return "Pac - %s" %self.username()


class Administrativos(Usuarios):
    pass


    def __str__(self):
        return "Adm - %s" %self.username()



class ExpecialidadesMedicos(models.Model):
    """
        Clasificacion de las Distintas Expecialidades de los Medicos
    """
    #fk
    codigo_medico = models.ForeignKey(Medicos)
    cod_expecialidad = models.ForeignKey(Expecialidades)


    def __str__(self):
        return "%s - %s" %(self.codigo_medico, self.cod_expecialidad)
    

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
        f_cad = "[Fecha: %s | Desde: %s | Hasta: %s ]" %(str(self.dia), str(self.hora_inicio), str(self.hora_fin))
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


    def n_turno(self):
        """
            devuelve los datos de un nuevo turno
        """
        #no implementado
        self.cant_turno += 1
        self.save()


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
    estado = models.CharField(max_length=1, default='P' ,choices=SOLICITUD_ESTADO_CHOICE)
    comentarios = models.TextField()

    #fk
    codigo_paciente = models.ForeignKey(Pacientes)
    codigo_medico = models.ForeignKey(Medicos)
