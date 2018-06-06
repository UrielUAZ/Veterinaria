from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login
from Login.views import home_page
from Login.views import inicio

urlpatterns = [
    url(r'^inicio', inicio, name="inicio"),
    url(r'^$', home_page, name="home_page"),
    url(r'^login', login, {'template_name':'login.html'}, name="login"),
    url(r'^cerrar/$', logout_then_login, name="logout"),


]