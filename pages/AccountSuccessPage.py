from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AccountSuccessPage:
    def __init__(self, driver):
        self.driver = driver

    register_success_message_xpath = "//div[@id='content']/h1"

    def register_success_message_displayed(self):
        wait=WebDriverWait(self.driver, 30)
        return wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.register_success_message_xpath))).is_displayed()


