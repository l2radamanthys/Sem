#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from django.db import connection, transaction

from utils import *
from constantes import *


#modelos
class TipoUsuario(models.Model):
    """
        En ves de crear las clases Medico, Paciente, Administrativo
       cree una clase categoria q le definira la clase a los diferentes
       tipo de usuario para definir permisos
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


class TipoDocumento:
    """
        tipo documento
    """
    nombre = models.CharField("nombre", max_length=150)

    
    def __str__(self):
        return self.nombre


class Usuarios(models.Model):
    """
        Para el login y el manejo de secciones
    """
    dni = models.IntegerField()
    #nro_doc = models.ChardField("Nro Documento", max_lenght="5")
    tipo_doc = user = models.CharField("Tipo Documento", max_length="5", choices=TIPO_DOC_CHOICE, default="--")
    sexo = models.CharField(max_length=1, default='-', choices=SEXO_CHOICE)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=60)

    #FK
    #tipo usuario (paciente, medico, administrativo)
    tipo_usuario = models.ForeignKey(TipoUsuario)
    #segun django.es de esta forma anda con la clase user yo queria usar herencia :( pero no funka asi -.-
    user = models.ForeignKey(User, unique=True)


    def doc(self):
        return "%s - %s" %(self.tipo_doc, self.dni)


    def username(self):
        """
            devuelve el nombre de usuario
        """
        return self.user.username


    def nombre_completo(self):
        """
            Nombre completo del paciente
        """
        nombre = self.user.first_name + " " + self.user.last_name
        if len(nombre) > 5:
            return nombre
        else:
            return "<None>"

        
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
    """
    por el momento no tiene canpos adjuntos mas adelantes tendra mas..
    cuando implemente la parte de Historia Clinica :P pero eso datos
    estaran alli
    """
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
    cod_expecialidad = models.ForeignKey(Expecialidades)#, unique=True)


    def __str__(self):
        return "%s - %s" %(self.codigo_medico, self.cod_expecialidad)


    def esp_not_in_medico_sql(self, med_id=-1):
        """
            Consulta SQL Cruda
            Devuelve un Array con todas las Especialidades q no fueron
            asigandas al medico
        """
        #no se implemento por que encontre una manera alternativa de hacerlo
        #sin tener q recurrir a consultas crudas de SQL

        #cursor = connection.cursor()
        #query = """
        #SELECT *
        #FROM GestionTurnos_expecialidades
        #WHERE """
        #cursor.execute(query)
        pass


class Consultorios(models.Model):
    """
        Aunq el modelo fue definido, el mismo no se va a implementar por
        el momento.. tal ves en proximas revisiones sea implementado
    """
    #sin usar por el momento
    nombre = models.CharField(max_length=30)


    def __str__(self):
        return self.nombre


class HorarioAtencion(models.Model):
    """
        Definicion de Horarios de Atencion del Medico
    """
    dia = models.CharField('Dia', max_length=4, default='LUN', choices=DATE_CHOICE)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    duracion_turno = models.IntegerField(default=15) #duracion en minutos del turno por defecto 15 min
    intervalo = models.IntegerField(default=0) #entretiempo entre turnos por defecto es 0 (es en minutos)

    #FK
    medico = models.ForeignKey(Medicos)
    #cod_expecialidad = models.ForeignKey(Expecialidades) //para que no sea tan complicado no tomara en cuenta expecialidades


    def __str__(self):
        f_cad = "[Fecha: %s | Desde: %s | Hasta: %s ]" %(str(self.dia), str(self.hora_inicio), str(self.hora_fin))
        return f_cad


class DiasAtencion(models.Model):
    """
        Horario de Atencion en un dia Particular
    """
    fecha = models.DateField()
    cant_turno = models.IntegerField() #contador de turnos asignados
    ##estos datos se obtienen del horario
    #hora_inicio = models.TimeField()
    #hora_fin = models.TimeField()
    #duracion_turno = models.TimeField() #duracion en minutos
    #intervalo = models.TimeField() #entretiempo entre turnos

    #fk
    medico = models.ForeignKey(Medicos)
    horario_atenc = models.ForeignKey(HorarioAtencion)
    

    def n_turno(self):
        """
            devuelve los datos de un nuevo turno
        """
        #no implementado
        #self.cant_turno += 1
        #self.save()
        pass


    def h_ini(self):
        """
            Retorna un String con la Hora Inicio del Horario de Atencion
            en formato hh:mm
        """
        return self.hora_inicio.strftime("%H:%M")


    def h_fin(self):
        """
            Retorna un String con la Hora Finalizacion del Horario de
            Atencion en formato hh:mm
        """
        return self.hora_fin.strftime("%H:%M")


class Turnos(models.Model):
    """
        Objecto q representa los turnos asignados
    """
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    comentarios = models.TextField()

    #fk
    paciente = models.ForeignKey(Pacientes)
    medico = models.ForeignKey(Medicos)


class SolitudesTurnos(models.Model):
    """
        Solicitudes de Turnos q realizan los Pacientes
    """
    fecha_solicitud = models.DateField(auto_now_add=True) #fecha en la q se solicito el turno
    fecha_requerida = models.DateField()#fecha para la cual se solicito turno
    estado = models.CharField(max_length=1, default='P' ,choices=SOLICITUD_ESTADO_CHOICE)
    comentarios = models.TextField()

    #fk
    codigo_paciente = models.ForeignKey(Pacientes)
    codigo_medico = models.ForeignKey(Medicos)


    def date_sol(self):
        return date_to_str(self.fecha_solicitud)


    def date_req(self):
        return date_to_str(self.fecha_requerida)