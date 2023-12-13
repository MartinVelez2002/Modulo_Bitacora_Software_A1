from django.urls import path
from modulos.Actividades.views_actividades.view_actividades import anadirActividad

app_name = 'actividad'

urlpatterns = [
    path('crear_actividad/', (anadirActividad.as_view()), name='crear_actividad')
]