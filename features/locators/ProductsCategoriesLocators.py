from selenium.webdriver.common.by import By

new_product_category_locator = (By.XPATH, "//span[normalize-space()='Add New Product Category']")
name_product_category_locator = (By.XPATH, "(//input[@id='name'])[2]")
description_product_category_locator = (By.XPATH, "(//textarea[@id='description'])[2]")
enabled_product_category_locator = (By.XPATH, "(//button[@id='enabled'])[2]")
submit_button_product_category_locator = (By.XPATH, "(//button[@type='submit'])[2]")
pop_up_product_category_locator = (By.CSS_SELECTOR, ".ant-notification-notice-wrapper")
drawer = (By.XPATH, "//button[@aria-label='Close']")
drawer_content = (By.XPATH, "//div[@class='ant-drawer-content-wrapper']")
color_product_category_dropdown = (By.XPATH, "(//input[@id='color'])[2]")
