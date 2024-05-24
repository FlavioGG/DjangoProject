from django.db import models

# Create your models here.
# users/models.py

class Perfil_de_Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)  # Campo para almacenar números de teléfono
    fecha_nacimiento = models.DateField()
    

class Direccion(models.Model):
    usuario = models.ForeignKey(Perfil_de_Usuario, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)

