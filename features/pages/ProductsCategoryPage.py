import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from features.locators.LeadsLocators import add_new_lead_button, lead_confirmation_pop_up_locator
from features.locators.ProductsCategoriesLocators import name_product_category_locator, \
    description_product_category_locator, enabled_product_category_locator, submit_button_product_category_locator, \
    pop_up_product_category_locator, color_product_category_dropdown, product_name_alert_locator, \
    product_description_alert_locator, product_color_alert_locator, product_enabled_alert_locator
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
        time.sleep(3)
        product_enabled.send_keys(Keys.TAB)
        time.sleep(3)
        product_enabled.send_keys(Keys.ENTER)

    def select_color_product_category(self):
        color_product_category = WaitManager.wait_for_element(self.driver, color_product_category_dropdown)
        time.sleep(2)
        color_product_category.send_keys(Keys.TAB)
        time.sleep(2)
        color_product_category.send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        color_product_category.send_keys(Keys.ENTER)

    def click_product_category_submit_button(self):
        product_category_submit_button = WaitManager.wait_for_element(self.driver,
                                                                      submit_button_product_category_locator)
        product_category_submit_button.click()

    def is_product_category_submitted_popup_displayed(self):
        try:
            WaitManager.wait_for_element(self.driver, pop_up_product_category_locator)
            return True
        except TimeoutException:
            return False

    def is_products_category_alerts_displayed(self):
        alert_name = WaitManager.wait_for_element(self.driver, product_name_alert_locator)
        alert_description = WaitManager.wait_for_element(self.driver, product_description_alert_locator)
        alert_color = WaitManager.wait_for_element(self.driver, product_color_alert_locator)
        alert_enabled = WaitManager.wait_for_element(self.driver, product_enabled_alert_locator)
        if not (alert_name.is_displayed() and alert_description.is_displayed() and alert_color.is_displayed() and alert_enabled.is_displayed()):
            raise AssertionError("Some alert(s) were not displayed for the products category.")

        return True
