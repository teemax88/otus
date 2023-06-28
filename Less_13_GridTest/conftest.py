import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


# def pytest_addoption(parser):
#     parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
#     parser.addoption("--url", "-U", action="store", default="http://localhost/opencart", help="choose your browser")
#
#
# @pytest.fixture
# def url(request):
#     return request.config.getoption("--url")


@pytest.fixture
def browser():
    """ Фикстура инициализации браузера """
    # selenium_grid_url = "http://localhost:4444/wd/hub"
    # cap = DesiredCapabilities.CHROME.copy()

    # driver = webdriver.Remote(desired_capabilities=cap, command_executor=selenium_grid_url)
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.google.com/")

    yield driver

    driver.quit()
