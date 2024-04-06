from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    email_XPATH = (By.XPATH, "//input[@id='normal_login_email']")
    password_XPATH = (By.XPATH, "//input[@id='normal_login_password']")
    login_button_XPATH = (By.XPATH, "//span[normalize-space()='Log In']")
    dashboard_logo_XPATH = (By.XPATH, "//img[@src='/assets/logo-text-B-YMIDGj.svg']")

    def __init__(self, driver):
        self.driver = driver

    def fill_email_field(self, email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.email_XPATH))
        email_field.clear()
        email_field.send_keys(email)

    def fill_password_field(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_XPATH))
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button_XPATH))
        login_button.click()
        sleep(5)


