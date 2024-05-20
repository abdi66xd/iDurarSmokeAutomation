import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains

from features.locators.ProductsLocators import add_new_product_locator, product_name_locator, product_category_locator, \
    product_currency_locator, product_price_locator, product_description_locator, product_reference_locator, \
    product_submit_locator, success_submitted_locator, enter_product_name_alert_locator, \
    enter_product_category_alert_locator, enter_product_price_alert_locator
from utilities.WaitManager import WaitManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_product_button(self):
        WaitManager.wait_for_page_load(self.driver)
        time.sleep(2)
        new_product_button = WaitManager.wait_for_element(self.driver, add_new_product_locator)
        time.sleep(2)
        new_product_button.click()

    def fill_product_name_field(self, product_name):
        WaitManager.wait_for_page_load(self.driver)
        product_name_field = WaitManager.wait_for_element(self.driver, product_name_locator)
        product_name_field.clear()
        product_name_field.send_keys(product_name)

    def select_product_category_field(self):
        WaitManager.wait_for_page_load(self.driver)
        action_chains = ActionChains(self.driver)
        time.sleep(2)
        action_chains.send_keys(Keys.TAB)
        time.sleep(2)
        action_chains.send_keys(Keys.ENTER)
        time.sleep(2)
        action_chains.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        action_chains.send_keys(Keys.ENTER)
        action_chains.perform()

    def select_product_currency_field(self):
        WaitManager.wait_for_page_load(self.driver)
        action_chains = ActionChains(self.driver)
        time.sleep(2)
        action_chains.send_keys(Keys.TAB)
        time.sleep(2)
        action_chains.send_keys(Keys.ENTER)
        time.sleep(2)
        action_chains.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        action_chains.send_keys(Keys.ENTER)
        action_chains.perform()

    def fill_product_price_field(self, product_price):
        WaitManager.wait_for_page_load(self.driver)
        product_price_field = WaitManager.wait_for_element(self.driver, product_price_locator)
        product_price_field.clear()
        product_price_field.send_keys(product_price)

    def fill_product_description_field(self, product_description):
        WaitManager.wait_for_page_load(self.driver)
        product_description_field = WaitManager.wait_for_element(self.driver, product_description_locator)
        product_description_field.clear()
        product_description_field.send_keys(product_description)

    def fill_product_ref_field(self, product_reference):
        WaitManager.wait_for_page_load(self.driver)
        product_ref_field = WaitManager.wait_for_element(self.driver, product_reference_locator)
        product_ref_field.clear()
        product_ref_field.send_keys(product_reference)

    def click_submit_new_product_button(self):
        WaitManager.wait_for_page_load(self.driver)
        submit_product_button = WaitManager.wait_for_element(self.driver, product_submit_locator)
        submit_product_button.click()

    def is_product_submitted_popup_displayed(self):
        WaitManager.wait_for_page_load(self.driver)
        try:
            WaitManager.wait_for_element(self.driver, success_submitted_locator)
            return True
        except TimeoutException:
            return False

    def is_expenses_category_alerts_displayed(self):
        alert_product_name = WaitManager.wait_for_element(self.driver, enter_product_name_alert_locator)
        alert_product_category = WaitManager.wait_for_element(self.driver, enter_product_category_alert_locator)
        alert_product_price = WaitManager.wait_for_element(self.driver, enter_product_price_alert_locator)
        if not (
                alert_product_name.is_displayed() and alert_product_category.is_displayed() and alert_product_price.is_displayed()):
            raise AssertionError("Some alert(s) were not displayed for products creation.")

        return True
