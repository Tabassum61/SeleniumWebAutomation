import pytest
from selenium import webdriver

@pytest.fixture()
def setup_teardown(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver

    yield
    driver.quit()
