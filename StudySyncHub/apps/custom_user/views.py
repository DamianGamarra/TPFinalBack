from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.shortcuts import redirect


class RegistroUsuarioView(CreateView):
    template_name = 'registro.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Usuario creado exitosamente.')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el usuario. Por favor, ingrese correctamente los datos.')
        return super().form_invalid(form)

class CustomLoginView(LoginView):
    template_name = "custom_login.html"
 
    def form_valid(self, form):
        
        response = super().form_valid(form)

        
        if not self.request.user.alumno:
            
            return redirect('crear_alumno.html')

        return response   
    
    
    def form_invalid(self, form):
        messages.error(
            self.request, "Credenciales incorrectas. Por favor, inténtalo de nuevo."
        )  
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    success_url = reverse_lazy("custom_login.html")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, '¡Te has desconectado exitosamente!')
        return super().dispatch(request, *args, **kwargs)