from selenium.webdriver.common.by import By

avatar_icon_locator = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/span[1]")
email_element_locator = (By.XPATH, "//p[normalize-space()='abdiasalpire12@gmail.com']")
logo_image_locator = (By.XPATH, "//img[@alt='Logo']")
people_tab_locator = (By.XPATH, "//a[normalize-space()='Peoples']")
companies_tab_locator = (By.XPATH, "//a[normalize-space()='Companies']")
leads_tab_locator = (By.XPATH, "//a[normalize-space()='Leads']")
product_category_tab_locator = (By.XPATH, "//a[normalize-space()='Products Category']")
expenses_category_tab_locator = (By.XPATH, "//a[normalize-space()='Expenses Category']")
customer_category_tab_locator = (By.XPATH, "//a[normalize-space()='Customers']")