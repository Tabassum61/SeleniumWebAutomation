from selenium.webdriver.common.by import By
from pages.AccountPage import AccountPage
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    email_id_input_id= "input-email"
    password_input_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def unsuccessful_login_warning_message(self):
        self.check_display_status("warning_message_xpath",self.warning_message_xpath)


    def give_email_input(self, email):
        self.type_into_element(email,"email_id_input_id",self.email_id_input_id)


    def give_password_input(self, password):
        self.type_into_element(password,"password_input_id",self.password_input_id)


    def click_login_button(self):
        self.click_element("login_button_xpath",self.login_button_xpath)
        return AccountPage(self.driver)

    def login_with_credentials(self,email,password):
        self.give_email_input(email)
        self.give_password_input(password)
        return self.click_login_button()




