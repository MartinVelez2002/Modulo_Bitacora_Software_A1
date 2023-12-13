from django.urls import reverse_lazy
from django.views.generic import *
from modulos.Actividades.forms import FormActividades
from modulos.Actividades.models import ActividadModel


class anadirActividad(CreateView):
    model = ActividadModel
    template_name = 'c_actividad.html'
    success_url = reverse_lazy()
    form_class = FormActividades

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Crear Actividad'
        context['url_anterior'] = '/'

        return context

