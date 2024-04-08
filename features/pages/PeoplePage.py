from selenium.common import TimeoutException
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from utilities.WaitManager import WaitManager


class PeoplePage:
    new_person_button = (By.XPATH,
                         "//button[@class='ant-btn css-16v3ahg ant-btn-primary']")
    first_name = (By.XPATH, "//div[@class='BottomCollapseBox']//div//div[@class='ant-row css-16v3ahg']//div["
                            "@class='ant-col ant-col-24 css-16v3ahg']//div[@class='ant-spin-nested-loading "
                            "css-16v3ahg']//div[@class='ant-spin-container']//form[@class='ant-form ant-form-vertical "
                            "css-16v3ahg']//div//input[@id='firstname']")
    last_name = (By.XPATH, "//div[@class='BottomCollapseBox']//div//div[@class='ant-row css-16v3ahg']//div["
                           "@class='ant-col ant-col-24 css-16v3ahg']//div[@class='ant-spin-nested-loading "
                           "css-16v3ahg']//div[@class='ant-spin-container']//form[@class='ant-form ant-form-vertical "
                           "css-16v3ahg']//div//input[@id='lastname']")
    submit_new_person_button = (By.XPATH, "//div[@class='BottomCollapseBox']//div//button[@type='submit']")
    close_icon = (By.XPATH, "//span[@class='anticon anticon-close']")
    people_submitted_popup = (By.XPATH, "//div[@class='ant-notification-notice ant-notification-notice-success "
                                        "ant-notification-notice-closable']")

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_person(self):
        new_person_button = WaitManager.wait_for_element(self.driver, self.new_person_button)
        new_person_button.click()

    def fill_firstname_field(self, first_name):
        email_field = WaitManager.wait_for_element(self.driver, self.first_name)
        email_field.clear()
        email_field.send_keys(first_name)

    def fill_lastname_field(self, last_name):
        email_field = WaitManager.wait_for_element(self.driver, self.last_name)
        email_field.clear()
        email_field.send_keys(last_name)

    def click_submit_new_person_button(self):
        submit_new_person_button = WaitManager.wait_for_element(self.driver, self.submit_new_person_button)
        submit_new_person_button.click()

    def click_close_modal_icon(self):
        close_icon = WaitManager.wait_for_element(self.driver, self.submit_new_person_button)
        close_icon.click()

    def is_people_submitted_popup_displayed(self):
        try:
            WaitManager.wait_for_element(self.driver, self.people_submitted_popup)
            return True
        except TimeoutException:
            return False
