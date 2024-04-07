from selenium.webdriver.common.by import By
from utilities.WaitManager import WaitManager


class DashboardPage:
    avatar_icon_XPATH = (By.XPATH,
                         "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/span[1]")
    email_element_XPATH = (By.XPATH, "//p[normalize-space()='abdiasalpire12@gmail.com']")

    def __init__(self, driver):
        self.driver = driver

    def click_avatar_icon(self):
        login_button = WaitManager.wait_for_element(self.driver, self.avatar_icon_XPATH)
        login_button.click()

    def catch_mail_name(self):
        email_element = WaitManager.wait_for_element(self.driver, self.email_element_XPATH)
        return email_element.text
