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
    profesor = models.CharField(max_length=100, blank=True)
    
    def __str__(self) :
        return self.get_nombre_display()