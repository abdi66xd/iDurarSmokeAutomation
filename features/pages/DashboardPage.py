from utilities.WaitManager import WaitManager
from features.locators.DashboardLocators import logo_image_locator, \
    email_element_locator, avatar_icon_locator, people_tab_locator, companies_tab_locator, leads_tab_locator, \
    product_category_tab_locator


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
        logo = WaitManager.wait_for_element(self.driver, logo_image_locator)
        if logo:
            width = logo.get_attribute("naturalWidth")
            height = logo.get_attribute("naturalHeight")
            if width is not None and height is not None:
                return int(width) > 0 and int(height) > 0
        return False

    def click_people_tab(self):
        people_tab = WaitManager.wait_for_element(self.driver, people_tab_locator)
        people_tab.click()

    def click_companies_tab(self):
        companies_tab = WaitManager.wait_for_element(self.driver, companies_tab_locator)
        companies_tab.click()

    def click_leads_tab(self):
        companies_tab = WaitManager.wait_for_element(self.driver, leads_tab_locator)
        companies_tab.click()

    def click_products_category_tab(self):
        products_category_tab = WaitManager.wait_for_element(self.driver, product_category_tab_locator)
        products_category_tab.click()