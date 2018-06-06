from django.conf.urls import url
from django.conf.urls import include
from Usuarios.views import principal
from Usuarios.views import lista_usuarios
from Usuarios.views import nuevo_usuario
from Usuarios.views import editar_usuario
from Usuarios.views import eliminar_usuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', principal, name='principal'),
    url(r'^lista_usuarios/', login_required(lista_usuarios), name='lista_usuarios'),
    url(r'^nuevo_usuario/', nuevo_usuario, name='nuevo_usuario'),
    url(r'^editar_usuario/(?P<pk>[0-9]+)/$', editar_usuario, name='editar_usuario'),
    url(r'^eliminar_usuario/(?P<pk>[0-9]+)/$', eliminar_usuario, name='eliminar_usuario'),

]