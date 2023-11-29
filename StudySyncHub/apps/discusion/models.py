from django.db import models
from apps.alumno.models import Alumno

class Discusion(models.Model):
    titulo = models.CharField(max_length=30,blank=False , null=False, default="")
    contenido = models.TextField(max_length=1000,blank=False , null=False, default="")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(Alumno, on_delete=models.CASCADE,null=True ,related_name='discusiones')
    
    def __str__(self) :
        return self.titulo
    
    
class Comentario(models.Model):
    discusion = models.ForeignKey(Discusion, on_delete=models.CASCADE,null=True ,related_name='comentarios')
    autor = models.ForeignKey(Alumno, on_delete=models.CASCADE,null=True ,related_name='comentarios')
    contenido = models.TextField(max_length=1000,blank=False , null=False, default="")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return f"Comentario de {self.autor} en {self.discusion.titulo}"
    
    