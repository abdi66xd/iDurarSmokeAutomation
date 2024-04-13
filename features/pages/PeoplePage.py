from selenium.common import TimeoutException
from features.locators.PeopleLocators import people_submitted_popup_locator, submit_new_person_button_locator, \
    last_name_locator, first_name_locator, new_person_button_locator
from utilities.WaitManager import WaitManager


class PeoplePage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_person(self):
        new_person_button = WaitManager.wait_for_element(self.driver, new_person_button_locator)
        new_person_button.click()

    def fill_firstname_field(self, first_name):
        email_field = WaitManager.wait_for_element(self.driver, first_name_locator)
        email_field.clear()
        email_field.send_keys(first_name)

    def fill_lastname_field(self, last_name):
        email_field = WaitManager.wait_for_element(self.driver, last_name_locator)
        email_field.clear()
        email_field.send_keys(last_name)

    def click_submit_new_person_button(self):
        submit_new_person_button = WaitManager.wait_for_element(self.driver, submit_new_person_button_locator)
        submit_new_person_button.click()

    def click_close_modal_icon(self):
        close_icon = WaitManager.wait_for_element(self.driver, submit_new_person_button_locator)
        close_icon.click()

    def is_people_submitted_popup_displayed(self):
        try:
            WaitManager.wait_for_element(self.driver, people_submitted_popup_locator)
            return True
        except TimeoutException:
            return False
