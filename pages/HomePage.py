from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search_box_field_name=  "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_button_link_text = "Login"
    register_button_link_text = "Register"


    def enter_a_product_in_search_box(self,product_name):
        self.driver.find_element(By.NAME,self.search_box_field_name).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def click_my_account_drop_menu(self):
        self.driver.find_element(By.XPATH, self.my_account_drop_menu_xpath).click()

    def click_login_button(self):
        self.driver.find_element(By.LINK_TEXT, self.login_button_link_text).click()

    def click_register_button(self):
        self.driver.find_element(By.LINK_TEXT, self.register_button_link_text).click()
