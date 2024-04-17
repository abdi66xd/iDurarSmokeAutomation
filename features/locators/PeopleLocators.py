from selenium.webdriver.common.by import By

new_person_button_locator = (By.XPATH,
                             "//button[@class='ant-btn css-16v3ahg ant-btn-primary']")
first_name_locator = (By.XPATH, "(//input[@id='firstname'])[2]")
last_name_locator = (By.XPATH, "(//input[@id='lastname'])[2]")
submit_new_person_button_locator = (By.XPATH, "//div[@class='BottomCollapseBox']//div//button[@type='submit']")
close_icon_locator = (By.XPATH, "//span[@class='anticon anticon-close']")
people_submitted_popup_locator = (By.XPATH, "//div[@class='ant-notification-notice ant-notification-notice-success "
                                            "ant-notification-notice-closable']")
people_phone_number_locator = (By.XPATH, "(//input[@id='phone'])[2]")
people_email_locator = (By.XPATH, "(//input[@id='email'])[2]")
