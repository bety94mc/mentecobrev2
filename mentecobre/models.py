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


class Articulos(models.Model):

    ''' opciones para las distintas columnas '''
    

    tipoOpciones = (('CU','Cultura'),('EVT','Eventos y eras'),('FDV','Formas de vida'),('LIB','Libros'),
                    ('LOC','Localizaciones'),('MG','Magia'),('PJ','Personajes'),('OBJ','Objetos y materiales'),('ORG','Organización'),
                    ('FAM','Familia'),('MUL','multimedia'),('WIKI','wiki/otros'),('DIS','Disambiguación'),('RD','Redirección'),('SUB','Subpágina'),)
    prioridadOpciones = (('1','Alta'),('2','Media'),('3','Baja'),('4','TBD'),)
    citaOpciones = (('Y','Sí'),('N','No'),)
    traducidoOpciones = (('Y','Sí'),('F','Falta Cita'), ('O','On Hold'),)
    revisadoOpciones = (('Y','Sí'),('P','En progreso'),)
    universoOpciones = (('C','Cosmere'),('M','Mistborn'),('S', 'Stormlight'),('A','Aliento'),('E','Elantris'),('AB','Arena Blanca'),('B','Brandon'),('FU','Fuera Universo'),
                        ('OH','Otras Historias'),('R','Rithmatista'),('RT','Rueda del Tiempo'),('CT','Citoverso'),('RK','Reckoners'),('SS','Sombras por Silencio'),('AL','Alcatraz'),
                        ('L','Legion'),('SO','Sexto del Ocaso'),('AE','Alma del Emperador'))
    
    ''' columnas de la tabla'''

    pageidEn = models.IntegerField(null=True, blank=True)
    pageidEs = models.IntegerField(null=True, blank=True)
    tituloEn = models.CharField( max_length=200, null=True, blank=True)
    tituloEs = models.CharField( max_length=200, null=True, blank=True)
    tipo = models.CharField( max_length=4, choices=tipoOpciones, null=True, blank=True)
    prioridad = models.CharField( max_length=1, choices=prioridadOpciones, null=True, blank=True)
    traductor = models.ForeignKey("Usuario",on_delete=models.DO_NOTHING, null=True, blank=True, limit_choices_to={'groups__name': "Traductores"},related_name='traductor') # añadir cuando esté creado limit_choices_to={'groups__name': "traductores"}
    fechaasignado = models.DateField(null=True, blank=True)
    cita = models.CharField( max_length=1, choices=citaOpciones, null=True, blank=True)
    traducido = models.CharField( max_length=1, choices=traducidoOpciones, null=True, blank=True)
    fechatraducido = models.DateField(null=True, blank=True)
    revisor = models.ForeignKey("Usuario", models.DO_NOTHING, null=True, blank=True, limit_choices_to={'groups__name': "Revisores"}, related_name='revisor') # añadir cuando esté creado limit_choices_to={'groups__name': "revisores"}
    revisado = models.CharField( max_length=1, choices=revisadoOpciones, null=True, blank=True)
    fechaasignadorevisor = models.DateField(null=True, blank=True)
    fecharevisado = models.DateField(null=True, blank=True)
    notas = models.TextField(null=True, blank=True)
    universo = MultiSelectField(max_length=3, choices=universoOpciones, null=True, blank=True)
    urldrive = models.URLField(null=True, blank=True)
    urlEn = models.URLField(null=True, blank=True)
    urlEs = models.URLField(null=True, blank=True)
    fechacambiosEn = models.DateField(null=True, blank=True)
    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        return reverse('id', args=[str(self.id)])