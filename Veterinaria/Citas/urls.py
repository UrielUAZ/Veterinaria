from django.conf.urls import url
from django.conf.urls import include
from Citas.views import lista_citas
from Citas.views import nueva_cita
from Citas.views import editar_cita
from Citas.views import eliminar_cita


urlpatterns = [
    #url(r'^$', principal, name='principal'),
    url(r'^lista_citas/', lista_citas, name='lista_citas'),
    url(r'^nueva_cita/', nueva_cita, name='nueva_cita'),
    url(r'^editar_cita/(?P<pk>[0-9]+)/$', editar_cita, name='editar_cita'),
    url(r'^eliminar_cita/(?P<pk>[0-9]+)/$', eliminar_cita, name='eliminar_cita'),
    ]