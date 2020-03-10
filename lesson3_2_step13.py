from selenium import webdriver
import unittest
import time

class TestWeb(unittest.TestCase):
	def test_complete(self):
		link_1 = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link_1)
		
		input1 = browser.find_element_by_css_selector(".first_block .first")
		input1.send_keys("Ivan")
	
		input2 = browser.find_element_by_css_selector(".first_block .second")
		input2.send_keys("Petrov")
		
		input3 = browser.find_element_by_css_selector(".first_block .third")
		input3.send_keys("ivan.petrow@step.com")
		
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		
		time.sleep(1)
		
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual ("Congratulations! You have successfully registered!", welcome_text, "Not find element")
		

	def test_error(self):
		link_1 = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link_1)
		
		input1 = browser.find_element_by_css_selector(".first_block .first")
		input1.send_keys("Ivan")
	
		input2 = browser.find_element_by_css_selector(".first_block .second")
		input2.send_keys("Petrov")
		
		input3 = browser.find_element_by_css_selector(".first_block .third")
		input3.send_keys("ivan.petrow@step.com")
		
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		
		time.sleep(1)
		
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual ("Congratulations! You have successfully registered!", welcome_text, "Not find element")
		
		
if __name__ == "__main__":
	unittest.main()