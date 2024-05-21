import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains

from features.locators.ProformaInvoiceLocators import add_new_proforma_invoice_button, client_proforma_invoice_field, \
    item_name_proforma_invoice_field, quantity_proforma_invoice_field, price_proforma_invoice_field, \
    save_proforma_invoice_button, proforma_invoice_notification_xpath, proforma_invoice_client_alert, \
    proforma_invoice_tax_alert, proforma_invoice_price_alert, proforma_invoice_quantity_alert, \
    proforma_invoice_item_name_alert, proforma_add_new_item_button
from utilities.WaitManager import WaitManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProformaInvoicePage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_proforma_invoice_button(self):
        WaitManager.wait_for_page_load(self.driver)
        time.sleep(2)
        new_product_button = WaitManager.wait_for_element(self.driver, add_new_proforma_invoice_button)
        time.sleep(2)
        new_product_button.click()

    def select_client_proforma_invoice_field(self):
        WaitManager.wait_for_page_load(self.driver)
        client_name_invoice_field = WaitManager.wait_for_element(self.driver, client_proforma_invoice_field)
        time.sleep(2)
        client_name_invoice_field.clear()
        client_name_invoice_field.click()
        time.sleep(2)
        client_name_invoice_field.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        client_name_invoice_field.send_keys(Keys.ENTER)

    def select_proforma_client_tax_field(self):
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

    def fill_proforma_item_name_field(self, item_name):
        WaitManager.wait_for_page_load(self.driver)
        item_field = WaitManager.wait_for_element(self.driver, item_name_proforma_invoice_field)
        item_field.clear()
        time.sleep(2)
        item_field.send_keys(item_name)
        item_field.send_keys(Keys.ENTER)

    def fill_proforma_item_quantity_field(self, item_quantity):
        WaitManager.wait_for_page_load(self.driver)
        item_quantity_field = WaitManager.wait_for_element(self.driver, quantity_proforma_invoice_field)
        item_quantity_field.clear()
        time.sleep(2)
        item_quantity_field.send_keys(5)

    def fill_proforma_item_price_field(self, item_price):
        WaitManager.wait_for_page_load(self.driver)
        item_price_field = WaitManager.wait_for_element(self.driver, price_proforma_invoice_field)
        item_price_field.clear()
        time.sleep(2)
        item_price_field.send_keys(5)

    def click_submit_new_proforma_invoice_button(self):
        WaitManager.wait_for_page_load(self.driver)
        submit_invoice_button = WaitManager.wait_for_element(self.driver, save_proforma_invoice_button)
        time.sleep(2)
        submit_invoice_button.click()

    def is_proforma_invoice_submitted_popup_displayed(self):
        WaitManager.wait_for_page_load(self.driver)
        try:
            WaitManager.wait_for_element(self.driver, proforma_invoice_notification_xpath)
            return True
        except TimeoutException:
            return False

    def are__proforma_invoice_alerts_displayed(self):
        proforma_client_alert = WaitManager.wait_for_element(self.driver, proforma_invoice_client_alert)
        proforma_invoice_item_name_alerts = WaitManager.wait_for_element(self.driver, proforma_invoice_item_name_alert)
        proforma_invoice_quantity = WaitManager.wait_for_element(self.driver, proforma_invoice_quantity_alert)
        proforma_invoice_price = WaitManager.wait_for_element(self.driver, proforma_invoice_price_alert)
        proforma_invoice_tax = WaitManager.wait_for_element(self.driver, proforma_invoice_tax_alert)
        if not (
                proforma_client_alert.is_displayed()
                and proforma_invoice_item_name_alerts.is_displayed()
                and proforma_invoice_quantity.is_displayed()
                and proforma_invoice_price.is_displayed()
                and proforma_invoice_tax.is_displayed()):
            raise AssertionError("Some alert(s) were not displayed for proforma creation.")
        return True

    def click_new_proforma_item_button(self):
        WaitManager.wait_for_page_load(self.driver)
        submit_new_item = WaitManager.wait_for_element(self.driver, proforma_add_new_item_button)
        time.sleep(2)
        submit_new_item.click()
