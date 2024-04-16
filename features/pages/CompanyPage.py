import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.locators.CompanyLocators import add_new_company_locator, company_name_locator, company_email_locator, \
    company_submitted_pop_up_locator, company_submit_button_locator, company_contact_locator, company_phone_locator, \
    company_country_locator, company_website_locator, company_contact_options_locator
from utilities.WaitManager import WaitManager


class CompanyPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_company_button(self):
        login_button = WaitManager.wait_for_element(self.driver, add_new_company_locator)
        login_button.click()

    def fill_company_name_field(self, company_name):
        company_name_field = WaitManager.wait_for_element(self.driver, company_name_locator)
        company_name_field.clear()
        company_name_field.send_keys(company_name)

    def fill_company_email_field(self, company_email):
        company_email_field = WaitManager.wait_for_element(self.driver, company_email_locator)
        company_email_field.clear()
        company_email_field.send_keys(company_email)

    def click_submit_new_company_button(self):
        company_name_field = WaitManager.wait_for_element(self.driver, company_submit_button_locator)
        company_name_field.click()

    def is_company_submitted_popup_displayed(self):
        try:
            WaitManager.wait_for_element(self.driver, company_submitted_pop_up_locator)
            return True
        except TimeoutException:
            return False

    def select_company_contact_field(self):
        time.sleep(3)
        company_contact_dropdown = WaitManager.wait_for_element(self.driver, company_contact_locator)
        time.sleep(3)
        company_contact_dropdown.click()
        time.sleep(3)
        company_contact_dropdown.send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        company_contact_dropdown.send_keys(Keys.ENTER)

    def select_company_country_field(self):
        time.sleep(3)
        company_contact_dropdown = WaitManager.wait_for_element(self.driver, company_contact_locator)
        time.sleep(3)
        company_contact_dropdown.click()
        time.sleep(3)
        company_contact_dropdown.send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        company_contact_dropdown.send_keys(Keys.ENTER)

    def fill_company_phone_field(self, company_phone):
        company_phone_field = WaitManager.wait_for_element(self.driver, company_phone_locator)
        company_phone_field.clear()
        company_phone_field.send_keys(company_phone)

    def fill_company_website_field(self, company_website):
        company_website_field = WaitManager.wait_for_element(self.driver, company_website_locator)
        company_website_field.clear()
        company_website_field.send_keys(company_website)
