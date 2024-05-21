import os
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains

from features.locators.OffersLocators import add_new_offer_button, client_offer_field, item_name_offer_field, \
    quantity_offer_field, price_offer_field, save_offer_button, offer_notification_xpath, offer_client_alert, \
    offer_item_name_alert, offer_quantity_alert, offer_price_alert, offer_tax_alert, offer_new_item_button, \
    firs_option_offer, download_option_offer
from utilities.OsHelpers import get_download_directory
from utilities.WaitManager import WaitManager
from selenium.webdriver.common.keys import Keys



class OffersPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_offer_button(self):
        WaitManager.wait_for_page_load(self.driver)
        time.sleep(2)
        new_offer_button = WaitManager.wait_for_element(self.driver, add_new_offer_button)
        time.sleep(2)
        new_offer_button.click()

    def select_lead_offer_field(self):
        WaitManager.wait_for_page_load(self.driver)
        lead_offer_field = WaitManager.wait_for_element(self.driver, client_offer_field)
        time.sleep(2)
        lead_offer_field.clear()
        lead_offer_field.click()
        time.sleep(2)
        lead_offer_field.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        lead_offer_field.send_keys(Keys.ENTER)

    def select_offer_tax_field(self):
        WaitManager.wait_for_page_load(self.driver)
        action_chains = ActionChains(self.driver)
        time.sleep(1)
        action_chains.send_keys(Keys.TAB)
        time.sleep(1)
        action_chains.perform()
        action_chains.send_keys(Keys.TAB)
        time.sleep(1)
        action_chains.perform()
        action_chains.send_keys(Keys.TAB)
        time.sleep(1)
        action_chains.perform()
        action_chains.send_keys(Keys.TAB)
        time.sleep(1)
        action_chains.perform()
        action_chains.send_keys(Keys.TAB)
        time.sleep(1)
        action_chains.perform()
        action_chains.send_keys(Keys.ENTER)
        time.sleep(1)
        action_chains.perform()
        action_chains.send_keys(Keys.ENTER)
        time.sleep(1)
        action_chains.perform()

    def fill_offer_item_name_field(self, offer_item_field):
        WaitManager.wait_for_page_load(self.driver)
        item_field = WaitManager.wait_for_element(self.driver, item_name_offer_field)
        item_field.clear()
        time.sleep(2)
        item_field.send_keys(offer_item_field)
        item_field.send_keys(Keys.ENTER)

    def fill_offer_item_quantity_field(self):
        WaitManager.wait_for_page_load(self.driver)
        offer_item_quantity_field = WaitManager.wait_for_element(self.driver, quantity_offer_field)
        offer_item_quantity_field.clear()
        time.sleep(2)
        offer_item_quantity_field.send_keys(5)

    def fill_offer_item_price_field(self):
        WaitManager.wait_for_page_load(self.driver)
        offer_item_price_field = WaitManager.wait_for_element(self.driver, price_offer_field)
        offer_item_price_field.clear()
        time.sleep(2)
        offer_item_price_field.send_keys(5)

    def click_submit_new_offer_button(self):
        WaitManager.wait_for_page_load(self.driver)
        submit_invoice_button = WaitManager.wait_for_element(self.driver, save_offer_button)
        time.sleep(2)
        submit_invoice_button.click()

    def is_offer_submitted_popup_displayed(self):
        WaitManager.wait_for_page_load(self.driver)
        try:
            WaitManager.wait_for_element(self.driver, offer_notification_xpath)
            return True
        except TimeoutException:
            return False

    def are_offer_alerts_displayed(self):
        offers_client_alert = WaitManager.wait_for_element(self.driver, offer_client_alert)
        offers_item_name_alerts = WaitManager.wait_for_element(self.driver, offer_item_name_alert)
        offers_quantity = WaitManager.wait_for_element(self.driver, offer_quantity_alert)
        offers_price = WaitManager.wait_for_element(self.driver, offer_price_alert)
        offers_tax = WaitManager.wait_for_element(self.driver, offer_tax_alert)
        if not (
                offers_client_alert.is_displayed()
                and offers_item_name_alerts.is_displayed()
                and offers_quantity.is_displayed()
                and offers_price.is_displayed()
                and offers_tax.is_displayed()):
            raise AssertionError("Some alert(s) were not displayed for offer creation.")
        return True

    def click_new_offer_button(self):
        WaitManager.wait_for_page_load(self.driver)
        submit_new_item = WaitManager.wait_for_element(self.driver, offer_new_item_button)
        time.sleep(2)
        submit_new_item.click()

    def click_options_offer_list(self):
        WaitManager.wait_for_page_load(self.driver)
        first_option = WaitManager.wait_for_element(self.driver, firs_option_offer)
        time.sleep(5)
        first_option.click()

    def click_download_offer_option(self):
        WaitManager.wait_for_page_load(self.driver)
        download_option = WaitManager.wait_for_element(self.driver, download_option_offer)
        download_option.click()

    def is_offer_pdf_downloaded(self, timeout=30):
        for _ in range(timeout):
            files = os.listdir(get_download_directory())
            if any(file.endswith(".pdf") for file in files):
                return True
            time.sleep(1)
        return False
