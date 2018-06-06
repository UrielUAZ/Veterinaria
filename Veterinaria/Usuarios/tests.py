# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.urls import resolve
from Usuarios.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from Usuarios.models import Usuario

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 2, 3)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.strip().startswith('<html>')) 
        self.assertIn('<title>Usuarios</title>', html)  
        self.assertTrue(html.strip().endswith('</html>'))


    #def test_home_page_returns_correct_html_1(self):
    #    request = HttpRequest()
    #    response = home_page(request)
    #    html = response.content.decode('utf8')
    #    expected_html = render_to_string('home.html')
    #    self.assertEqual(html, expected_html)


    def test_home_page_returns_correct_html_2(self):
        response = self.client.get('/')  

        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Usuarios</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')


    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'user_name': 'Uriel', 'user_password': 'quiubo',
        'user_tel': '4922237674', 'user_email': 'urielalejandroml@gmail.com'})

        self.assertEqual(Usuario.objects.count(), 1)  
        new_user = Usuario.objects.first()  
        self.assertEqual(new_user.nombre, 'Uriel')
 

        #self.assertTemplateUsed(response, 'home.html')


    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'user_name': 'Uriel', 'user_password': 'quiubo',
        'user_tel': '4922237674', 'user_email': 'urielalejandroml@gmail.com'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')


    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Usuario.objects.count(), 0)


    def test_displays_all_list_items(self):
        Usuario.objects.create(
            nombre='Uriel',
            password='QuiuboCompa',
            telefono=None,
            email='urielalejandroml@gmail.com'
        )
        Usuario.objects.create(
            nombre='Alejandro',
            password='QueOnda',
            telefono='4921230291',
            email='cassette_23@hotmail.com'
        )

        response = self.client.get('/')

        self.assertIn('Uriel', response.content.decode())
        self.assertIn('Alejandro', response.content.decode())



class UsuarioModelTest(TestCase):

    def test_saving_and_retrieving_users(self):
        first_user = Usuario()
        first_user.nombre = 'Uriel'
        first_user.password = 'pruebas'
        first_user.telefono = '4922237674'
        first_user.email = 'urielalejandroml@gmail.com'
        first_user.save()

        second_user = Usuario()
        second_user.nombre = 'Alejandro'
        second_user.password = 'mantenimiento'
        second_user.email = 'cassette_23@hotmail.com'
        second_user.save()

        saved_users = Usuario.objects.all()
        self.assertEqual(saved_users.count(), 2)

        first_saved_user = saved_users[0]
        second_saved_user = saved_users[1]
        self.assertEqual(first_saved_user.nombre, 'Uriel')
        self.assertEqual(second_saved_user.nombre, 'Alejandro')
        self.assertEqual(first_saved_user.password, 'pruebas')
        self.assertEqual(second_saved_user.password, 'mantenimiento')
        self.assertEqual(first_saved_user.telefono, '4922237674')
        self.assertEqual(second_saved_user.telefono, None)
        self.assertEqual(first_saved_user.email, 'urielalejandroml@gmail.com')
        self.assertEqual(second_saved_user.email, 'cassette_23@hotmail.com')


    
