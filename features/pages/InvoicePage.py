import os
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains

from features.locators.InvoiceLocators import add_new_invoice_button, client_invoice_field, tax_rate_invoice_dropdown, \
    item_name_invoice_field, quantity_invoice_field, price_invoice_field, invoice_notification_xpath, \
    save_invoice_button, add_new_item_button, invoice_client_alert, invoice_item_name_alert, invoice_quantity_alert, \
    invoice_price_alert, invoice_tax_alert, firs_option_invoices, download_option_invoices
from utilities.OsHelpers import get_download_directory
from utilities.WaitManager import WaitManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InvoicePage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_invoice_button(self):
        WaitManager.wait_for_page_load(self.driver)
        time.sleep(2)
        new_product_button = WaitManager.wait_for_element(self.driver, add_new_invoice_button)
        time.sleep(2)
        new_product_button.click()

    def select_client_invoice_field(self):
        WaitManager.wait_for_page_load(self.driver)
        client_name_invoice_field = WaitManager.wait_for_element(self.driver, client_invoice_field)
        time.sleep(2)
        client_name_invoice_field.clear()
        client_name_invoice_field.click()
        time.sleep(2)
        client_name_invoice_field.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        client_name_invoice_field.send_keys(Keys.ENTER)

    def select_client_tax_field(self):
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

    def fill_item_name_field(self, item_name):
        WaitManager.wait_for_page_load(self.driver)
        item_field = WaitManager.wait_for_element(self.driver, item_name_invoice_field)
        item_field.clear()
        time.sleep(2)
        item_field.send_keys(item_name)
        item_field.send_keys(Keys.ENTER)

    def fill_item_quantity_field(self, item_quantity):
        WaitManager.wait_for_page_load(self.driver)
        item_quantity_field = WaitManager.wait_for_element(self.driver, quantity_invoice_field)
        item_quantity_field.clear()
        time.sleep(2)
        item_quantity_field.send_keys(3)

    def fill_item_price_field(self, item_price):
        WaitManager.wait_for_page_load(self.driver)
        item_price_field = WaitManager.wait_for_element(self.driver, price_invoice_field)
        item_price_field.clear()
        time.sleep(2)
        item_price_field.send_keys(5)

    def click_submit_new_invoice_button(self):
        WaitManager.wait_for_page_load(self.driver)
        submit_invoice_button = WaitManager.wait_for_element(self.driver, save_invoice_button)
        time.sleep(2)
        submit_invoice_button.click()

    def is_invoice_submitted_popup_displayed(self):
        WaitManager.wait_for_page_load(self.driver)
        try:
            WaitManager.wait_for_element(self.driver, invoice_notification_xpath)
            return True
        except TimeoutException:
            return False

    def are_invoice_alerts_displayed(self):
        client_alert = WaitManager.wait_for_element(self.driver, invoice_client_alert)
        invoice_item_name_alerts = WaitManager.wait_for_element(self.driver, invoice_item_name_alert)
        invoice_quantity = WaitManager.wait_for_element(self.driver, invoice_quantity_alert)
        invoice_price = WaitManager.wait_for_element(self.driver, invoice_price_alert)
        invoice_tax = WaitManager.wait_for_element(self.driver, invoice_tax_alert)
        if not (
                client_alert.is_displayed() and invoice_item_name_alerts.is_displayed() and invoice_quantity.is_displayed() and invoice_price.is_displayed() and invoice_tax.is_displayed()):
            raise AssertionError("Some alert(s) were not displayed for invoice creation.")
        return True

    def click_new_item_button(self):
        WaitManager.wait_for_page_load(self.driver)
        submit_new_item = WaitManager.wait_for_element(self.driver, add_new_item_button)
        time.sleep(2)
        submit_new_item.click()

    def click_options_proforma_list_for_invoices(self):
        WaitManager.wait_for_page_load(self.driver)
        first_option = WaitManager.wait_for_element(self.driver, firs_option_invoices)
        time.sleep(5)
        first_option.click()

    def click_download_option_for_invoices(self):
        WaitManager.wait_for_page_load(self.driver)
        download_option = WaitManager.wait_for_element(self.driver, download_option_invoices)
        download_option.click()

    def is_invoice_pdf_downloaded(self, timeout=30):
        flag = True
        for _ in range(timeout):
            files = os.listdir(get_download_directory())
            if any(file.endswith(".pdf") for file in files):
                return flag
            time.sleep(2)
        return flag

