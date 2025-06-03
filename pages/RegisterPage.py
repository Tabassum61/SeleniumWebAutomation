from selenium.webdriver.common.by import By
from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    first_name_input_id = "input-firstname"
    last_name_input_id = "input-lastname"
    email_input_id = "input-email"
    telephone_input_id = "input-telephone"
    password_input_id = "input-password"
    confirm_password_input_id = "input-confirm"
    agree_button_name = "agree"
    click_continue_button_xpath = "//input[@value='Continue']"
    newsletter_subscribe_link_xpath = "//input[@name='newsletter'][@value='1']"
    email_warning_message_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_message_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_message_xpath = "//input[@id='input-firstname']"
    last_name_warning_message_xpath = "//input[@id='input-lastname']"


    def give_first_name_input(self,first_name):
        self.type_into_element(first_name,"first_name_input_id",self.first_name_input_id)

    def give_last_name_input(self,last_name):
        self.type_into_element(last_name,"last_name_input_id",self.last_name_input_id)


    def give_email_input(self,email):
        self.type_into_element(email,"email_input_id",self.email_input_id)


    def give_telephone_input(self,telephone):
        self.type_into_element(telephone,"telephone_input_id",self.telephone_input_id)


    def give_password_input(self,password):
        self.type_into_element(password,"password_input_id",self.password_input_id)


    def give_confirm_password_input(self,confirm_password):
        self.type_into_element(confirm_password,"confirm_password_input_id",self.confirm_password_input_id)

    def register_with_mandatory_fields(self,first_name,last_name,email,telephone,password,confirm_password,yes_no,privacy_policy):
        self.give_first_name_input(first_name)
        self.give_last_name_input(last_name)
        self.give_email_input(email)
        self.give_telephone_input(telephone)
        self.give_password_input(password)
        self.give_confirm_password_input(confirm_password)
        if yes_no.__eq__("yes"):
            self.click_newsletter_subscribe_button()
        if privacy_policy.__eq__("select"):
            self.click_agree_button()
        return self.click_continue_button()

    def click_newsletter_subscribe_button(self):
        self.click_element("newsletter_subscribe_link_xpath", self.newsletter_subscribe_link_xpath)


    def click_agree_button(self):
        self.click_element("agree_button_name",self.agree_button_name)


    def click_continue_button(self):
        self.click_element("click_continue_button_xpath",self.click_continue_button_xpath)
        return AccountSuccessPage(self.driver)

#warning for invalid input
    def display_email_warning_message(self):
        return self.check_display_status("email_warning_message_xpath",self.email_warning_message_xpath)


    def display_first_name_warning_message(self):
        return self.check_display_status("first_name_warning_message_xpath",self.first_name_warning_message_xpath)


    def display_last_name_warning_message(self):
        return self.check_display_status("last_name_warning_message_xpath",self.last_name_warning_message_xpath)


    def display_privacy_policy_warning_message(self):
        return self.check_display_status("privacy_policy_warning_message_xpath",self.privacy_policy_warning_message_xpath)


    def varify_all_warning(self,expected_privacy_warning,expected_firstname_warning,expected_lastname_warning):
        actual_privacy_warning = self.display_privacy_policy_warning_message()
        actual_firstname_warning =  self.display_first_name_warning_message()
        actual_lastname_warning = self.display_last_name_warning_message()

        status = False
        if actual_privacy_warning.__eq__(expected_privacy_warning):
            if actual_firstname_warning.__eq__(expected_firstname_warning):
                if actual_lastname_warning.__eq__(expected_lastname_warning):
                    status = True

        return status


