from selenium.webdriver.common.by import By

class BasePageLocators:
    base_page_logo = (By.CLASS_NAME, "logo pull-left")
    home_page_header_button = (By.XPATH, "//*[@href= '/' and contains(text(),'Home')]")
    products_page_header_button = (By.XPATH, "//*[@href= '/products' ]")
    cart_page_header_button = (By.XPATH, "//*[@href= '/view_cart']")
    login_singup_page_header_button = (By.XPATH, "//*[@href= '/login']")
    logout_header_button = (By.XPATH, "//*[@href= '/logout']")
    delete_account_header_button = (By.XPATH, "//*[@href= '/delete_account']")
    user_logged_in_name = (By.XPATH, "//*[contains(text(), 'TestUser')]")