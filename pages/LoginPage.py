from selenium.webdriver.common.by import By
from pages.AccountPage import AccountPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email_id_input_ID= "input-email"
    password_input_ID = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_x_path = "//div[@id='account-login']/div[1]"

    def unsuccessful_login_warning_message(self):
        return self.driver.find_element(By.XPATH, self.warning_message_x_path).is_displayed()

    def give_email_input(self, email):
        self.driver.find_element(By.ID, self.email_id_input_ID).send_keys(email)

    def give_password_input(self, password):
        self.driver.find_element(By.ID, self.password_input_ID).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return AccountPage(self.driver)

    def login_with_credentials(self,email,password):
        self.give_email_input(email)
        self.give_password_input(password)
        return self.click_login_button()




