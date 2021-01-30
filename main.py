import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://web.telegram.org")
phone_number_input = browser.find_element_by_css_selector("[ng-model=\"credentials.phone_number\"]")
phone_number_input.clear()
phone_number_input.send_keys()
