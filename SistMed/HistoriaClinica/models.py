#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


from GestionTurnos.models import Pacientes, Medicos
from constantes import *
from constantes import _MEDIA_ROOT
from utils import date_to_str


class InformacionBasica(models.Model):
    """
        Datos identificatorios basicos del Paciente
    """
    #los sig datos se obtienen directamente del usuario q se asigna
    #- Nombre y Apellido
    #- Email
    #- dni
    #- sexo

    fecha_nacimiento = models.DateTimeField('Fecha Nacimiento')
    lugar_nacimiento = models.CharField('Lugar Nacimiento', max_length=60)
    grupo_sanguineo = models.CharField('Grupo Sanguineo', max_length=3, default='--', choices=GRUPO_SANGUINEO_CHOICE)

    #complementos agregados
    padre = models.CharField('Padre', max_length=120)
    madre = models.CharField('Madre', max_length=120)
    obra_social = models.CharField('Obra Social', max_length=30)
    nro_afiliado = models.CharField('Nro Afiliado', max_length=10)

    estado_civil = models.CharField('Estado Civil', max_length=1, default='-', choices=ESTADO_CIVIL_CHOICE)
    ocupacion = models.CharField(max_length=30)
    religion = models.CharField(max_length=30)

    motivo_consulta = models.TextField()
    antecedentes_enfermedad_actual = models.TextField()

    #fk datos paciente...
    paciente = models.ForeignKey(Pacientes, unique=True)


class AntecedentesPerinatales(models.Model):
    """
        Referentes al nacimiento
    """
    hist_clinica = models.ForeignKey(InformacionBasica)
    enbarazo_nro = models.IntegerField('Embarazo Nro')
    duracion_embarazo = models.IntegerField('Duracion/Semanas') #en semanas
    controles = models.CharField('Controles Durante Embarazo', max_length=1, choices=TRUE_FALSE_CHOICE) #si tubo controles durante el embarazo
    parto_normal = models.CharField('Parto Normal', max_length=1, choices=TRUE_FALSE_CHOICE) #si nacio parto normal o cesareas
    peso = models.FloatField('Peso al Nacer') #peso al nacer
    talla = models.FloatField('Talla')
    patologias = models.CharField('Presento Patologias al Nacer', max_length=1, choices=TRUE_FALSE_CHOICE) #al nacer S/N
    atencion_medica = models.CharField('Requirio Atencion Medica', max_length=1, choices=TRUE_FALSE_CHOICE)# requirio atencion medica S/N
    otros_datos = models.TextField('Otros Datos de Relevancia o Informacion Adicional') #otra informacion relevante


#carnet de vacunacion
class Vacuna(models.Model):
    """
        Para el Carnet de Vacunacion
    """
    hist_clinica = models.ForeignKey(InformacionBasica)
    
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=30)
    tipo_dosis = models.CharField(max_length=3, default='---', choices=TIPO_DOSIS_CHOICE)


    def date(self):
        """
        """
        return fecha.strftime('%d/%m/%Y')



#Examen Fisico
class ExamenBase(models.Model):
    """
        Examen Fisico Basico
    """
    hist_clinica = models.ForeignKey(InformacionBasica)
    fecha = models.DateTimeField()#fecha q se realizo el examem

    #signos vitales
    temp_corporal = models.FloatField("Temperatura Corporal")
    pres_art_sist = models.IntegerField("Presion Arterial Sistolica")
    pres_art_diast = models.IntegerField("Presion Arterial Dastolica")
    frec_respiratoria = models.IntegerField("Frecuencia Respiratoria")
    pulso = models.IntegerField("Pulso")

    peso_medio = models.FloatField()
    altura_media = models.FloatField()
    peso = models.FloatField()
    altura = models.FloatField()
    talla = models.CharField(max_length=30)
    bmi = models.FloatField("Indice de Masa Corporal") #indice de masa corporal
    imprecion_general = models.TextField() #text


    #calculado segun info obtenida en la siguiente presentacion
    #http://www.slideshare.net/lSpical/5examen-fisico-signos-vitales-y-apreciacion-general
    def presion_art_pulso(self):
        """
        """
        return pres_art_sist - pres_art_diast


    def presion_art_media(self):
        """
        """
        return pres_art_diast + (self.pres_art_pulso() / 3)

    
    def date(self):
        """
        """
        return self.fecha.strftime('%d/%m/%Y')


    def __str__(self):
        return "Examen Realizado el: %s" %date_to_str(self.fecha)


