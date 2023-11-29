from django.urls import path
from .views import CrearAlumno , PerfilAlumno , ActualizarAlumno, Home

urlpatterns = [
    path('crear_alumno/', CrearAlumno.as_view(), name='crear_alumno'),
    path('perfil<int:pk>/', PerfilAlumno.as_view() , name='perfil_alumno'),
    path('actualizar_alumno/<int:pk>/', ActualizarAlumno.as_view(), name='actualizar_alumno'),
]