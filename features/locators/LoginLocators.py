from selenium.webdriver.common.by import By

email_locator = (By.XPATH, "//input[@id='normal_login_email']")
password_locator = (By.XPATH, "//input[@id='normal_login_password']")
login_button_locator = (By.XPATH, "//span[normalize-space()='Log In']")
dashboard_logo_locator = (By.XPATH, "//img[@src='/assets/logo-text-B-YMIDGj.svg']")
email_alert_locator = (By.XPATH, "//div[@class='ant-form-item-explain-error']")
invalid_credentials_alert_locator = (By.XPATH, "//div[@class='ant-notification-notice-description']")
