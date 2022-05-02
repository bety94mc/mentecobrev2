from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.db.models import Count, Max, Min, Case, When, IntegerField, F, Q, Manager

from multiselectfield import MultiSelectField
# Create your models here.

class Usuario(AbstractUser):
    universoOpciones = (('A','Aliento de los diosos'), ('AB', 'Arena Blanca'), ('AE', 'El alma del emperador'),('AL','Alcatraz'),('C','Cosmere'),('CT','Citoverso'),('E','Elantris'),
                        ('FU','Fuera del universo'),('L','Legión'),('M','Nacidos de la bruma'),('OH','Otras Historias'),('R','Rithmatista'),('RK','Reckoners'),('RT','Rueda del Tiempo'),('S','Archivo de las tormentas'),
                        ('SO','Sexto del Ocaso'),('SS','Sombras por silencio'),)
    tipoRango = (('Ad','Admin'),('Col','Colaborador'),)
    
    rango = models.CharField(max_length=3, choices=tipoRango, null=True, blank=True)
    universo = MultiSelectField(max_length=20,choices=universoOpciones, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.username)
    def get_absolute_url(self):
        return reverse('username', args=[str(self.username)])


class ManejadorUsuario(UserManager):
    def create_user(self, name, password=None):
        if not name:
            raise ValueError('Usuarios deben de tener un nombre válido')
        usuario = self.model(name=self.normalize_name(name),)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario


class Glosario(models.Model):
    """
    Objeto tipo Modelo. Glosario de Palabras Inglés-Español. Si tienen página, se indica.
    """
    universoOpciones = (('A','Aliento de los diosos'), ('AB', 'Arena Blanca'), ('AE', 'El alma del emperador'),('AL','Alcatraz'),('C','Cosmere'),('CT','Citoverso'),('E','Elantris'),
                        ('FU','Fuera del universo'),('L','Legión'),('M','Nacidos de la bruma'),('OH','Otras Historias'),('R','Rithmatista'),('RK','Reckoners'),('RT','Rueda del Tiempo'),('S','Archivo de las tormentas'),
                        ('SO','Sexto del Ocaso'),('SS','Sombras por silencio'),)
    
    wordEn = models.CharField(max_length=200)
    wordEs = models.CharField(max_length=200,null=True, blank=True)
    universo = MultiSelectField(max_length=20,choices=universoOpciones, null=True, blank=True)
    urlEn = models.URLField(max_length=2000,null=True, blank=True)
    urlEs = models.URLField(max_length=2000,null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        return reverse('id', args=[str(self.id)])
