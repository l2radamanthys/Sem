#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(User):
    """
    Para el login y el manejo de secciones
    """
    dni = models.IntegerField('DNI')
    sexo = models.CharField('Sexo', max_length=1, select_sexo=[('M','Masculino'), ('F', 'Femenino'), ('-','-----')])
    categoria = models.IntegerField('Categoria', select_categoria=[(0,'Paciente'), (1, 'Medico'), (2,'Administrativo')])
    cod_categoria = models.IntegerField('CodCategoria')
    telefono = models.CharField('Nro de telefono', max_length=20)

    #renombrados para mayor comodidad
    nombre = first_name
    apellido = last_name
    
    #datos para recordar
    #username, password



    def __str__(self):
        return self.username

    class Admin:
        pass


class Medico(models.Model):
    pass


class Paciente(models.Model):
    pass


class Administrativo(models.Model):
    pass