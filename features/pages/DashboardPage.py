from selenium.webdriver.common.by import By
from utilities.WaitManager import WaitManager


class DashboardPage:
    avatar_icon = (By.XPATH,
                   "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/span[1]")
    email_element = (By.XPATH, "//p[normalize-space()='abdiasalpire12@gmail.com']")
    logo_image = (By.XPATH, "//img[@src='/assets/logo-text-B-YMIDGj.svg']")
    people_tab = (By.XPATH, "//a[normalize-space()='Peoples']")

    def __init__(self, driver):
        self.driver = driver

    def click_avatar_icon(self):
        login_button = WaitManager.wait_for_element(self.driver, self.avatar_icon)
        login_button.click()

    def catch_mail_name(self):
        email_element = WaitManager.wait_for_element(self.driver, self.email_element)
        return email_element.text

    def is_logo_loaded(self):
        logo = WaitManager.wait_for_element(self.driver, self.logo_image)
        if logo:
            width = logo.get_attribute("naturalWidth")
            height = logo.get_attribute("naturalHeight")
            if width is not None and height is not None:
                return int(width) > 0 and int(height) > 0
        return False

    def click_people_tab(self):
        people_tab = WaitManager.wait_for_element(self.driver, self.people_tab)
        people_tab.click()

    