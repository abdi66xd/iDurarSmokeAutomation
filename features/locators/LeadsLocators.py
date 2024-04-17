from selenium.webdriver.common.by import By

add_new_lead_button = (By.XPATH, "(//button[@type='button'])[2]")
lead_type_button_dropdown = (By.XPATH, "(//input[@id='type'])[2]")
lead_status_dropdown = (By.XPATH, "(//input[@id='status'])[2]")
lead_people_dropdown = (By.XPATH, "(//input[@id='rc_select_190'])[1]")
lead_notes_text_area = (By.XPATH, "(//textarea[@id='notes'])[2]")
lead_submit_button = (By.XPATH, "(//button[@type='submit'])[2]")
lead_source_dropdown = (By.XPATH, "(//input[@id='source'])[2]")
lead_confirmation_pop_up =(By.XPATH, "//body/div/div[@class='ant-drawer ant-drawer-right css-16v3ahg ant-drawer-open']/div[@class='ant-drawer-content-wrapper']/div[@role='dialog']/div[@class='ant-drawer-body']/div[@class='sidePanelContent']/div[@class='collapseBox collapsed']/div[@class='BottomCollapseBox']/div/div[@class='ant-row css-16v3ahg']/div[@class='ant-col ant-col-24 css-16v3ahg']/div[@class='ant-spin-nested-loading css-16v3ahg']/div[@class='ant-spin-container']/form[@class='ant-form ant-form-vertical css-16v3ahg']/div[1]")