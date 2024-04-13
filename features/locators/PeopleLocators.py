from selenium.webdriver.common.by import By

new_person_button_locator = (By.XPATH,
                             "//button[@class='ant-btn css-16v3ahg ant-btn-primary']")
first_name_locator = (By.XPATH, "//div[@class='BottomCollapseBox']//div//div[@class='ant-row css-16v3ahg']//div["
                                "@class='ant-col ant-col-24 css-16v3ahg']//div[@class='ant-spin-nested-loading "
                                "css-16v3ahg']//div[@class='ant-spin-container']//form[@class='ant-form "
                                "ant-form-vertical"
                                "css-16v3ahg']//div//input[@id='firstname']")
last_name_locator = (By.XPATH, "//div[@class='BottomCollapseBox']//div//div[@class='ant-row css-16v3ahg']//div["
                               "@class='ant-col ant-col-24 css-16v3ahg']//div[@class='ant-spin-nested-loading "
                               "css-16v3ahg']//div[@class='ant-spin-container']//form[@class='ant-form "
                               "ant-form-vertical"
                               "css-16v3ahg']//div//input[@id='lastname']")
submit_new_person_button_locator = (By.XPATH, "//div[@class='BottomCollapseBox']//div//button[@type='submit']")
close_icon_locator = (By.XPATH, "//span[@class='anticon anticon-close']")
people_submitted_popup_locator = (By.XPATH, "//div[@class='ant-notification-notice ant-notification-notice-success "
                                            "ant-notification-notice-closable']")
