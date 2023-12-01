from django.db import models
from apps.alumno.models import Alumno
from apps.custom_user.models import CustomUser

class Discusion(models.Model):
    titulo = models.CharField(max_length=30,blank=False , null=False, default="")
    contenido = models.TextField(max_length=1000,blank=False , null=False, default="")
    creador = models.ForeignKey(Alumno, on_delete=models.CASCADE,null=True ,related_name='discusiones')
    
    def __str__(self) :
        return self.titulo + " - " +self.contenido 
    
class Comentario(models.Model):
    discusion = models.ForeignKey('Discusion', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.discusion.titulo}"
    
    
