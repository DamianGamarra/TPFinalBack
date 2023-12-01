from django.urls import path
from .views import CrearDiscusionView, DetallesDiscusionView , ListaDiscusionesView , EditarDiscusionView , EliminarDiscusionView , EditarComentarioView , EliminarComentarioView


urlpatterns = [
     path('crear_discusion/', CrearDiscusionView.as_view(), name='crear_discusion'),
     path('detalles_discusion/<int:discusion_id>/', DetallesDiscusionView.as_view(), name='detalles_discusion'),    
     path('discusiones/', ListaDiscusionesView.as_view(), name='lista_discusiones'),
     path('editar_discusion/<int:discusion_id>/', EditarDiscusionView.as_view(), name='editar_discusion'),
     path('eliminar_discusion/<int:discusion_id>/', EliminarDiscusionView.as_view(), name='eliminar_discusion'),
         path('editar_comentario/<int:comentario_id>/', EditarComentarioView.as_view(), name='editar_comentario'),
    path('eliminar_comentario/<int:comentario_id>/', EliminarComentarioView.as_view(), name='eliminar_comentario'),
]