import pytest
from selenium import webdriver
from Utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    driver = None
    browser = ReadConfigurations.read_configurations("basic info","browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("safari"):
        driver = webdriver.Safari()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("opera"):
        driver = webdriver.Opera()
    else:
        print("Unsupported browser")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configurations("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
