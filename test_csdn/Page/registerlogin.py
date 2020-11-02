from time import sleep

from selenium.webdriver.common.by import By

from test_csdn.Page.base import Base
from test_csdn.Page.csdnscan import CsdnScan
from test_csdn.Page.login import AccountLoginPage
from test_csdn.Page.phonelogin import PhoneLogin
from test_csdn.Page.wechatscan import WeChatScan


class RegisterLoginPage(Base):
    def account_password(self):
        self.find(By.XPATH,'//div[@class="main-select"]/ul/li[2]').click()
        return AccountLoginPage(self._driver)

    def csdn_app_scan(self):
        self.find(By.XPATH,'//div[@class="main-select"]/ul/li[1]').click()
        sleep(5)
        return CsdnScan(self._driver)

    def wechat_app_scan(self):
        self.find(By.XPATH,'//div[@class="main-select"]/ul/li[3]').click()
        sleep(5)
        return WeChatScan(self._driver)

    def phone_nopasswd_login(self):
        self.find(By.XPATH,'//div[@class="main-select"]/ul/li[3]').click()

        return PhoneLogin(self._driver)
