from selenium.webdriver.common.by import By

class BasePageLocators:
    basePageLogo = (By.CLASS_NAME, "logo pull-left")
    homePageTitle = (By.XPATH, "//*[@href= '/' and contains(text(),'Home')]")
    productsPageTitle = (By.XPATH, "//*[@href= '/products' ]")
    cartPageTitle = (By.XPATH, "//*[@href= '/view_cart']")
    loginSignupPageTitle = (By.XPATH, "//*[@href= '/login']")