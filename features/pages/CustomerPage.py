import time

from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.locators.CompanyLocators import add_new_company_locator, company_name_locator, company_email_locator, \
    company_submitted_pop_up_locator, company_submit_button_locator, company_contact_locator, company_phone_locator, \
    company_country_locator, company_website_locator
from features.locators.CustomerLocators import add_new_client_button, success_client_created_button, \
    type_client_dropdown, people_client_dropdown, company_client_dropdown, submit_client_button_f
from utilities.WaitManager import WaitManager


class CustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_client_button(self):
        client_button = WaitManager.wait_for_element(self.driver, add_new_client_button)
        client_button.click()

    def is_client_submitted_popup_displayed(self):
        try:
            WaitManager.wait_for_element(self.driver, success_client_created_button)
            return True
        except TimeoutException:
            return False

    def select_client_type_field(self):
        client_type_dropdown = WaitManager.wait_for_element(self.driver, type_client_dropdown)
        client_type_dropdown.click()
        client_type_dropdown.send_keys(Keys.ARROW_DOWN)
        client_type_dropdown.send_keys(Keys.ENTER)

    def select_people_field(self):
        client_people_dropdown = WaitManager.wait_for_element(self.driver, people_client_dropdown)
        client_people_dropdown.click()
        client_people_dropdown.send_keys(Keys.ARROW_DOWN)
        client_people_dropdown.send_keys(Keys.ENTER)

    def select_company_field(self):
        client_company_dropdown = WaitManager.wait_for_element(self.driver, company_client_dropdown)
        client_company_dropdown.click()
        client_company_dropdown.send_keys(Keys.ARROW_DOWN)
        client_company_dropdown.send_keys(Keys.ENTER)

    def click_submit_new_client_button(self):
        submit_client_button = WaitManager.wait_for_element(self.driver, submit_client_button_f)
        submit_client_button.click()