#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls.defaults import *

#site admin
from django.contrib import admin
admin.autodiscover()

#propios
from settings import MEDIA_ROOT

import generics_views
from GestionTurnos import pacientes_views, admin_views, medicos_views
from GestionTurnos import especialidades_views, turnos_views
from HistoriaClinica import medicos_views as hc_med_views


urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include('django.contrib.admin.urls')),
    (r'^admin/', include(admin.site.urls)),

    #media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes': True }),

    #Pagina inicio
    (r'^/?$', generics_views.index),

    ## - Sessiones - ##
    (r'^accounts/login/$', generics_views.login),
    (r'^accounts/logout/$', generics_views.logout),
    (r'^accounts/change_password/$', generics_views.cambio_contrasenia),
    (r'^accounts/datos-personales/$', generics_views.datos_personales),
    (r'^accounts/modificar-datos-personales/$', generics_views.datos_personales_modificar),


    ## - Gestion Turnos - ##
    # - Pacientes Views
    (r'^pacientes/nuevo/$', pacientes_views.nuevo_paciente),
    (r'^pacientes/listado/$', pacientes_views.listado_pacientes),
    (r'^pacientes/datos/$', pacientes_views.datos_paciente),
    (r'^pacientes/datos/(\d{1,2})/$', pacientes_views.datos_paciente),
    (r'^pacientes/modificar/$', pacientes_views.modificar_paciente),
    (r'^pacientes/modificar/(\d{1,2})/$', pacientes_views.modificar_paciente),
    (r'^pacientes/guardar/$', pacientes_views.guardar_cambios_paciente),
    (r'^pacientes/guardar/(\d{1,2})/$', pacientes_views.guardar_cambios_paciente),
    (r'^pacientes/borrar/$', pacientes_views.borrar_paciente),
    (r'^pacientes/borrar/(\d{1,2})/$', pacientes_views.borrar_paciente),
    (r'^pacientes/borrado/$', pacientes_views.borrado_paciente),
    (r'^pacientes/borrado/(\d{1,2})/$', pacientes_views.borrado_paciente),
    (r'^pacientes/buscar/$', pacientes_views.buscar_pacientes),


    # - Medicos Views
    (r'^medicos/nuevo/$', medicos_views.nuevo_medico),
    (r'^medicos/listado/$', medicos_views.listado_medicos),
    (r'^medicos/datos/$', medicos_views.datos_medico),
    (r'^medicos/datos/(\d{1,2})/$', medicos_views.datos_medico),
    (r'^medicos/modificar/$', medicos_views.modificar_medico),
    (r'^medicos/modificar/(\d{1,2})/$', medicos_views.modificar_medico),
    (r'^medicos/guardar/$', medicos_views.guardar_cambios_medico),
    #(r'^medicos/guardar/(\d{1,2})/$', medicos_views.guardar_cambios_medico),
    (r'^medicos/borrar/$', medicos_views.borrar_medico),
    (r'^medicos/borrar/(\d{1,2})/$', medicos_views.borrar_medico),
    (r'^medicos/borrado/$', medicos_views.borrado_medico),
    (r'^medicos/borrado/(\d{1,2})/$', medicos_views.borrado_medico),
    (r'^medicos/buscar/$', medicos_views.buscar_medicos),
    (r'^medicos/agregar-especialidades/$', medicos_views.agregar_especialidad),
    (r'^medicos/agregar-especialidades/(\d{1,2})/$', medicos_views.agregar_especialidad),
    (r'^medicos/borrar-especialidad/$', medicos_views.borrar_expecialidad),

    # - Medicos - Especialidades
    (r'^medicos/especialidades/agregar/$', especialidades_views.agregar),
    (r'^medicos/especialidades/listado/$', especialidades_views.listado),
    (r'^medicos/especialidades/borrar/$', especialidades_views.borrar),
    (r'^medicos/especialidades/borrar/(\d{1,2})/$', especialidades_views.borrar),
    (r'^medicos/especialidades/borrado/$', especialidades_views.borrado),
    (r'^medicos/especialidades/borrado/(\d{1,2})/$', especialidades_views.borrado),

    # - Medicos - Dia Atencion
    (r'^medicos/horario-atencion/agregar/$', medicos_views.agregar_horario_atencion),
    (r'^medicos/horario-atencion/agregar/(\d{1,2})/$', medicos_views.agregar_horario_atencion),
    #(r'^medicos/dias-atencion/modificar/$', medicos_views.borrar_medico),'
    #(r'^medicos/dias-atencion/modificar/(\d{1,2})/$', medicos_views.borrar_medico),
    #(r'^medicos/dias-atencion/guardar/$', medicos_views.borrar_medico),'
    #(r'^medicos/dias-atencion/guardar/(\d{1,2})/$', medicos_views.borrar_medico),
    #r'^medicos/dias-atencion/borrar/$', medicos_views.agregar_dia_atencion),
    #r'^medicos/dias-atencion/borrar/(\d{1,2})/$', medicos_views.borrar_dia_atencion),

    # - Medico - Agenda
    (r'^medicos/agenda/agregar-turno/$', turnos_views.nuevo_turno),
    (r'^medicos/agenda/mostrar-por-dia/$', turnos_views.mostrar_agenda_por_dia),


    # - Administrativos Views
    (r'^administrativos/nuevo/$', admin_views.nuevo_admin),
    (r'^administrativos/listado/$', admin_views.listado_admins),
    (r'^administrativos/datos/$', admin_views.datos_admin),
    (r'^administrativos/datos/(\d{1,2})/$', admin_views.datos_admin),
    (r'^administrativos/modificar/$', admin_views.modificar_admin),
    (r'^administrativos/modificar/(\d{1,2})/$', admin_views.modificar_admin),
    (r'^administrativos/guardar/$', admin_views.guardar_cambios_admin),
    (r'^administrativos/guardar/(\d{1,2})/$', admin_views.guardar_cambios_admin),
    (r'^administrativos/borrar/$', admin_views.borrar_admin),
    (r'^administrativos/borrar/(\d{1,2})/$', admin_views.borrar_admin),
    (r'^administrativos/borrado/$', admin_views.borrado_admin),
    (r'^administrativos/borrado/(\d{1,2})/$', admin_views.borrado_admin),
    (r'^administrativos/buscar/$', admin_views.buscar_admins),

    # - Turnos
    (r'^pacientes/turnos/nueva-solicitud/$', turnos_views.nueva_solicitud_turno),
    (r'^pacientes/turnos/listado-solicitudes/$', turnos_views.listado_solicitudes_turno_pac),
    (r'^pacientes/turnos/mostrar-solicitud/$', turnos_views.detalle_solicitud_turno_pac),
    (r'^medicos/turnos/listado-solicitudes/(\d{1,2})/$', turnos_views.listado_solicitudes_turno),


    #(r'^medicos/agenda/agregar-turno/$', turnos_views.nuevo_turno),
    (r'^medicos/turnos/nuevo-turno/$', generics_views.error404),
    (r'^medicos/turnos/nuevo-turno/(\d{1,2})/$', turnos_views.nuevo_turno),
    (r'^administrativos/turnos/nuevo-turno/$', turnos_views.nuevo_turno_adm),


    ## - Historia Clinica - ## (solo visible para medicos)
    (r'^historia-clinica/nueva/$', hc_med_views.nueva),
    (r'^historia-clinica/listado-pacientes/$', hc_med_views.listado_pacientes),

    # - Datos Base
    (r'^historia-clinica/mostrar-datos-base/$', hc_med_views.mostrar_datos_paciente),
    (r'^historia-clinica/modificar-datos-base/$', hc_med_views.modificar_datos_paciente),

    # - Antecedentes Perinatales
    (r'^historia-clinica/mostrar-antecedentes-perinatales/$', hc_med_views.mostrar_antecedentes_perinatales),
    (r'^historia-clinica/agregar-antecedentes-perinatales/$', hc_med_views.agregar_antecedentes_perinatales),
    (r'^historia-clinica/modificar-antecedentes-perinatales/$', hc_med_views.modificar_antecedentes_perinatales),

    # - Vacunas
    (r'^historia-clinica/listado-vacunas/$', hc_med_views.listado_vacunas),
    (r'^historia-clinica/listado-vacunas/(\d{0,2})/$', hc_med_views.listado_vacunas),
    (r'^historia-clinica/agregar-vacuna/$', hc_med_views.agregar_vacuna),
    (r'^historia-clinica/agregar-vacuna/(\d{0,2})/$', hc_med_views.agregar_vacuna),
    (r'^historia-clinica/borrar-vacuna/$', hc_med_views.borrar_vacuna),
    (r'^historia-clinica/modificar-vacuna/$', hc_med_views.modificar_vacuna),

    # - Examen Fisico
    # - Examen Fisico -> Examen Base
    (r'^historia-clinica/nuevo-examen-base/$', hc_med_views.nuevo_examen_base),
    (r'^historia-clinica/mostrar-examen-base/$', hc_med_views.mostrar_examen_base),
    (r'^historia-clinica/listado-examen-fisico/$', hc_med_views.listado_examenes_fisicos),

    # - Examen Fisico -> Examen Cardio Vascular
    (r'^historia-clinica/mostrar-examen-cardio-vascular/$', hc_med_views.mostrar_examen_cardio_vascular),

    # - Examen Fisico -> Examen Aparato Respiratorio
    (r'^historia-clinica/mostrar-examen-aparato-respiratorio/$', hc_med_views.mostrar_examen_aparato_respiratorio),

    # - Examen Fisico -> Examen Cabeza
    (r'^historia-clinica/mostrar-examen-cabeza/$', hc_med_views.mostrar_examen_cabeza),
    (r'^historia-clinica/nuevo-examen-cabeza/$', hc_med_views.nuevo_examen_cabeza),

    # - Examen Fisico -> Examen Cuello
    (r'^historia-clinica/mostrar-examen-cuello/$', hc_med_views.mostrar_examen_cuello),
    (r'^historia-clinica/nuevo-examen-cuello/$', hc_med_views.nuevo_examen_cuello),

    # - Examen Fisico -> Imagenes
    (r'^historia-clinica/mostrar-imagenes/$', hc_med_views.mostrar_imagenes),
    (r'^historia-clinica/mostrar-imagen/$', hc_med_views.mostrar_imagen),
    (r'^historia-clinica/agregar-imagen/$', hc_med_views.agregar_imagen),

    # - Examen Fisico -> Analisis de Laboratorio
    (r'^historia-clinica/mostrar-analisis-lab/$', hc_med_views.mostrar_analisis_lab),

    # - Consultas Medicas
    (r'^historia-clinica/listado-consultas/$', hc_med_views.listado_consultas_medicas),
    (r'^historia-clinica/nueva-consulta/$', hc_med_views.nueva_consulta_medica),
    (r'^historia-clinica/mostrar-consulta/$', hc_med_views.mostrar_consulta_medica),


    ## - Otras Views - ##
    (r'area/$', generics_views.area),
    (r'^usuario-no-autorizado/$', generics_views.no_autorizado),
    (r'^error/$', generics_views.page_error),

)

#paginas personalizadas para los errores 404 y 505
handler404 = 'generics_views.error404'
#handler500 = 'generics_views.error500'
