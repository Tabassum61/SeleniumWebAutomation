from selenium.webdriver.common.by import By
from pages.AccountSuccessPage import AccountSuccessPage


class RegisterPage:
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
    email_warning_message_x_path = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_message_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_message_xpath = "//input[@id='input-firstname']"
    last_name_warning_message_xpath = "//input[@id='input-lastname']"


    def give_first_name_input(self,first_name):
        self.driver.find_element(By.ID, self.first_name_input_id).send_keys(first_name)

    def give_last_name_input(self,last_name):
        self.driver.find_element(By.ID, self.last_name_input_id).send_keys(last_name)

    def give_email_input(self,email):
        self.driver.find_element(By.ID, self.email_input_id).send_keys(email)

    def give_telephone_input(self,telephone):
        self.driver.find_element(By.ID, self.telephone_input_id).send_keys(telephone)

    def give_password_input(self,password):
        self.driver.find_element(By.ID, self.password_input_id).send_keys(password)

    def give_confirm_password_input(self,confirm_password):
        self.driver.find_element(By.ID, self.confirm_password_input_id).send_keys(confirm_password)

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
        self.driver.find_element(By.XPATH, self.newsletter_subscribe_link_xpath).click()

    def click_agree_button(self):
        self.driver.find_element(By.NAME, self.agree_button_name).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.click_continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

#warning for invalid input
    def display_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.email_warning_message_x_path).is_displayed()

    def display_first_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.first_name_warning_message_xpath).is_displayed()

    def display_last_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.last_name_warning_message_xpath).is_displayed()

    def display_privacy_policy_warning_message(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_warning_message_xpath).is_displayed()

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


