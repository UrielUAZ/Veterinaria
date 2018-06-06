from selenium import webdriver
import unittest
import warnings
from selenium.webdriver.common.keys import Keys
import time
import unittest
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

class NewVisitorTest(LiveServerTestCase):

    MAX_WAIT = 10

    def setUp(self):
        MAX_WAIT = 10  
        self.browser = webdriver.Firefox()


    def tearDown(self):  
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('Usuarios', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Lista de usuarios', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Nombre de usuario'
        )

        inputbox2 = self.browser.find_element_by_id('id_new_item_2')  
        self.assertEqual(
            inputbox2.get_attribute('placeholder'),
            'Contrasena'
        )

        inputbox3 = self.browser.find_element_by_id('id_new_item_3')  
        self.assertEqual(
            inputbox3.get_attribute('placeholder'),
            'Telefono'
        )

        inputbox4 = self.browser.find_element_by_id('id_new_item_4')  
        self.assertEqual(
            inputbox4.get_attribute('placeholder'),
            'Correo electronico'
        )



        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Uriel')  
        inputbox2.send_keys('Hola')
        inputbox3.send_keys('4922237674')
        inputbox4.send_keys('urielalejandroml@gmail.com')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox4.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('Uriel')


        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')


    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        MAX_WAIT = 10 
        while True:  
            try:
                table = self.browser.find_element_by_id('id_list_table')  
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > MAX_WAIT:  
                    raise e  
                time.sleep(0.5)


    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        #self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')  


        

