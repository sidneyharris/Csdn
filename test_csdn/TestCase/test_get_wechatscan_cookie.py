import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_csdn.Page.main import Main

class TestWechatScan:
    def setup(self):
        self.main = Main()

    def test_wechatscan_cookie(self):
        self.main.goto_Login_Register().wechat_app_scan().get_wechat_scan()

        cookies = json.load(open('wechatscan.json'))
        for cookie in cookies:

            self.main._driver.add_cookie(cookie)

        while True:
            # self.main._driver.refresh()
            #显示等待
            res = WebDriverWait(self.main._driver,20). \
            until(expected_conditions.element_to_be_clickable((By.XPATH,'//div[@class="index_nav_left"]/ul/li[1]/a')))
            if res is not None:
                break