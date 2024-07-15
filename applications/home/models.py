from django.db import models

# Create your models here.


class Prueba(models.Model):
  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  edad = models.IntegerField()
  fecha_nacimiento = models.DateField()
    
  def __str__(self):
    return self.nombre + '-' + self.apellido