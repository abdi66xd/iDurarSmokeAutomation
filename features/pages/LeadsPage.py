import time

from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.locators.CompanyLocators import add_new_company_locator, company_name_locator, company_email_locator, \
    company_submitted_pop_up_locator, company_submit_button_locator, company_contact_locator, company_phone_locator, \
    company_country_locator, company_website_locator
from features.locators.LeadsLocators import add_new_lead_button, lead_type_button_dropdown, lead_status_dropdown, \
    lead_people_dropdown, lead_source_dropdown, lead_notes_text_area, lead_submit_button, lead_confirmation_pop_up
from utilities.WaitManager import WaitManager


class LeadPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_leads_button(self):
        login_button = WaitManager.wait_for_element(self.driver, add_new_lead_button)
        login_button.click()

    def select_lead_type_field(self):
        lead_type_dropdown = WaitManager.wait_for_element(self.driver, lead_type_button_dropdown)
        lead_type_dropdown.click()
        lead_type_dropdown.send_keys(Keys.ARROW_DOWN)
        lead_type_dropdown.send_keys(Keys.ENTER)

    def select_lead_status_field(self):
        lead_status_dropdowns = WaitManager.wait_for_element(self.driver, lead_type_button_dropdown)
        lead_status_dropdowns.click()
        lead_status_dropdowns.send_keys(Keys.ARROW_DOWN)
        lead_status_dropdowns.send_keys(Keys.ENTER)

    def select_lead_source_field(self):
        lead_source_dropdowns = WaitManager.wait_for_element(self.driver, lead_source_dropdown)
        lead_source_dropdowns.click()
        lead_source_dropdowns.send_keys(Keys.ARROW_DOWN)
        lead_source_dropdowns.send_keys(Keys.ENTER)

    def select_lead_people_field(self):
        lead_peoples_dropdown = WaitManager.wait_for_element(self.driver, lead_people_dropdown)
        lead_peoples_dropdown.click()
        lead_peoples_dropdown.send_keys(Keys.ARROW_DOWN)
        lead_peoples_dropdown.send_keys(Keys.ENTER)

    def click_submit_new_lead_button(self):
        lead_name_field = WaitManager.wait_for_element(self.driver, lead_submit_button)
        lead_name_field.click()

    def is_lead_submitted_popup_displayed(self):
        try:
            WaitManager.wait_for_element(self.driver, lead_confirmation_pop_up)
            return True
        except TimeoutException:
            return False

    def fill_notes_field(self, lead_notes_text):
        lead_text_area = WaitManager.wait_for_element(self.driver, lead_notes_text_area)
        lead_text_area.clear()
        lead_text_area.send_keys(lead_notes_text)
