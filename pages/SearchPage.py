from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_link_text = "HP LP3065"
    invalid_product_search_xpath= "//input[@id='button-search']/following-sibling::p"

    def display_status_of_hp_product(self):
        return self.check_display_status("valid_hp_product_link_text",self.valid_hp_product_link_text)

    def display_status_of_invalid_product(self):
        return self.check_display_status("invalid_product_search_xpath",self.invalid_product_search_xpath)
