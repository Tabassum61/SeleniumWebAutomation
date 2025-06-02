from datetime import datetime
import pytest
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegistration:

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success = register_page.register_with_mandatory_fields("Moti11","bhai",self.generate_email_with_time_stamp(),"123456","12345","12345","no","select")
        expected_text = "Your Account Has Been Created!"
        assert account_success.register_success_message_displayed().__eq__(expected_text)


    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success = register_page.register_with_mandatory_fields("Moti11", "bhai",
                                                                       self.generate_email_with_time_stamp(), "123456",
                                                                       "12345", "12345", "yes", "select")
        expected_text = "Your Account Has Been Created!"
        assert account_success.register_success_message_displayed().__eq__(expected_text)

    def test_register_with_same_emailid(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_with_mandatory_fields("Moti11", "bhai",
                                                                       "ocean@gmail.com", "123456",
                                                                       "12345", "12345", "no", "select")
        expected_text = "Warning: E-Mail Address is already registered!"
        assert register_page.display_email_warning_message().__eq__(expected_text)

    def test_register_without_credentials(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_with_mandatory_fields("","","","","","","no","no")
        assert register_page.varify_all_warning("Warning: You must agree to the Privacy Policy!","First Name must be between 1 and 32 characters!","Last Name must be between 1 and 32 characters!")


    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        return "motibhai"+time_stamp+"@gmail.com"