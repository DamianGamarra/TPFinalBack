from django.shortcuts import render
from django.views.generic import View
from apps.materias.models import Materia
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProyectoForm
from django.views.generic.edit import UpdateView , CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Proyectos

        


class CrearProyectoView(CreateView):
    model = Proyectos
    form_class = ProyectoForm  
    template_name = 'crear_proyecto.html'  
    success_url = 'perfil_proyecto.html' 
        
        
class DetallesProyectoView(View):
    template_name = 'detalles_proyecto.html'  
    def get(self, request, proyecto_id):
        proyecto = proyecto.objects.get(pk=proyecto_id)
        is_owner = proyecto.alumno == request.user.alumno if hasattr(request.user, 'alumno') else False
        return render(request, self.template_name, {'proyecto': proyecto, 'is_owner': is_owner})
    
    
    
class ListaProyectosView(View):
    model = Proyectos
    template_name = 'lista_proyectos.html'  
    context_object_name = 'proyectos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materias_proyectos'] = [(proyecto, proyecto.materia) for proyecto in context['proyectos']]
        return context
    
    
    
    
class EditarProyectoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Proyectos
    form_class = ProyectoForm
    template_name = 'editar_proyecto.html'

    def test_func(self):
        proyecto = self.get_object()
        return self.request.user.is_superuser or (hasattr(self.request.user, 'alumno') and proyecto.alumno == self.request.user.alumno)

    def get_success_url(self):
            return reverse_lazy('proyectos:perfil_proyecto', kwargs={'proyecto_id': self.object.id})
    
    
    
class EliminarProyectoView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Proyectos
    template_name = 'eliminar_proyecto.html'
    success_url = reverse_lazy('proyectos:lista_proyectos')

    def test_func(self):
        proyecto = self.get_object()
        return self.request.user.is_superuser or (hasattr(self.request.user, 'alumno') and proyecto.alumno == self.request.user.alumno)