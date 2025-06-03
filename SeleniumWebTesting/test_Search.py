import time

import pytest
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_search_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_result = home_page.search_for_a_product("HP")
        assert search_result.display_status_of_hp_product()

    def test_search_an_invalid_product(self):
        home_page = HomePage(self.driver)
        search_result = home_page.search_for_a_product("Honda")
        expected_text = "There is no product that matches the search criteria."
        time.sleep(3)
        assert search_result.display_status_of_invalid_product().__eq__(expected_text)

    def test_search_without_any_valid_product(self):
        home_page = HomePage(self.driver)
        search_result = home_page.search_for_a_product("")
        expected_text = "There is no product that matches the search criteria."
        time.sleep(3)
        assert search_result.display_status_of_invalid_product().__eq__(expected_text)
