import time

from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.locators.CompanyLocators import add_new_company_locator, company_name_locator, company_email_locator, \
    company_submitted_pop_up_locator, company_submit_button_locator, company_contact_locator, company_phone_locator, \
    company_country_locator, company_website_locator
from features.locators.CustomerLocators import add_new_client_button, success_client_created_button, \
    type_client_dropdown, people_client_dropdown, company_client_dropdown, submit_client_button_f, error_client_popup
from utilities.WaitManager import WaitManager


class CustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_client_button(self):
        client_button = WaitManager.wait_for_element(self.driver, add_new_client_button)
        client_button.click()

    def is_client_submitted_popup_displayed(self):
        client_displayed = WaitManager.wait_for_element(self.driver, error_client_popup)
        client_displayed.is_displayed()
        return client_displayed

    def select_people_client_type_field(self):
        action_chains = ActionChains(self.driver)
        action_chains.send_keys(Keys.TAB * 5)
        time.sleep(1)
        action_chains.send_keys(Keys.ENTER * 2)
        time.sleep(1)
        action_chains.perform()

    def select_company_client_type_field(self):
        action_chains = ActionChains(self.driver)
        action_chains.send_keys(Keys.TAB * 5)
        time.sleep(1)
        action_chains.send_keys(Keys.ENTER)
        time.sleep(1)
        action_chains.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        action_chains.send_keys(Keys.ENTER)
        time.sleep(1)
        action_chains.perform()

    def select_people_field(self):
        action_chains = ActionChains(self.driver)
        time.sleep(1)
        action_chains.send_keys(Keys.TAB * 2)
        time.sleep(1)
        action_chains.send_keys(Keys.ENTER)
        time.sleep(1)
        action_chains.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        action_chains.send_keys(Keys.ENTER)
        time.sleep(1)
        action_chains.perform()

    def select_company_field(self):
        action_chains = ActionChains(self.driver)
        action_chains.send_keys(Keys.TAB * 2)
        time.sleep(1)
        action_chains.send_keys(Keys.ENTER)
        time.sleep(1)
        action_chains.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        action_chains.send_keys(Keys.ENTER)
        time.sleep(1)
        action_chains.perform()

    def click_submit_new_client_button(self):
        submit_client_button = WaitManager.wait_for_element(self.driver, submit_client_button_f)
        submit_client_button.click()
