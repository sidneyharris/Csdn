from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class Base:
    _url = ""

    def __init__(self,driver:WebDriver = None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        if self._url != "":
            self._driver.get(self._url)
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()

    def find(self, by, locator):#封装一个find方法
        return self._driver.find_element(by,locator)