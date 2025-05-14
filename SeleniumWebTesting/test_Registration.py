from datetime import datetime
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
class TestRegistration:

    def test_register_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Moti")
        self.driver.find_element(By.ID, "input-lastname").send_keys("bhai")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("123467")
        self.driver.find_element(By.ID, "input-password").send_keys("1234")
        self.driver.find_element(By.ID, "input-confirm").send_keys("1234")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)


    def test_register_with_all_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Moti")
        self.driver.find_element(By.ID, "input-lastname").send_keys("bhai")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("123467")
        self.driver.find_element(By.ID, "input-password").send_keys("1234")
        self.driver.find_element(By.ID, "input-confirm").send_keys("1234")
        self.driver.find_elements(By.XPATH, "//input[@name='newsletter'][@value='1']").clear()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)


    def test_register_with_same_emailid(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Ocean")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Eleven")
        self.driver.find_element(By.ID, "input-email").send_keys("ocean@gmail.com")
        self.driver.find_element(By.ID, "input-telephone").send_keys("123467")
        self.driver.find_element(By.ID, "input-password").send_keys("1234")
        self.driver.find_element(By.ID, "input-confirm").send_keys("1234")
        self.driver.find_elements(By.XPATH, "//input[@name='newsletter'][@value='1']").clear()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_text = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(expected_text)

    def test_register_without_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("")
        self.driver.find_element(By.ID, "input-lastname").send_keys("")
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-telephone").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.ID, "input-confirm").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()

        expected_privacy = "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(expected_privacy)

        expected_firstname_warning = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH,"//input[@id='input-firstname']/following-sibling::div").text.__contains__(expected_firstname_warning)

        expected_lasttname_warning = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__contains__(
            expected_lasttname_warning)


    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        return "motibhai"+time_stamp+"@gmail.com"