#Examen Fisico
class HabitosToxicos(models.Model):
    """
        Habitos toxicos del paciente
    """
    examen_fisico = models.ForeignKey(ExamenBase)
    fecha = models.DateTimeField()#fecha q se realizo el examem

    alcohol = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE) #S/N
    tabaco = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)#S/N
    drogas = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)#S/N
    infuciones = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)#S/N
    observaciones = models.TextField('Observaciones')#text


#Examen Fisico
class PielFaneasTejidoCelularSubcutaneo(models.Model):
    #tengo q buscarle un nombre mas corto
    """
        Examen Fisico - Analisis de Piel, Faneas y Tejido Subcutaneo
    """
    examen_fisico = models.ForeignKey(ExamenBase, unique=True)

    aspecto = models.TextField('Aspecto')
    dist_pilosa = models.TextField('Distribucion Pilosa')
    lesiones = models.TextField('Leciones')
    faneras = models.TextField('Faneras')
    tejido_cel_subcutaneo = models.TextField('Tejido Celular Subcutaneo')


#Examen Fisico
class Cabeza(models.Model):
    """
        Examen Fisico - Cabeza
    """
    examen_fisico = models.ForeignKey(ExamenBase)
    craneo = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    fontanelas_y_suturas = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    facie = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    parpados = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    conjuntivas = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    globo_ocular_mov = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    vision = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    nariz_fosas_nasales = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    labios = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    dientes = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    lengua = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    mucosa_bucofaringea = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    amigdalas = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    pabellones_auriculares = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    cond_audit_externo = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    timpanos = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    audicion = models.CharField(max_length=1, default='-', choices=ESTADO_CHOICE)  #N/A Normal - Alterado
    observaciones = models.TextField('Observaciones')


#Examen Fisico
class Cuello(models.Model):
    """
        Examen Fisico - Cuello
    """
    examen_fisico = models.ForeignKey(ExamenBase)
    inspecion = models.CharField('Inspecion', max_length=250)
    palpacion = models.CharField('Palpacion', max_length=250)
    percucion = models.CharField('Percucion', max_length=250)
    ausculacion = models.CharField('Ausculacion', max_length=250)
    observaciones = models.TextField('Observaciones')


'''
#Examen Fisico
class ToraxAparatoRespiratorio:
    """
        Examen Fisico - Torax y Aparato Respiratorio
    """
    examen_fisico = models.ForeignKey(ExamenBase, unique=True)

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
    hist_clinica = models.ForeignKey(ExamenBase)
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
    examen_fisico = models.ForeignKey(ExamenBase, unique=True)
    #falta
    observaciones = models.TextField('Observaciones')


#Examen Fisico
class SistemaOsteoArticular:
    """
        Examen Fisico - Sistema Osteo Articular
    """
    examen_fisico = models.ForeignKey(ExamenBase, unique=True)

    columna_vertebral = models.CharField()
    miembros = models.CharField()
    ejes_oseos = models.CharField()
    articulaciones = models.CharField()
    trofismo_muscular = models.CharField()
    observaciones = models.TextField('Observaciones')


#Examen Fisico
class SistemaNeuroMuscular:
    examen_fisico = models.ForeignKey(ExamenBase, unique=True)
    #falta
    observaciones = models.TextField('Observaciones')
'''


#Examen Fisico
class OtrosEstudio(models.Model):
    examen_fisico = models.ForeignKey(ExamenBase, unique=True)
    fecha = models.DateField()#fecha q se realizo el examem
    descripcion = models.TextField('Descripcion')


class Imagen(models.Model):
    examen_fisico = models.ForeignKey(ExamenBase)
    titulo = models.CharField('titulo', max_length=250)
    descripcion = models.TextField('Descripcion')
    imagen = models.ImageField(upload_to="estudios/imagenes")


'''
class AnalisisLaboratorio:
    hist_clinica = models.ForeignKey(InformacionBasica)
    pass
'''


class Diagnostico(models.Model):
    hist_clinica = models.ForeignKey(InformacionBasica)
    fecha = models.DateField()
    observaciones = models.TextField()
    #observaciones =



class ConsultaMedica(models.Model):
    hist_clinica = models.ForeignKey(InformacionBasica)
    fecha = models.DateTimeField()
    observaciones = models.TextField()
    #fk
    #paciente = models.ForeignKey(Pacientes) al pedo -.-
    medico = models.ForeignKey(Medicos)

    def fecha_(self):
        return  date_to_str(self.fecha)


#tipica receta
"""
class Receta(models.Model):
    #hist_clinica = models.ForeignKey(InformacionBasica)
    consulta_medica = models.ForeignKey(ConsultaMedica)
    medicamento = models.CharField("Medicamento", max_lenght=250)
    prescripcion = models.TextField()
"""
