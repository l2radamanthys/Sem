#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

#Modelo Base version intermedia


class InformacionBasica(models.Model):
    """
        Datos identificatorios basicos del Paciente
    """
    #los sig datos se obtienen directamente del usuario q se asigna
    #- Nombre y Apellido
    #- Email
    dni = models.IntegerField()
    sexo = models.CharField(max_length=1, default='-', choices=SEXO_CHOICE)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=60)

    fecha_nacimiento = models.CharField('Fecha Nacimiento')
    lugar_nacimiento = models.CharField()
    grupo_sanguineo = models.CharField()

    estado_civil = models.CharField()
    ocupacion = models.CharField()
    religion = models.CharField()

    motivo_consulta = models.CharField()#TEXT
    antecedentes_enfermedad_actual = models.CharField()#TEXT

    user = models.ForeignKey(User, unique=True)

class AntecedentesPerinatales(models.Model):
    """
        Referentes al nacimiento
    """
    hist_clinica = models.ForeignKey(InformacionBasica)
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
    hist_clinica = models.ForeignKey(InformacionBasica)
    fecha = models.DateTimeField()#fecha q se realizo el examem

    alcohol = models.CharField() #S/N
    tabaco = models.CharField()#S/N
    drogas = models.CharField()#S/N
    infuciones = models.CharField()#S/N
    observaciones = models.TextField()#text


#Examen Fisico
class ExamenFisico:
    hist_clinica = models.ForeignKey(InformacionBasica)
    fecha = models.DateTimeField()#fecha q se realizo el examem


class ExamenBase:
    """
        Examen Fisico Basico
    """
    examen_fisico = models.ForeignKey(ExamenFisico, unique=True)

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
        Examen Fisico - Analisis de Piel, Faneas y Tejido Subcutaneo
    """
    examen_fisico = models.ForeignKey(ExamenFisico, unique=True)

    aspecto = models.TextField('Aspecto')
    dist_pilosa = models.TextField('Distribucion Pilosa')
    leciones = models.TextField('Leciones')
    faneras = models.TextField('Faneras')
    tejido_cel_subcutaneo = models.TextField('Tejido Celular Subcutaneo')


#Examen Fisico
class Cabeza():
    """
        Examen Fisico - Cabeza
    """
    examen_fisico = models.ForeignKey(ExamenFisico, unique=True)

    craneo = models.CharField()  #N/A Normal - Alterado
    fontanelas_y_suturas = models.CharField()  #N/A Normal - Alterado
    facie = models.CharField()  #N/A Normal - Alterado
    parpados = models.CharField()  #N/A Normal - Alterado
    conjuntivas = models.CharField()  #N/A Normal - Alterado
    globo_ocular_mov = models.CharField()  #N/A Normal - Alterado
    vision = models.CharField()  #N/A Normal - Alterado
    nariz_fosas_nasales = models.CharField()  #N/A Normal - Alterado
    labios = models.CharField()  #N/A Normal - Alterado
    dientes = models.CharField()  #N/A Normal - Alterado
    lengua = models.CharField()  #N/A Normal - Alterado
    mucosa_bucofaringea = models.CharField()  #N/A Normal - Alterado
    amigdalas = models.CharField()  #N/A Normal - Alterado
    pabellones_auriculares = models.CharField()  #N/A Normal - Alterado
    cond_audit_externo = models.CharField()  #N/A Normal - Alterado
    timpanos = models.CharField()  #N/A Normal - Alterado
    audicion = models.CharField()  #N/A Normal - Alterado
    observaciones = models.TextField('Observaciones')


#Examen Fisico
class Cuello:
    """
        Examen Fisico - Cuello
    """
    examen_fisico = models.ForeignKey(ExamenFisico, unique=True)

    inspecion = models.CharField('Inspecion')
    palpacion = models.CharField('Palpacion')
    percucion = models.CharField('Percucion')
    ausculacion = models.CharField('Ausculacion')
    observaciones = models.TextField('Observaciones')



#Examen Fisico
class ToraxAparatoRespiratorio:
    """
        Examen Fisico - Torax y Aparato Respiratorio
    """
    examen_fisico = models.ForeignKey(ExamenFisico, unique=True)

    inspecion = models.CharField('Inspecion')
    palpacion = models.CharField('Palpacion')
    percucion = models.CharField('Percucion')
    ausculacion = models.CharField('Ausculacion')
    piel = models.CharField()
    tipo_respiracion = models.CharField()
    tiraje = models.CharField()
    uso_musculos_accesorios = models.CharField()
    #semiologia omitido por el momentos

    observaciones = models.TextField('Observaciones')


#Examen Fisico
class AparatoCardiovascular:
    """
        Examen Fisico - Aparato Cardio Vascular
    """
    hist_clinica = models.ForeignKey(InformacionBasica)
    fecha = models.DateTimeField()#fecha q se realizo el examem
    
    latidos =
    choque_de_punta
    R1
    R2
    R3
    R4
    soplos
    chasquidos
    
    #pulso
    pulso_carotideo_izq
    pulso_carotideo_der
    pulso_humeral_izq
    pulso_humeral_der
    pulso_radial_izq
    pulso_radial_der
    pulso_femoral_izq
    pulso_femoral_der
    pulso_popliteo_izq
    pulso_popliteo_der
    pulso_tibial_posterior_izq
    pulso_tibial_posterior_der
    pulso_pedio_izq
    pulso_pedio_der


#Examen Fisico
class AbdomenPelvis:
    examen_fisico = models.ForeignKey(ExamenFisico, unique=True)
    #falta
    observaciones = models.TextField('Observaciones')


#Examen Fisico
class SistemaOsteoArticular:
    """
        Examen Fisico - Sistema Osteo Articular
    """
    examen_fisico = models.ForeignKey(ExamenFisico, unique=True)

    columna_vertebral = models.CharField()
    miembros = models.CharField()
    ejes_oseos = models.CharField()
    articulaciones = models.CharField()
    trofismo_muscular = models.CharField() 
    observaciones = models.TextField('Observaciones')


#Examen Fisico
class SistemaNeuroMuscular:
    examen_fisico = models.ForeignKey(ExamenFisico, unique=True)
    #falta
    observaciones = models.TextField('Observaciones')



#Examen Fisico
class OtrosEstudio:
    examen_fisico = models.ForeignKey(ExamenFisico, unique=True)
    fecha = models.DateField()#fecha q se realizo el examem
    descripcion = models.TextField('Descripcion')


class Imagen:
    examen_fisico = models.ForeignKey(ExamenFisico, unique=True)
    imagen =
    descripcion = models.TextField()
    
   
class AnalisisLaboratorio:
    hist_clinica = models.ForeignKey(InformacionBasica)
    pass


class Diagnostico:
    hist_clinica = models.ForeignKey(InformacionBasica)
    fecha =
    observaciones =


class ConsultaMedica:
    hist_clinica = models.ForeignKey(InformacionBasica)
    fecha = models.DateField()
    pass


class MedicamentosRecetados:
    hist_clinica = models.ForeignKey(InformacionBasica)
    consulta_medica = models.ForeignKey(ConsultaMedica)
    medicamento = models.CharField()
    prescripcion = models.TextField()