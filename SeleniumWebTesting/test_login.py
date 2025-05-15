from _datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        home_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.give_email_input("ocean@gmail.com")
        login_page.give_password_input("12345")
        login_page.click_login_button()
        account_page = AccountPage(self.driver)
        assert account_page.login_sccess_message()

    def test_login_with_Invalid_email_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        home_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.give_email_input(self.generate_email_with_time_stamp())
        login_page.give_password_input("12345")
        login_page.click_login_button()
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.unsuccessful_login_warning_message().__eq__(expected_text)


    def test_login_with_valid_email_Invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        home_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.give_email_input("ocean111@gmail.com")
        login_page.give_password_input("12345")
        login_page.click_login_button()
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.unsuccessful_login_warning_message().__eq__(expected_text)


    def test_login_without_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        home_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.give_email_input("")
        login_page.give_password_input("")
        login_page.click_login_button()
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.unsuccessful_login_warning_message().__eq__(expected_text)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        return "ocean"+time_stamp+"@gmail.com"
