from selenium import webdriver
import time
import math

def calc(x):
	return math.log(math.fabs(12 * math.sin(x)))

def clicker():
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

clicker()

confirm = browser.switch_to.alert
confirm.accept()

time.sleep(1)

x_element = browser.find_element_by_id("input_value")
x = str(calc(int(x_element.text)))

input = browser.find_element_by_id("answer")
input.send_keys(x)

clicker()

alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
print(addToClipBoard)
alert.accept()

#ввовидм ответ на задачу
link = "https://stepik.org/accounts/google/login/?next=/users/32495060/courses"
browser.get(link)

login = "********" #your email on google
password = "***********" #your password on google 

input_login = browser.find_element_by_css_selector("#identifierId")
input_login.send_keys(login)

next = browser.find_element_by_css_selector("#identifierNext > span > span")
next.click()
time.sleep(2)

input_password = browser.find_element_by_css_selector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
input_password.send_keys(password)

next = browser.find_element_by_css_selector("#passwordNext > span > span")
next.click()
time.sleep(2)

link = "https://stepik.org/lesson/184253/step/4?unit=158843"
browser.get(link)
time.sleep(6)

input_answer = browser.find_element_by_css_selector("#ember222")
input_answer.send_keys(addToClipBoard)
time.sleep(2)

button = browser.find_element_by_css_selector("#ember107 > div > section > div > div.attempt__inner > div.attempt__actions > button")
button.click()