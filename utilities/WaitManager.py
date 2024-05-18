from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitManager:
    @classmethod
    def wait_for_element(cls, driver, locator, timeout=4, retry_attempts=5):
        attempts = 0
        while attempts < retry_attempts:
            try:
                element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
                return element
            except TimeoutException:
                print("TimeoutException occurred. Retrying...")
            except StaleElementReferenceException:
                print("StaleElementReferenceException occurred. Retrying...")
            attempts += 1

    @classmethod
    def wait_for_page_load(cls, driver, timeout=100):
        WebDriverWait(driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    @classmethod
    def wait_for_url_change(cls, driver, current_url, timeout=20):
        WebDriverWait(driver, timeout).until(
            lambda driver: driver.current_url != current_url
        )

    @classmethod
    def safe_click(cls, driver):
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            try:
                driver.click()
                break
            except StaleElementReferenceException:
                attempts += 1
