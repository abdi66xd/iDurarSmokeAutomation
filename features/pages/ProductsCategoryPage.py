import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from features.locators.LeadsLocators import add_new_lead_button, lead_confirmation_pop_up_locator
from features.locators.ProductsCategoriesLocators import name_product_category_locator, \
    description_product_category_locator, enabled_product_category_locator, submit_button_product_category_locator, \
    pop_up_product_category_locator
from utilities.WaitManager import WaitManager


class ProductsCategoryPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_product_category_button(self):
        time.sleep(2)
        lead_button = WaitManager.wait_for_element(self.driver, add_new_lead_button)
        time.sleep(2)
        lead_button.click()

    def fill_product_category_name_field(self, product_category_name_input):
        product_category_name = WaitManager.wait_for_element(self.driver, name_product_category_locator)
        product_category_name.clear()
        product_category_name.send_keys(product_category_name_input)

    def fill_product_category_description_field(self, product_category_description_input):
        product_category_description = WaitManager.wait_for_element(self.driver, description_product_category_locator)
        product_category_description.clear()
        product_category_description.send_keys(product_category_description_input)

    def click_enabled_product_category(self):
        product_enabled = WaitManager.wait_for_element(self.driver, enabled_product_category_locator)
        product_enabled.click()

    def click_product_category_submit_button(self):
        product_category_submit_button = WaitManager.wait_for_element(self.driver, submit_button_product_category_locator)
        product_category_submit_button.click()

    def is_product_category_submitted_popup_displayed(self):
        try:
            WaitManager.wait_for_element(self.driver, pop_up_product_category_locator)
            return True
        except TimeoutException:
            return False


