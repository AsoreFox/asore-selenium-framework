from selenium.webdriver.common.by import By

class HomePageLocators:
    homePageLogo = (By.XPATH, "//*[@href="'/'" and contains(text(), 'Home')]")
    homePageTitle= (By.XPATH, "//*[@href= "'/'" and contains(text(),'Home')]")
    homePageText = (By.XPATH, "//*[@class = 'col-sm-6'][1]")
    homePageImage = (By.XPATH,"//*[@class='girl img-responsive']")