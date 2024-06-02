import time

from allure_commons.types import AttachmentType
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys, ActionChains

from features.locators.ExpensesLocators import add_new_expenses_locator, expenses_name_locator, \
    expenses_category_locator, expenses_currency_locator, expenses_price_locator, expenses_description_locator, \
    expenses_reference_locator, expenses_submit_locator, expenses_success_submitted_locator, \
    enter_expenses_name_alert_locator, enter_expenses_category_alert_locator, enter_expenses_price_alert_locator, \
    expenses_first_option_menu, show_option_of_menu, name_show_label, expense_show_label, currency_show_label, \
    total_show_label, description_show_label, ref_show_label
from features.locators.ProductsLocators import enter_product_name_alert_locator, \
    enter_product_category_alert_locator, enter_product_price_alert_locator
from utilities.WaitManager import WaitManager
import allure
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

    def click_expenses_options(self):
        expenses_options = WaitManager.wait_for_element(self.driver, expenses_first_option_menu)
        time.sleep(3)
        expenses_options.click()
        time.sleep(3)

    def click_show_expense_option(self):
        show_expenses_options = WaitManager.wait_for_element(self.driver, show_option_of_menu)
        time.sleep(3)
        show_expenses_options.click()
        time.sleep(3)

    from allure_commons.types import AttachmentType

    def are_labels_content_translated_to_spanish(self):
        expense_name_showed = WaitManager.wait_for_element(self.driver, name_show_label)
        expense_category_showed = WaitManager.wait_for_element(self.driver, expense_show_label)
        expense_currency_showed = WaitManager.wait_for_element(self.driver, currency_show_label)
        expense_total_showed = WaitManager.wait_for_element(self.driver, total_show_label)
        expense_description_showed = WaitManager.wait_for_element(self.driver, description_show_label)
        expense_reference_showed = WaitManager.wait_for_element(self.driver, ref_show_label)

        result = True
        incorrect_fields = []

        if expense_name_showed.text != "Nombre":
            result = False
            incorrect_fields.append("Nombre")

        if expense_category_showed.text != "Categoría de gasto":
            result = False
            incorrect_fields.append("Categoría de gasto")

        if expense_currency_showed.text != "Moneda":
            result = False
            incorrect_fields.append("Moneda")

        if expense_total_showed.text != "Total":
            result = False
            incorrect_fields.append("Total")

        if expense_description_showed.text != "Descripción":
            result = False
            incorrect_fields.append("Descripción")

        if expense_reference_showed.text != "Ref":
            result = False
            incorrect_fields.append("Ref")

        if not result:
            error_message = f"Following fields are not translated correctly: {', '.join(incorrect_fields)}"
            allure.attach(error_message, name="Incorrect Fields", attachment_type=AttachmentType.TEXT)
            raise AssertionError(error_message)

        return result



