from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitManager:
    @classmethod
    def wait_for_element(cls, driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

    @classmethod
    def wait_for_page_load(cls, driver, timeout=10):
        WebDriverWait(driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
