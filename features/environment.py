import allure
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
    context.driver.get(ConfigReader.read_configuration("Basic Information", "url"))


@allure.step
def take_screenshot(context, step_name):
    allure.attach(context.driver.get_screenshot_as_png(), name=step_name, attachment_type=allure.attachment_type.PNG)


def after_step(context, step):
    if step.status == "failed":
        take_screenshot(context, step.name)


def after_scenario(context, scenario):
    context.driver.quit()
