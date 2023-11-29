from django.db import models
from apps.materias.models import Materia

class Proyectos(models.Model):
    nombre = models.CharField(max_length=30,blank=False , null=False, default="")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField(max_length=1000,blank=False , null=False, default="")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE,null=True ,related_name='proyectos')
    alumno = models.ForeignKey('alumno.Alumno', on_delete=models.CASCADE,null=True ,related_name='proyectos')