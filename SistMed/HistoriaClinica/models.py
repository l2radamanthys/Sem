#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

#Modelo Base version intermedia


class InformacionBasica(models.Model):
    """
        Datos identificatorios basicos del Paciente
    """
    #el nombre de la clase no es le final

    #los sig datos se obtienen directamente del usuario q se asigna
    #- Nombre y Apellido
    #- DNI
    #- Sexo
    #- Email
    #- telefono
    #- direccion

    fecha_nacimiento = models.CharField('Fecha Nacimiento')
    lugar_nacimiento = models.CharField()
    grupo_sanguineo = models.CharField()

    estado_civil = models.CharField()
    ocupacion = models.CharField()
    religion = models.CharField()

    motivo_consulta = models.CharField()#TEXT
    antecedentes_enfermedad_actual = models.CharField()#TEXT


class AntecedentesPerinatales(models.Model):
    """
        Referentes al nacimiento
    """
    nro_historia_clinica = #FK 1-1
    enbarazo_nro = models.CharField()
    duracion_embarazo = models.CharField() #en semanas
    controles = models.CharField() #si tubo controles durante el embarazo
    parto_normal = models.CharField('Nacio de Parto Normal') #si nacio parto normal o cesareas
    peso = models.CharField('Peso al Nacer') #peso al nacer
    talla = models.CharField('Talla')
    patologias = models.CharField('Patologias al Nacer') #al nacerS/N
    atencion_medica = models.CharField('Requirio Atencion Medica')# requirio atencion medica S/N
    otros_datos = models.TextField('Otros Datos de Relevancia') #otra informacion relevante


#antecedentes personales
class HabitosToxicos(models.Model):
    """
        Habitos toxicos del paciente
    """
    nro_historia_clinica = #FK 1-1
    alcohol = models.CharField() #S/N
    tabaco = models.CharField()#S/N
    drogas = models.CharField()#S/N
    infuciones = models.CharField()#S/N
    comentarios= models.TextField()#text


#Examen Fisico
class ExamenFisicoBase:
    """
        Examen Fisico Basico
    """
    nro_historia_clinica = #FK 1-M
    fecha = models.CharField()#fecha q se realizo el examem

    #signos vitales
    FC = models.CharField()
    TA = models.CharField()
    FR = models.CharField()
    pulso = models.CharField()

    peso_habitual = models.CharField()
    peso_actual = models.CharField()
    talla = models.CharField()
    BMI = models.CharField()
    imprecion_general = models.CharField() #text


#Examen Fisico
class PielFaneasTejidoCelularSubcutaneo:
    #tengo q buscarle un nombre mas corto
    """
        Analisis de Piel, Faneas y Tejido Subcutaneo
    """
    nro_historia_clinica = #FK 1-M
    fecha = models.CharField()#fecha q se realizo el examem

    aspecto = models.TextField('Aspecto')
    dist_pilosa = models.TextField('Distribucion Pilosa')
    leciones = models.TextField('Leciones')
    faneras = models.TextField('Faneras')
    tejido_cel_subcutaneo = models.TextField('Tejido Celular Subcutaneo')


#Examen Fisico
class Cabeza():
    craneo = #N/A Normal - Alterado
    fontanelas_y_suturas
    facie
    parpados
    conjuntivas
    globo_ocular_mov
    vision
    nariz_fosas_nasales
    labios
    dientes
    lengua
    mucosa_bucofaringea
    amigdalas
    pabellones_auriculares
    cond_audit_externo
    timpanos
    audicion
    info_adicional = models.TextField('informacion Adicional')


#Examen Fisico
class Cuello:
    pass


#Examen Fisico
class ToraxAparatoRespiratorio:
    pass


#Examen Fisico
class AparatoCardiovascular:
    pass


#Examen Fisico
class AbdomenPelvis:
    pass


#Examen Fisico
class SistemaOsteoArticular:
    pass


#Examen Fisico
class SistemaNeuroMuscular:
    pass




