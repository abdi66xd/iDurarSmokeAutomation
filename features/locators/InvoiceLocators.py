from selenium.webdriver.common.by import By

add_new_invoice_button = (By.XPATH, "(//button[@class='ant-btn css-16v3ahg ant-btn-primary'])[1]")
client_invoice_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
item_name_invoice_field = (By.XPATH, "(//input[@id='items_0_itemName'])[1]")
quantity_invoice_field = (By.XPATH, "(//input[@id='items_0_quantity'])[1]")
price_invoice_field = (By.XPATH, "(//input[@id='items_0_price'])[1]")
tax_rate_invoice_dropdown = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[3]/div[1]/form[1]/div[7]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
save_invoice_button = (By.XPATH, "(//button[@type='submit'])[1]")
invoice_notification_xpath = (By.XPATH, "//div[contains(@class, 'ant-notification-notice-wrapper') and //div[contains(text(), 'Request success')]]")
add_new_item_button = (By.XPATH, "(//button[@class='ant-btn css-16v3ahg ant-btn-dashed ant-btn-block'])[1]")
