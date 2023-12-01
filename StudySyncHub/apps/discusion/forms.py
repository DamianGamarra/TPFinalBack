from django import forms
from .models import Discusion, Comentario


class DiscusionForm(forms.ModelForm):
    class Meta:
        model = Discusion
        fields = ['titulo', 'contenido']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']