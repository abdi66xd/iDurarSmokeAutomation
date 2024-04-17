from selenium.webdriver.common.by import By

add_new_company_locator = (By.XPATH, "//span[normalize-space()='Add New Company']")
company_name_locator = (By.XPATH, "//div[@class='BottomCollapseBox']//div//div[@class='ant-row css-16v3ahg']//div["
                                  "@class='ant-col ant-col-24 css-16v3ahg']//div[@class='ant-spin-nested-loading "
                                  "css-16v3ahg']//div[@class='ant-spin-container']//form[@class='ant-form "
                                  "ant-form-vertical css-16v3ahg']//div//input[@id='name']")
company_contact_locator = (By.CSS_SELECTOR, "#rc_select_10")
company_country_locator = (By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > "
                                            "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child("
                                            "3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > "
                                            "div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child("
                                            "1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > "
                                            "div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child("
                                            "1) > div:nth-child(1) > span:nth-child(1) > input:nth-child(1)")
company_phone_locator = (By.XPATH, "//div[@class='BottomCollapseBox']//div//div[@class='ant-row css-16v3ahg']//div["
                                   "@class='ant-col ant-col-24 css-16v3ahg']//div[@class='ant-spin-nested-loading "
                                   "css-16v3ahg']//div[@class='ant-spin-container']//form[@class='ant-form "
                                   "ant-form-vertical css-16v3ahg']//div//input[@id='phone']")
company_email_locator = (By.XPATH, "//div[@class='BottomCollapseBox']//div//div[@class='ant-row css-16v3ahg']//div["
                                   "@class='ant-col ant-col-24 css-16v3ahg']//div[@class='ant-spin-nested-loading "
                                   "css-16v3ahg']//div[@class='ant-spin-container']//form[@class='ant-form "
                                   "ant-form-vertical css-16v3ahg']//div//input[@id='email']")
company_website_locator = (By.XPATH, "//div[@class='BottomCollapseBox']//div//div[@class='ant-row css-16v3ahg']//div["
                                     "@class='ant-col ant-col-24 css-16v3ahg']//div[@class='ant-spin-nested-loading "
                                     "css-16v3ahg']//div[@class='ant-spin-container']//form[@class='ant-form "
                                     "ant-form-vertical css-16v3ahg']//div//input[@id='website']")
company_submit_button_locator = (By.XPATH, "//div[@class='BottomCollapseBox']//div//button[@type='submit']")
company_submitted_pop_up_locator = (By.XPATH, "//div[@class='ant-notification-notice-wrapper']//div[contains(@class, 'ant-notification-notice-success')]")