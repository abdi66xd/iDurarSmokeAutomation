import time

from utilities.WaitManager import WaitManager
from features.locators.DashboardLocators import logo_image_locator, \
    email_element_locator, avatar_icon_locator, people_tab_locator, companies_tab_locator, leads_tab_locator, \
    product_category_tab_locator, expenses_category_tab_locator, customer_category_tab_locator, products_tab_locator, \
    invoices_tab_locator, proformas_invoices_tab_locator, expenses_tab_locator


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def click_avatar_icon(self):
        login_button = WaitManager.wait_for_element(self.driver, avatar_icon_locator)
        login_button.click()

    def catch_mail_name(self):
        email = WaitManager.wait_for_element(self.driver, email_element_locator)
        return email.text

    def is_logo_loaded(self):
        time.sleep(1)
        logo = WaitManager.wait_for_element(self.driver, logo_image_locator)
        if logo:
            width = logo.get_attribute("naturalWidth")
            height = logo.get_attribute("naturalHeight")
            if width is not None and height is not None:
                return int(width) > 0 and int(height) > 0
        return False

    def click_people_tab(self):
        people_tab = WaitManager.wait_for_element(self.driver, people_tab_locator)
        time.sleep(3)
        people_tab.click()

    def click_companies_tab(self):
        companies_tab = WaitManager.wait_for_element(self.driver, companies_tab_locator)
        time.sleep(3)
        companies_tab.click()

    def click_leads_tab(self):
        companies_tab = WaitManager.wait_for_element(self.driver, leads_tab_locator)
        time.sleep(3)
        companies_tab.click()

    def click_products_category_tab(self):
        products_category_tab = WaitManager.wait_for_element(self.driver, product_category_tab_locator)
        time.sleep(3)
        products_category_tab.click()

    def click_expenses_category_tab(self):
        expenses_category_tab = WaitManager.wait_for_element(self.driver, expenses_category_tab_locator)
        time.sleep(3)
        expenses_category_tab.click()

    def click_customers_tab(self):
        customers_category_tab = WaitManager.wait_for_element(self.driver, customer_category_tab_locator)
        time.sleep(3)
        customers_category_tab.click()

    def click_products_tab(self):
        product_tab = WaitManager.wait_for_element(self.driver, products_tab_locator)
        time.sleep(3)
        product_tab.click()

    def click_invoices_tab(self):
        invoices_tab = WaitManager.wait_for_element(self.driver, invoices_tab_locator)
        time.sleep(3)
        invoices_tab.click()

    def click_proforma_invoices_tab(self):
        proforma_invoices_tab = WaitManager.wait_for_element(self.driver, proformas_invoices_tab_locator)
        time.sleep(3)
        proforma_invoices_tab.click()

    def click_expenses_tab(self):
        expenses_tab = WaitManager.wait_for_element(self.driver, expenses_tab_locator)
        time.sleep(3)
        expenses_tab.click()