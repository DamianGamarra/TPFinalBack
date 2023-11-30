from django.shortcuts import render
from django.views.generic import ListView
from apps.materias.models import Materia
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy



class MateriasListView(ListView):
    template_name = 'materias_list.html'
    context_object_name = 'materias'

    def get_queryset(self):
            return Materia.objects.all()
    
    
class MateriaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Materia
    template_name = 'materia_form.html'
    fields = ['nombre', 'profesor']
    success_url = reverse_lazy('materia:materias_list')

    def test_func(self):
        return self.request.user.is_superuser
    
    
class MateriaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Materia
    template_name = 'materia_form.html'
    fields = ['nombre', 'profesor']
    success_url = reverse_lazy('materia:materias_list')

    def test_func(self):
        return self.request.user.is_superuser
    
class MateriaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Materia
    template_name = 'materia_confirm_delete.html'
    success_url = reverse_lazy('materia:materias_list')

    def test_func(self):
        return self.request.user.is_superuser