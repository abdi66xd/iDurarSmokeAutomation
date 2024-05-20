from selenium.webdriver.common.by import By

add_new_product_locator = (By.XPATH, "(//button[@class='ant-btn css-16v3ahg ant-btn-primary'])[1]")
product_name_locator = (By.XPATH, "(//input[@id='name'])[2]")
product_category_locator = (By.XPATH, "//a[contains(text(), 'select')]")
product_currency_locator = (By.XPATH, "(//input[@role='combobox'])[6]")
product_price_locator = (By.XPATH, "(//input[@id='price'])[2]")
product_description_locator = (By.XPATH, "(//textarea[@id='description'])[2]")
product_reference_locator = (By.XPATH, "(//input[@id='ref'])[2]")
product_submit_locator = (By.XPATH, "(//button[@type='submit'])[2]")
success_submitted_locator = (By.XPATH, "//div[contains(@class, 'ant-notification-notice-wrapper') and contains("
                                       "@style, 'transform: translate3d(0px, 0px, 0px);')]")
enter_product_name_alert_locator = (By.XPATH, "(//div[contains(text(),'Please enter Name')])[1]")
enter_product_category_alert_locator = (By.XPATH, "(//div[contains(text(),'Please enter Product Category')])[1]")
enter_product_price_alert_locator = (By.XPATH, "(//div[contains(text(),'Please enter Price')])[1]")