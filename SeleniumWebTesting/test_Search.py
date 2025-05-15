import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_search_a_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_a_product_in_search_box("HP")
        home_page.click_search_button()
        search_result = SearchPage(self.driver)
        assert search_result.display_status_of_hp_product()

    def test_search_an_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_a_product_in_search_box("Honda")
        home_page.click_search_button()
        expected_text = "There is no product that matches the search criteria."
        search_result = SearchPage(self.driver)
        assert search_result.display_status_of_invalid_product().__eq__(expected_text)

    def test_search_without_any_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_a_product_in_search_box("")
        home_page.click_search_button()
        expected_text = "There is no product that matches the search criteria."
        search_result = SearchPage(self.driver)
        assert search_result.display_status_of_invalid_product().__eq__(expected_text)
