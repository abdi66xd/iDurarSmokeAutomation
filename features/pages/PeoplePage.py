import time

from selenium.common import TimeoutException
from features.locators.PeopleLocators import people_submitted_popup_locator, submit_new_person_button_locator, \
    last_name_locator, first_name_locator, new_person_button_locator, people_phone_number_locator, people_email_locator
from utilities.WaitManager import WaitManager


class PeoplePage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_person(self):
        time.sleep(2)
        new_person_button = WaitManager.wait_for_element(self.driver, new_person_button_locator)
        time.sleep(2)
        WaitManager.wait_for_page_load(self.driver)
        time.sleep(2)
        new_person_button.click()

    def fill_people_firstname_field(self, first_name):
        email_field = WaitManager.wait_for_element(self.driver, first_name_locator)
        WaitManager.wait_for_page_load(self.driver)
        email_field.clear()
        email_field.send_keys(first_name)

    def fill_people_lastname_field(self, last_name):
        email_field = WaitManager.wait_for_element(self.driver, last_name_locator)
        WaitManager.wait_for_page_load(self.driver)
        email_field.clear()
        email_field.send_keys(last_name)

    def click_submit_new_person_button(self):
        submit_new_person_button = WaitManager.wait_for_element(self.driver, submit_new_person_button_locator)
        WaitManager.wait_for_page_load(self.driver)
        submit_new_person_button.click()

    def click_people_close_modal_icon(self):
        close_icon = WaitManager.wait_for_element(self.driver, submit_new_person_button_locator)
        WaitManager.wait_for_page_load(self.driver)
        close_icon.click()

    def is_people_submitted_popup_displayed(self):
        try:
            WaitManager.wait_for_page_load(self.driver)
            WaitManager.wait_for_element(self.driver, people_submitted_popup_locator)
            return True
        except TimeoutException:
            return False

    def fill_people_phone_field(self, people_phone_number):
        WaitManager.wait_for_page_load(self.driver)
        people_phone_number_field = WaitManager.wait_for_element(self.driver, people_phone_number_locator)
        people_phone_number_field.clear()
        people_phone_number_field.send_keys(people_phone_number)

    def fill_people_email_field(self, people_email):
        WaitManager.wait_for_page_load(self.driver)
        people_email_field = WaitManager.wait_for_element(self.driver, people_email_locator)
        people_email_field.clear()
        people_email_field.send_keys(people_email)


