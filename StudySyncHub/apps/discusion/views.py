from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .models import Discusion
from .forms import DiscusionForm, ComentarioForm
from django.shortcuts import get_object_or_404
from .models import Comentario
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.alumno.models import Alumno

class CrearDiscusionView(LoginRequiredMixin,View):
    template_name = 'crear_discusion.html'  # Ajusta el nombre del template según tu estructura

    def get(self, request):
        form = DiscusionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DiscusionForm(request.POST)
        if form.is_valid():
            discusion = form.save(commit=False)
            
            discusion.save()
            return redirect('lista_discusiones')  # Ajusta el nombre de la URL según tus necesidades

        return render(request, self.template_name, {'form': form})
    

    
    


class DetallesDiscusionView(View):
    template_name = 'detalles_discusion.html'

    def get(self, request, discusion_id):
        discusion = get_object_or_404(Discusion, pk=discusion_id)
        comentarios = Comentario.objects.filter(discusion=discusion)
        comentario_form = ComentarioForm()  # Aquí estás creando una instancia del formulario

        return render(request, self.template_name, {
            'discusion': discusion,
            'comentarios': comentarios,
            'comentario_form': comentario_form,
        })

    def post(self, request, discusion_id):
        discusion = get_object_or_404(Discusion, pk=discusion_id)
        comentario_form = ComentarioForm(request.POST)

        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.discusion = discusion
            comentario.autor = request.user
            comentario.save()

        return redirect('detalles_discusion', discusion_id)
    
    
class ListaDiscusionesView(View):
    template_name = 'lista_discusiones.html'

    def get(self, request):
        discusiones = Discusion.objects.all()
        return render(request, self.template_name, {'discusiones': discusiones})
    
class EditarDiscusionView(View):
    template_name = 'editar_discusion.html'  

    def get(self, request, discusion_id):
        discusion = get_object_or_404(Discusion, pk=discusion_id)
        form = DiscusionForm(instance=discusion)
        return render(request, self.template_name, {'form': form})

    def post(self, request, discusion_id):
        discusion = get_object_or_404(Discusion, pk=discusion_id)
        form = DiscusionForm(request.POST, instance=discusion)
        if form.is_valid():
            discusion = form.save(commit=False)
            discusion.save()
            return redirect('lista_discusiones')  

        return render(request, self.template_name, {'form': form})
    
class EliminarDiscusionView(DeleteView):
    model = Discusion
    template_name = 'eliminar_discusion.html'
    success_url = reverse_lazy('lista_discusiones')

    def get(self, request, discusion_id):
        discusion = get_object_or_404(Discusion, pk=discusion_id)
        return render(request, self.template_name, {'discusion': discusion})

    def post(self, request, discusion_id):
        discusion = get_object_or_404(Discusion, pk=discusion_id)
        discusion.delete()
        return redirect(self.success_url)


class EditarComentarioView(UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'editar_comentario.html'
    success_url = reverse_lazy('lista_discusiones')

    def get(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, pk=comentario_id)
        if request.user == comentario.autor or request.user.is_superuser:
            form = ComentarioForm(instance=comentario)
            return render(request, self.template_name, {'form': form, 'comentario': comentario})
        else:
            return redirect('lista_discusiones')

    def post(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, pk=comentario_id)
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid() and (request.user == comentario.autor or request.user.is_superuser):
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form, 'comentario': comentario})
    
class EliminarComentarioView(DeleteView):
    model = Comentario
    template_name = 'eliminar_comentario.html'
    success_url = reverse_lazy('lista_discusiones')

    def get(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, pk=comentario_id)
        if request.user == comentario.autor or request.user.is_superuser:
            return render(request, self.template_name, {'comentario': comentario})
        else:
            return redirect('lista_discusiones')

    def post(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, pk=comentario_id)
        if request.user == comentario.autor or request.user.is_superuser:
            comentario.delete()
            return redirect(self.success_url)
        else:
            return redirect('lista_discusiones')