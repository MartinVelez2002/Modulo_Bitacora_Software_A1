from django.views.generic import TemplateView


class MostrarLogin(TemplateView):
    template_name = 'login.html'
