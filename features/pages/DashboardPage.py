import configparser
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import ConfigReader


class DashboardPage:
    avatar_icon_XPATH = (By.XPATH,
                         "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/span[1]")
    email_element_XPATH = (By.XPATH, "//p[normalize-space()='abdiasalpire12@gmail.com']")

    def __init__(self, driver):
        self.driver = driver

    def click_avatar_icon(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.avatar_icon_XPATH))
        login_button.click()

    def catch_mail_name(self):
        email_element = self.driver.find_element(*self.email_element_XPATH)
        email_text = email_element.text
        return email_text
