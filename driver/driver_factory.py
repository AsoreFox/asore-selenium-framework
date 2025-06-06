from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
class DriverFactory:
    def __init__(self, browser= "chrome", headless = True ):
        self.browser = browser.lower()
        self.headless = headless

    def create_driver(self):
        if self.browser == "chrome":
            return webdriver.Chrome(options = self._set_options(ChromeOptions()))
        elif self.browser == "firefox":
            return webdriver.Firefox(options = self._set_options(FirefoxOptions()))
        elif self.browser == "edge":
            return webdriver.Edge(options = self._set_options(EdgeOptions()))
        else:
            raise ValueError(f"Unsupported Browser: {self.browser}")
    
    def _set_options(self, browserOptions):
        options = browserOptions
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument('--start-maximized')
        return options