from selenium.webdriver.common.by import By

add_new_invoice_button = (By.XPATH, "button[class='ant-btn css-16v3ahg ant-btn-primary']")
client_invoice_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
item_name_invoice_field = (By.XPATH, "(//input[@id='items_0_itemName'])[1]")
quantity_invoice_field = (By.XPATH, "(//input[@id='items_0_quantity'])[1]")
price_invoice_field = (By.XPATH, "(//input[@id='items_0_price'])[1]")
tax_rate_invoice_dropdown = (By.CSS_SELECTOR, "div[class='ant-col ant-col-4 ant-col-offset-15 gutter-row css-16v3ahg'] input[role='combobox']")
save_invoice_button = (By.XPATH, "(//button[@type='submit'])[1]")
invoice_notification_xpath = (By.XPATH, "//div[contains(@class, 'ant-notification-notice-wrapper') and //div[contains(text(), 'Request success')]]")
add_new_item_button = (By.XPATH, "(//button[@class='ant-btn css-16v3ahg ant-btn-dashed ant-btn-block'])[1]")
invoice_client_alert = (By.XPATH, "(//div[contains(text(),'Please enter Client')])[1]")
invoice_item_name_alert = (By.XPATH, "(//div[contains(text(),'Missing itemName name')])[1]")
invoice_quantity_alert = (By.XPATH, "(//div[contains(text(),'Please enter 0,quantity')])[1]")
invoice_price_alert = (By.XPATH, "(//div[contains(text(),'Please enter 0,price')])[1]")
invoice_tax_alert = (By.XPATH, "(//div[contains(text(),'Please enter taxRate')])[1]")
firs_option_invoices = (By.XPATH, "//span[@aria-label='ellipsis']//*[name()='svg']")
download_option_invoices = (By.XPATH, "(//span[normalize-space()='Download'])[1]")