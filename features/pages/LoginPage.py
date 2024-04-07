from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utilities.WaitManager import WaitManager


class LoginPage:
    email = (By.XPATH, "//input[@id='normal_login_email']")
    password = (By.XPATH, "//input[@id='normal_login_password']")
    login_button = (By.XPATH, "//span[normalize-space()='Log In']")
    dashboard_logo = (By.XPATH, "//img[@src='/assets/logo-text-B-YMIDGj.svg']")
    email_alert = (By.XPATH, "//div[@class='ant-form-item-explain-error']")
    invalid_credentials_alert = (By.XPATH, "//div[@class='ant-notification-notice-description']")

    def __init__(self, driver):
        self.driver = driver

    def fill_email_field(self, email):
        email_field = WaitManager.wait_for_element(self.driver, self.email)
        email_field.clear()
        email_field.send_keys(email)

    def fill_password_field(self, password):
        password_field = WaitManager.wait_for_element(self.driver, self.password)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = WaitManager.wait_for_element(self.driver, self.login_button)
        login_button.click()
        WaitManager.wait_for_page_load(self.driver)

    def catch_email_alert(self):
        email_element = WaitManager.wait_for_element(self.driver, self.email_alert)
        return email_element.text

    def catch_invalid_credentials_error(self):
        invalid_credentials_alert = WaitManager.wait_for_element(self.driver, self.invalid_credentials_alert)
        return invalid_credentials_alert.text
