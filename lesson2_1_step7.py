from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('treasure')
x = x_element.get_attribute('valuex')
y = calc(x)

input = browser.find_element_by_id('answer')
input.send_keys(y)

check = browser.find_element_by_id('robotCheckbox')
check.click()

radio = browser.find_element_by_id('robotsRule')
radio.click()

button = browser.find_element_by_css_selector('button.btn')
button.click()

time.sleep(10)
browser.quit()