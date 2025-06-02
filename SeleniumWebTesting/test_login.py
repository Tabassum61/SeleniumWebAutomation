from datetime import datetime
import pytest
from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:


    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page =login_page.login_with_credentials("ocean@gmail.com","12345")
        assert account_page.login_sccess_message()

    def test_login_with_invalid_email_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials(self.generate_email_with_time_stamp(),"12345")
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.unsuccessful_login_warning_message().__eq__(expected_text)


    def test_login_with_valid_email_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials("ocean111@gmail.com", "12345")
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.unsuccessful_login_warning_message().__eq__(expected_text)


    def test_login_without_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials("", "")
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.unsuccessful_login_warning_message().__eq__(expected_text)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        return "ocean"+time_stamp+"@gmail.com"
