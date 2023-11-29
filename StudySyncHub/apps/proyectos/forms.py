from django import forms
from .models import Proyectos
from apps.alumno.models import Alumno

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'descripcion', 'materia']

    def __init__(self, *args, **kwargs):
        alumno = kwargs.pop('alumno', None)
        super(ProyectoForm, self).__init__(*args, **kwargs)

        if alumno:
            self.fields['alumno'] = forms.ModelChoiceField(queryset=Alumno.objects.filter(pk=alumno.pk), widget=forms.HiddenInput())