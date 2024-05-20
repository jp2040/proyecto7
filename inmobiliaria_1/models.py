from django.db import models

class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    tipo_usuario = models.CharField(max_length=20)

class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.DecimalField(max_digits=6, decimal_places=2)
    m2_totales = models.DecimalField(max_digits=6, decimal_places=2)
    estacionamientos = models.PositiveIntegerField()
    habitaciones = models.PositiveIntegerField()
    banos = models.PositiveIntegerField()
    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=50)
    tipo_inmueble = models.CharField(max_length=20)
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2)

    
class Region(models.Model):
    nombre = models.CharField(max_length=255)

class Comuna(models.Model):
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
