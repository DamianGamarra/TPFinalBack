from django.db import models

class Materia(models.Model):
    MATERIA_CHOICES = [
        ('Matematicas', 'Matematicas'),
        ('Back-end', 'Back-end'),
        ('Front-end', 'Front-end'),
        ('Nube', 'Nube'),
        ('Ingles', 'Ingles'),
    ]
    nombre = models.CharField(max_length=100, choices=MATERIA_CHOICES)
    
    def __str__(self) :
        return self.nombre