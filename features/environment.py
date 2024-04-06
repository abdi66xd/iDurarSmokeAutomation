from time import sleep

from selenium import webdriver
from utilities import ConfigReader


def before_scenario(context, scenario):
    browser_name = ConfigReader.read_configuration("Basic Information", "browser")
    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    elif browser_name == "edge":
        context.driver = webdriver.Edge()
    sleep(3)
    context.driver.maximize_window()
    context.driver.get("https://cloud.idurarapp.com/login")


def after_scenario(context, scenario):
    context.driver.quit()
