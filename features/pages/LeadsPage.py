import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from features.locators.LeadsLocators import add_new_lead_button, lead_notes_text_area, lead_submit_button, lead_confirmation_pop_up_locator
from utilities.WaitManager import WaitManager


class LeadPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_leads_button(self):
        lead_button = WaitManager.wait_for_element(self.driver, add_new_lead_button)
        time.sleep(2)
        lead_button.click()

    def select_lead_type_field(self):
        action_chains = ActionChains(self.driver)
        action_chains.send_keys(Keys.TAB * 5)
        action_chains.send_keys(Keys.ENTER * 2)  # Dos enters
        action_chains.perform()

    def select_lead_status_field(self):
        action_chains = ActionChains(self.driver)
        action_chains.send_keys(Keys.TAB * 2)
        action_chains.send_keys(Keys.ENTER * 2)
        action_chains.perform()

    def select_lead_source_field(self):
        action_chains = ActionChains(self.driver)
        action_chains.send_keys(Keys.TAB * 1)
        action_chains.send_keys(Keys.ENTER * 2)
        action_chains.perform()

    def select_lead_people_field(self):
        people_lead = ActionChains(self.driver)
        time.sleep(2)
        people_lead.send_keys(Keys.TAB * 1).perform()
        time.sleep(2)
        people_lead.send_keys(Keys.ARROW_RIGHT).perform()
        time.sleep(2)
        people_lead.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        people_lead.send_keys(Keys.ENTER).perform()
        time.sleep(2)
        people_lead.send_keys(Keys.TAB * 1).perform()

    def click_submit_new_lead_button(self):
        lead_name_field = WaitManager.wait_for_element(self.driver, lead_submit_button)
        lead_name_field.click()

    def is_lead_submitted_popup_displayed(self):
        try:
            WaitManager.wait_for_element(self.driver, lead_confirmation_pop_up_locator)
            return True
        except TimeoutException:
            return False

    def fill_notes_field(self, lead_notes_text):
        lead_text_area = WaitManager.wait_for_element(self.driver, lead_notes_text_area)
        lead_text_area.clear()
        lead_text_area.send_keys(lead_notes_text)
