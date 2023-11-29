from django.urls import path
from .views import MateriasListView, MateriaCreateView, MateriaUpdateView, MateriaDeleteView


urlpatterns = [
    path('materias/', MateriasListView.as_view(), name='materias_list'),
    path('materia/nueva/', MateriaCreateView.as_view(), name='materia_create'),
    path('materia/<int:pk>/editar/', MateriaUpdateView.as_view(), name='materia_edit'),
    path('materia/<int:pk>/eliminar/', MateriaDeleteView.as_view(), name='materia_delete'),
    
]