from selenium.webdriver.common.by import By

add_new_expenses_locator = (By.XPATH, "(//button[@type='button'])[2]")
expenses_name_locator = (By.XPATH, "(//input[@id='name'])[2]")
expenses_category_locator = (By.XPATH, "(//input)[10]")
expenses_currency_locator = (By.XPATH, "(//input)[11]")
expenses_price_locator = (By.XPATH, "//div[@class='BottomCollapseBox']//div//div[@class='ant-row css-16v3ahg']//div[@class='ant-col ant-col-24 css-16v3ahg']//div[@class='ant-spin-nested-loading css-16v3ahg']//div[@class='ant-spin-container']//form[@class='ant-form ant-form-vertical css-16v3ahg']//div//input[@id='total']")
expenses_description_locator = (By.XPATH, "(//textarea[@id='description'])[2]")
expenses_reference_locator = (By.XPATH, "(//input[@id='ref'])[2]")
expenses_submit_locator = (By.XPATH, "(//button[@type='submit'])[2]")
expenses_success_submitted_locator = (By.XPATH, "//div[@class='ant-notification-notice-wrapper' and contains(@style, "
                                                "'transform: translate3d(0px, 0px, 0px);')]")
enter_expenses_name_alert_locator = (By.XPATH, "(//div[contains(text(),'Please enter Name')])[1]")
enter_expenses_category_alert_locator = (By.XPATH, "(//div[contains(text(),'Please enter Expense Category')])[1]")
enter_expenses_price_alert_locator = (By.XPATH, "(//div[contains(text(),'Please enter Total')])[1]")
