from selenium.webdriver.common.by import By


class AccountPage():
    def __init__(self, driver):
        self.driver = driver

    login_successful_msg_link_text = "Edit your account information"


    def login_sccess_message(self):
        return self.driver.find_element(By.LINK_TEXT, self.login_successful_msg_link_text).is_displayed()

