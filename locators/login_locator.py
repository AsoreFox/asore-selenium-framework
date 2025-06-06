from selenium.webdriver.common.by import By

class LoginLocators:
    usernameInput = (By.ID, "username")
    passwordInput = (By.ID, "password")
    loginButton = (By.ID, "submit")
    errorMessage = (By.ID, "error")