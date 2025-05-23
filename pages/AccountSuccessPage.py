from selenium.webdriver.common.by import By


class AccountSuccessPage():
    def __init__(self, driver):
        self.driver = driver

    register_success_message_xpath = "//div[@id='content']/h1"

    def register_success_message_displayed(self):
        return self.driver.find_element(By.XPATH, self.register_success_message_xpath).is_displayed()

