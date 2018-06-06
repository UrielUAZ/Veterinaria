from django.conf.urls import url
from django.conf.urls import include
from Servicios.views import lista_servicios
from Servicios.views import nuevo_servicio
from Servicios.views import editar_servicio
from Servicios.views import eliminar_servicio
from Servicios.views import lista_tipo_servicio
from Servicios.views import nuevo_tipo_servicio
from Servicios.views import editar_tipo_servicio
from Servicios.views import eliminar_tipo_servicio


urlpatterns = [
    #url(r'^$', principal, name='principal'),
    url(r'^lista_servicios/', lista_servicios, name='lista_servicios'),
    url(r'^nuevo_servicio/', nuevo_servicio, name='nuevo_servicio'),
    url(r'^editar_servicio/(?P<pk>[0-9]+)/$', editar_servicio, name='editar_servicio'),
    url(r'^eliminar_servicio/(?P<pk>[0-9]+)/$', eliminar_servicio, name='eliminar_servicio'),
    url(r'^lista_tipo_servicio/', lista_tipo_servicio, name='lista_tipo_servicio'),
    url(r'^nuevo_tipo_servicio/', nuevo_tipo_servicio, name='nuevo_tipo_servicio'),
    url(r'^editar_tipo_servicio/(?P<pk>[0-9]+)/$', editar_tipo_servicio, name='editar_tipo_servicio'),
    url(r'^eliminar_tipo_servicio/(?P<pk>[0-9]+)/$', eliminar_tipo_servicio, name='eliminar_tipo_servicio'),
    #url(r'^usuarios/', include('Usuarios.urls')),
    #url(r'^login/', include('login.urls'))

]