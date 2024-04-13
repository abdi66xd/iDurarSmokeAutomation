from features.locators.LoginLocators import email_locator, password_locator, login_button_locator, email_alert_locator, \
    invalid_credentials_alert_locator
from utilities.WaitManager import WaitManager


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_email_field(self, email):
        email_field = WaitManager.wait_for_element(self.driver, email_locator)
        email_field.clear()
        email_field.send_keys(email)

    def fill_password_field(self, password):
        password_field = WaitManager.wait_for_element(self.driver, password_locator)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = WaitManager.wait_for_element(self.driver, login_button_locator)
        login_button.click()
        WaitManager.wait_for_page_load(self.driver)

    def catch_email_alert(self):
        email_element = WaitManager.wait_for_element(self.driver, email_alert_locator)
        return email_element.text

    def catch_invalid_credentials_error(self):
        invalid_credentials_alert = WaitManager.wait_for_element(self.driver, invalid_credentials_alert_locator)
        return invalid_credentials_alert.text
