from selenium.webdriver.common.by import By

from test_csdn.Page.base import Base
from test_csdn.Page.registerlogin import RegisterLoginPage
from test_csdn.Page.search import Search


class Main(Base):
    _url = "https://www.csdn.net"

    def goto_Login_Register(self):
        self.find(By.XPATH, '//div[@class="toolbar-btn-login csdn-toolbar-fl "]').click()
        return RegisterLoginPage(self._driver)

    def search(self):
        self.find(By.ID,'toolbar-search-input').click()
        return Search(self._driver)
