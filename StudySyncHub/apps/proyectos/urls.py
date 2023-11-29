from django.urls import path
from .views import CrearProyectoView, DetallesProyectoView , ListaProyectosView , EditarProyectoView , EliminarProyectoView


urlpatterns = [
    path('crear_proyecto/', CrearProyectoView.as_view(), name='crear_proyecto'),
    path('lista_proyectos/', ListaProyectosView.as_view(), name='lista_proyectos'),
    path('detalles_proyecto/<int:pk>/', DetallesProyectoView.as_view(), name='detalles_proyecto'),
    path('editar_proyecto/<int:pk>/', EditarProyectoView.as_view(), name='editar_proyecto'),
    path('eliminar_proyecto/<int:pk>/', EliminarProyectoView.as_view(), name='eliminar_proyecto'),
]
