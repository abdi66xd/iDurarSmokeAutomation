from selenium.webdriver.common.by import By

add_new_client_button = (By.XPATH, "(//button[@class='ant-btn css-16v3ahg ant-btn-primary'])[1]")
type_client_dropdown = (By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > input:nth-child(1)")
people_client_dropdown = (By.XPATH, "(//input[@role='combobox'])[7]")
company_client_dropdown = (By.XPATH, "(//input[@role='combobox'])[7]")
submit_client_button_f = (By.XPATH, "(//button[@type='submit'])[2]")
success_client_created_button = (By.XPATH, "(//div[@id='loom-companion-mv3'])[1]")