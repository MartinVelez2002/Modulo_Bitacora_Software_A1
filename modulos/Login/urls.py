from django.urls import path
from modulos.Login.views_login.views_login import MostrarLogin

app_name = 'login_mod'
urlpatterns = [
    path('login/', (MostrarLogin.as_view()), name='login_view')

]