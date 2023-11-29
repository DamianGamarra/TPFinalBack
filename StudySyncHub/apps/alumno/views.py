
from django.shortcuts import render
from .models import Alumno
from django.shortcuts import get_list_or_404
from django.views.generic import TemplateView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView





class CrearAlumno(LoginRequiredMixin,CreateView):
    model = Alumno
    template_name = 'crear_alumno.html'
    fields = ['nombre','apellido','fecha_nacimiento'] 
    success_url = reverse_lazy("perfil_alumno")
    
    

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("perfil_alumno", kwargs={'pk': self.object.pk})

class PerfilAlumno(LoginRequiredMixin,TemplateView):
    model = Alumno
    template_name = 'perfil_alumno.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        alumnos = get_list_or_404(Alumno, usuario=self.request.user)
        
        context["alumnos"] = alumnos
        return context
        
        
        
        
        
class ActualizarAlumno(LoginRequiredMixin,UpdateView):
    model = Alumno
    template_name = 'actualizar_alumno.html'
    fields = ['nombre','apellido','fecha_nacimiento']
    success_url = reverse_lazy("perfil_alumno")


class Home(TemplateView):
    template_name = 'home.html'