import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains

from features.locators.ExpensesLocators import add_new_expenses_locator, expenses_name_locator, \
    expenses_category_locator, expenses_currency_locator, expenses_price_locator, expenses_description_locator, \
    expenses_reference_locator, expenses_submit_locator, expenses_success_submitted_locator, \
    enter_expenses_name_alert_locator, enter_expenses_category_alert_locator, enter_expenses_price_alert_locator
from features.locators.ProductsLocators import enter_product_name_alert_locator, \
    enter_product_category_alert_locator, enter_product_price_alert_locator
from utilities.WaitManager import WaitManager

from selenium.webdriver.common.keys import Keys


class ExpensesPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_expense_button(self):
        WaitManager.wait_for_page_load(self.driver)
        time.sleep(3)
        new_expense_button = WaitManager.wait_for_element(self.driver, add_new_expenses_locator)
        time.sleep(3)
        new_expense_button.click()

    def fill_expense_name_field(self, expenses_name):
        WaitManager.wait_for_page_load(self.driver)
        product_expense_field = WaitManager.wait_for_element(self.driver, expenses_name_locator)
        product_expense_field.clear()
        product_expense_field.send_keys(expenses_name)

    def select_expense_category_field(self):
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

    def select_expense_currency_field(self):
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

    def fill_expense_price_field(self, expense_price):
        WaitManager.wait_for_page_load(self.driver)
        expense_price_dropdown = WaitManager.wait_for_element(self.driver, expenses_price_locator)
        time.sleep(2)
        expense_price_dropdown.send_keys(expense_price)

    def fill_expense_description_field(self, expense_description):
        WaitManager.wait_for_page_load(self.driver)
        expense_description_field = WaitManager.wait_for_element(self.driver, expenses_description_locator)
        expense_description_field.clear()
        expense_description_field.send_keys(expense_description)

    def fill_expense_ref_field(self, expense_reference):
        WaitManager.wait_for_page_load(self.driver)
        expense_ref_field = WaitManager.wait_for_element(self.driver, expenses_reference_locator)
        expense_ref_field.clear()
        expense_ref_field.send_keys(expense_reference)

    def click_submit_new_expense_button(self):
        WaitManager.wait_for_page_load(self.driver)
        submit_expense_button = WaitManager.wait_for_element(self.driver, expenses_submit_locator)
        submit_expense_button.click()

    def is_expense_submitted_popup_displayed(self):
        WaitManager.wait_for_page_load(self.driver)
        try:
            WaitManager.wait_for_element(self.driver, expenses_success_submitted_locator)
            return True
        except TimeoutException:
            return False

    def is_expenses_alerts_displayed(self):
        alert_expense_name = WaitManager.wait_for_element(self.driver, enter_expenses_name_alert_locator)
        alert_expense_category = WaitManager.wait_for_element(self.driver, enter_expenses_category_alert_locator)
        alert_expense_price = WaitManager.wait_for_element(self.driver, enter_expenses_price_alert_locator)
        if not (
                alert_expense_name.is_displayed() and alert_expense_category.is_displayed() and alert_expense_price.is_displayed()):
            raise AssertionError("Some alert(s) were not displayed for expenses creation.")
        return True
