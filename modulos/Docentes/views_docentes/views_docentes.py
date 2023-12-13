from django.urls import reverse_lazy
from django.views.generic import *
from modulos.Docentes.forms import FormDocentes
from modulos.Docentes.models import DocentesModel


class anadirDocente(CreateView, ListView):
    model = DocentesModel
    template_name = '../Templates/docentes_añadir.html'
    success_url = reverse_lazy('docentes:agregar_docente')
    context_object_name = 'docentes'
    form_class = FormDocentes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo_add'] = 'Agregar Docentes'
        context['url_anterior'] = '/'
        context['titulo_list'] = 'Docentes Registrados'

        return context


class EditarDocente(UpdateView):
    model = DocentesModel
    template_name = 'editar_docente.html'
    success_url = reverse_lazy('docentes:agregar_docente')
    form_class = FormDocentes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo_add'] = 'Edición de Docentes'
        context['url_anterior'] = '/docentes/crear_docente/'

        return context


class EliminarDocente(DeleteView):
    model = DocentesModel
    template_name = 'eliminar_docente.html'
    success_url = reverse_lazy('docentes:agregar_docente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo_add'] = 'Eliminar Docente'
        context['url_anterior'] = '/docentes/crear_docente'

        return context
