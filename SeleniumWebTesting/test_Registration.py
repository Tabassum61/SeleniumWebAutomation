from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegistration:

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        home_page.click_register_button()
        register_page = RegisterPage(self.driver)
        register_page.give_first_name_input("Moti11")
        register_page.give_last_name_input("bhai")
        register_page.give_email_input(self.generate_email_with_time_stamp())
        register_page.give_telephone_input("123456")
        register_page.give_password_input("12345")
        register_page.give_confirm_password_input("12345")
        register_page.click_agree_button()
        register_page.click_continue_button()
        expected_text = "Your Account Has Been Created!"
        register_success = AccountSuccessPage(self.driver)
        assert register_success.register_success_message_displayed().__eq__(expected_text)


    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        home_page.click_register_button()
        register_page = RegisterPage(self.driver)
        register_page.give_first_name_input("Moti11")
        register_page.give_last_name_input("bhai")
        register_page.give_email_input(self.generate_email_with_time_stamp())
        register_page.give_telephone_input("123456")
        register_page.give_password_input("12345")
        register_page.give_confirm_password_input("12345")
        register_page.click_newsletter_subscribe_button() #extra check
        register_page.click_agree_button()
        register_page.click_continue_button()

        expected_text = "Your Account Has Been Created!"
        register_success = AccountSuccessPage(self.driver)
        assert register_success.register_success_message_displayed().__eq__(expected_text)

    def test_register_with_same_emailid(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        home_page.click_register_button()
        register_page = RegisterPage(self.driver)
        register_page.give_first_name_input("Moti11")
        register_page.give_last_name_input("bhai")
        register_page.give_email_input("ocean@gmail.com")
        register_page.give_telephone_input("123456")
        register_page.give_password_input("12345")
        register_page.give_confirm_password_input("12345")
        register_page.click_agree_button()
        register_page.click_continue_button()
        expected_text = "Warning: E-Mail Address is already registered!"
        assert register_page.display_email_warning_message().__eq__(expected_text)

    def test_register_without_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        home_page.click_register_button()
        register_page = RegisterPage(self.driver)
        register_page.give_first_name_input("")
        register_page.give_last_name_input("")
        register_page.give_email_input("")
        register_page.give_telephone_input("")
        register_page.give_password_input("")
        register_page.give_confirm_password_input("")
        register_page.click_agree_button()
        register_page.click_continue_button()

        expected_privacy_warning = "Warning: You must agree to the Privacy Policy!"
        assert register_page.display_privacy_policy_warning_message().__eq__(expected_privacy_warning)

        expected_firstname_warning = "First Name must be between 1 and 32 characters!"
        assert register_page.display_first_name_warning_message().__eq__(expected_firstname_warning)

        expected_lastname_warning = "Last Name must be between 1 and 32 characters!"
        assert register_page.display_last_name_warning_message().__eq__(expected_lastname_warning)


    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        return "motibhai"+time_stamp+"@gmail.com"