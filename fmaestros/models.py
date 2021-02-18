# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import encoding
from reportlab.lib.units import cm


# Create your models here.
class Empresa(models.Model):
    codigo = models.CharField(max_length=16, unique=True)
    nombre = models.CharField(max_length=60, unique=True)
    razon_social = models.CharField(max_length=60, null=True, blank=True)
    cif = models.CharField(max_length=16, null=True, blank=True)
    cp = models.CharField(max_length=11, null=True, blank=True)
    direccion =  models.CharField(max_length=70, null=True, blank=True)
    poblacion = models.CharField(max_length=70, null=True, blank=True)
    provincia = models.CharField(max_length=70, null=True, blank=True)
    telefono = models.CharField(max_length=70, null=True, blank=True)
    pais = models.CharField(max_length=70, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_paso_historico = models.DateField(null=True, blank=True)

    def __str__(self):
        dato='%s' % (self.nombre,)
        return encoding.smart_str(dato, encoding='utf8', errors='ignore')

    class Meta:
        verbose_name_plural = "Empresas"


class Cuenta(models.Model):
    """
    ambigus, taquilla, futbol_base, primer_equipo ...
    """
    codigo = models.CharField(max_length=16, unique=True)
    nombre = models.CharField(max_length=60, unique=True)

    observaciones = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_paso_historico = models.DateField(null=True, blank=True) #correcion only DateField

    def __str__(self):
        dato='%s' % (self.nombre,)
        return encoding.smart_str(dato, encoding='utf8', errors='ignore')

    class Meta:
        verbose_name_plural = "Tipos de Gastos e Ingresos"

# _____________ INI Código añadido por crea_prototipo_fmaestros.py
 
    
class Obra(models.Model):
    codigo = models.CharField(max_length=4, unique=True,blank=True)
    nombre = models.CharField(max_length=60)
    
    observaciones = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_paso_historico = models.DateField(null=True, blank=True)#corregido

    def __str__(self):
        dato = str(self.nombre) + '  ' + str(self.codigo)
               #'%s' % (self.nombre,)#
        return encoding.smart_str(dato, encoding='utf8', errors='ignore')   

    class Meta:
        verbose_name_plural = "Obras"
        indexes = [
            models.Index(fields=['codigo']),
        ]

    
# _______________ FIN Código añadido por crea_prototipo_fmaestros.py
 

class Apunte(models.Model):
    """
    Fecha de la anotación.
    Número que hace el asiento a lo largo del ejercicio. (vamos a usar el ID)
    Cuenta que intervienen (no en el sentido del PGC).
    Importe
    Breve descripción de la operación.
    Gasto o Ingreso
    """
    fecha = models.DateField()
    descripcion = models.CharField(max_length=60)
    importe = models.DecimalField(max_digits=12, decimal_places=2)
    es_gasto = models.BooleanField()
    cuenta = models.ForeignKey(Cuenta)
    obra = models.ForeignKey(Obra,null=True,blank=True) #agregado la llave foranea

    observaciones = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_paso_historico = models.DateField(null=True, blank=True)#corregido

    def __str__(self):
        dato='%s %s %s %s' % (self.fecha, self.descripcion, self.importe, self.es_gasto)
        return encoding.smart_str(dato, encoding='utf8', errors='ignore')

    class Meta:
        verbose_name_plural = "Apunte Contable"

        indexes = [
            models.Index(['fecha']),
            models.Index(['es_gasto']),
            models.Index(['cuenta']),
            models.Index(['obra']),
        ]

