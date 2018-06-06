from selenium import webdriver
import unittest
import warnings
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
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
        self.browser.get('http://localhost:8000')

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
        inputbox.send_keys(Keys.ENTER)
        inputbox2.send_keys(Keys.ENTER)
        inputbox3.send_keys(Keys.ENTER)
        inputbox4.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('Uriel')


        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')
        

if __name__ == '__main__':  
   with warnings.catch_warnings(record=True):
       unittest.main()  