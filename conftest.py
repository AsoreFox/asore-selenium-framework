import pytest
from driver.driver_factory import DriverFactory

def pytest_addoption(parser):
    parser.addoption("--headless", action = "store_true", default = False)
    parser.addoption("--browser", action= "store", default = "chrome", help = "Browser to use: Chrome, Firefox or Edge")

@pytest.fixture
def driver(request):
    headless = request.config.getoption("--headless")
    browser = request.config.getoption("--browser")
    factory = DriverFactory(browser = browser, headless = headless)
    driver = factory.create_driver()
    yield driver
    driver.quit()
