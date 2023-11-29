from django.db import models



class Alumno(models.Model):
    nombre = models.CharField(max_length=30,blank=False , null=False, default="")
    apellido = models.CharField(max_length=30,blank=True , null=True , default="")
    usuario = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE,null=True ,related_name='alumno')
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + str(self.fecha_nacimiento)