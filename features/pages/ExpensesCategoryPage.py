import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys

from features.locators.ExpensesCategoriesLocators import add_new_expenses_button_categories_locator, \
    name_expenses_categories_locator, description_expenses_categories_locator, enable_expenses_categories_locator, \
    color_expenses_categories_locator, submit_button_expenses_categories_locator, popup_expenses_categories_locator, \
    expenses_name_alert_locator, expenses_description_alert_locator, expenses_color_alert_locator, \
    expenses_enabled_alert_locator

from utilities.WaitManager import WaitManager


class ExpensesCategoryPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_expenses_category_button(self):
        time.sleep(2)
        new_expense_button = WaitManager.wait_for_element(self.driver, add_new_expenses_button_categories_locator)
        time.sleep(2)
        new_expense_button.click()

    def fill_expenses_category_name_field(self, product_category_name_input):
        expenses_category_name = WaitManager.wait_for_element(self.driver, name_expenses_categories_locator)
        expenses_category_name.clear()
        expenses_category_name.send_keys(product_category_name_input)

    def fill_expenses_category_description_field(self, product_category_description_input):
        expenses_category_description = WaitManager.wait_for_element(self.driver, description_expenses_categories_locator)
        expenses_category_description.clear()
        expenses_category_description.send_keys(product_category_description_input)

    def click_enabled_expenses_category(self):
        expense_enabled = WaitManager.wait_for_element(self.driver, enable_expenses_categories_locator)
        time.sleep(3)
        expense_enabled.send_keys(Keys.ENTER)
        time.sleep(3)
        expense_enabled.send_keys(Keys.ENTER)

    def select_color_expenses_category(self):
        color_expenses_category = WaitManager.wait_for_element(self.driver, color_expenses_categories_locator)
        time.sleep(2)
        color_expenses_category.send_keys(Keys.TAB)
        time.sleep(2)
        color_expenses_category.send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        color_expenses_category.send_keys(Keys.ENTER)

    def click_expenses_category_submit_button(self):
        expenses_category_submit_button = WaitManager.wait_for_element(self.driver,
                                                                      submit_button_expenses_categories_locator)
        expenses_category_submit_button.click()

    def is_expenses_category_submitted_popup_displayed(self):
        try:
            WaitManager.wait_for_element(self.driver, popup_expenses_categories_locator)
            return True
        except TimeoutException:
            return False

    def is_expenses_category_alerts_displayed(self):
        alert_name = WaitManager.wait_for_element(self.driver, expenses_name_alert_locator)
        alert_description = WaitManager.wait_for_element(self.driver, expenses_description_alert_locator)
        alert_color = WaitManager.wait_for_element(self.driver, expenses_color_alert_locator)
        alert_enabled = WaitManager.wait_for_element(self.driver, expenses_enabled_alert_locator)
        if not (alert_name.is_displayed() and alert_description.is_displayed() and alert_color.is_displayed() and alert_enabled.is_displayed()):
            raise AssertionError("Some alert(s) were not displayed for the expenses category.")

        return True

