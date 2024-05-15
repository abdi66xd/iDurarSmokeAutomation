from selenium.webdriver.common.by import By

add_new_expenses_button_categories_locator = (By.XPATH, "(//span[normalize-space()='Add New Expense Category'])[1]")
name_expenses_categories_locator = (By.XPATH, "(//input[@id='name'])[2]")
description_expenses_categories_locator = (By.XPATH, "(//textarea[@id='description'])[2]")
color_expenses_categories_locator = (By.XPATH, "(//input[@id='color'])[2]")
enable_expenses_categories_locator = (By.XPATH, "(//button[@id='enabled'])[2]")
submit_button_expenses_categories_locator = (By.XPATH, "(//button[@type='submit'])[2]")
popup_expenses_categories_locator = (By.CSS_SELECTOR, ".ant-notification-notice-wrapper")
request_expenses_categories_locator = (By.CSS_SELECTOR, "div[class='BottomCollapseBox'] div button[type='submit']")
expenses_name_alert_locator = (By.XPATH, "//div[contains(text(),'Please enter Name')]")
expenses_description_alert_locator = (By.XPATH, "//div[contains(text(),'Please enter Description')]")
expenses_color_alert_locator = (By.XPATH, "//div[contains(text(),'Please enter Color')]")
expenses_enabled_alert_locator = (By.XPATH, "//div[contains(text(),'Please enter Enabled')]")
