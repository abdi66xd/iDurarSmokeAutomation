from selenium.webdriver.common.by import By

add_new_lead_button = (By.XPATH, "(//button[@type='button'])[2]")
lead_type_button_dropdown = (By.XPATH, "(//input[@id='type'])[2]")
lead_people_dropdown = (By.XPATH, "(//input[@id='rc_select_190'])[1]")
lead_notes_text_area = (By.XPATH, "(//textarea[@id='notes'])[2]")
lead_submit_button = (By.XPATH, "(//button[@type='submit'])[2]")
lead_source_dropdown = (By.XPATH, "(//input[@id='source'])[2]")
lead_confirmation_pop_up_locator = (By.CSS_SELECTOR, ".ant-notification-notice-success")
lead_whole_dialog = (By.XPATH, "//div[@role='dialog']")