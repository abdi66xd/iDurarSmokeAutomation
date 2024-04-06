from time import sleep

from selenium.webdriver.chrome import webdriver

from selenium.webdriver import Chrome

driver = Chrome()
driver.maximize_window()
driver.get('https://cloud.idurarapp.com/login')