from django.conf.urls import url
from django.conf.urls import include
from Noticias.views import lista_noticias
from Noticias.views import nueva_noticia
from Noticias.views import editar_noticia
from Noticias.views import eliminar_noticia

urlpatterns = [
    #url(r'^$', principal, name='principal'),
    url(r'^lista_noticias/', lista_noticias, name='lista_noticias'),
    url(r'^nueva_noticia/', nueva_noticia, name='nueva_noticia'),
    url(r'^editar_noticia/(?P<pk>[0-9]+)/$', editar_noticia, name='editar_noticia'),
    url(r'^eliminar_noticia/(?P<pk>[0-9]+)/$', eliminar_noticia, name='eliminar_noticia'),
    #url(r'^usuarios/', include('Usuarios.urls')),
    #url(r'^login/', include('login.urls'))

]