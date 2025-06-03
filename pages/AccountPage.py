from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    login_successful_msg_link_text = "Edit your account information"


    def login_sccess_message(self):
        return self.check_display_status("login_successful_msg_link_text",self.login_successful_msg_link_text)

