from selenium.webdriver.common.by import By

add_new_client_button = (By.XPATH, "(//button[@class='ant-btn css-16v3ahg ant-btn-primary'])[1]")
type_client_dropdown = (By.XPATH, "//div[3]/div/div/div/div/div/form/div/div/div/div[2]/div/div/div/div/span/input")
people_client_dropdown = (By.XPATH, "(//input[@role='combobox'])[7]")
company_client_dropdown = (By.XPATH, "(//input[@role='combobox'])[7]")
submit_client_button_f = (By.XPATH, "(//button[@type='submit'])[2]")
success_client_created_button = (By.XPATH, "(//div[@id='loom-companion-mv3'])[1]")
error_client_popup = (By.XPATH, "(//div[@class='ant-notification-notice ant-notification-notice-error ant-notification-notice-closable'])[1]")