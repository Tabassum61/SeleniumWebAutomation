from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name =  "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_button_link_text = "Login"
    register_button_link_text = "Register"


    def enter_a_product_in_search_box(self,product_name):
        self.type_into_element(product_name,"search_box_field_name",self.search_box_field_name)


    def click_search_button(self):
        self.click_element("search_button_xpath",self.search_button_xpath)
        return SearchPage(self.driver)

    def click_my_account_drop_menu(self):
        self.click_element("my_account_drop_menu_xpath",self.my_account_drop_menu_xpath)


    def click_login_button(self):
        self.click_element("login_button_link_text",self.login_button_link_text)
        return LoginPage(self.driver)

    def navigate_to_login_page(self):
        self.click_my_account_drop_menu()
        return self.click_login_button()

    def click_register_button(self):
        self.click_element("register_button_link_text",self.register_button_link_text)
        return RegisterPage(self.driver)

    def navigate_to_register_page(self):
        self.click_my_account_drop_menu()
        return self.click_register_button()

    def search_for_a_product(self, product_name):
        self.enter_a_product_in_search_box(product_name)
        return self.click_search_button()



