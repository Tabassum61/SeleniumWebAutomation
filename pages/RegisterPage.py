from selenium.webdriver.common.by import By


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

    def click_agree_button(self):
        self.driver.find_element(By.NAME, self.agree_button_name).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.click_continue_button_xpath).click()

    def click_newsletter_subscribe_button(self):
        self.driver.find_element(By.XPATH, self.newsletter_subscribe_link_xpath).click()

    def display_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.email_warning_message_x_path).is_displayed()

    def display_first_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.first_name_warning_message_xpath).is_displayed()

    def display_last_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.last_name_warning_message_xpath).is_displayed()

    def display_privacy_policy_warning_message(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_warning_message_xpath).is_displayed()

