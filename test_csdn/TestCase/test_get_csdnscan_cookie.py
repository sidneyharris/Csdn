import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_csdn.Page.main import Main

class TestGetCsdnScan:
    def setup(self):
        self.main = Main()

    def test_scdn_cookie(self):
        cookies = json.load(open('csdncookies.json'))
        for cookie in cookies:

            self.main._driver.add_cookie(cookie)

        while True:
            # self.main._driver.refresh()
            #显示等待
            res = WebDriverWait(self.main._driver,20). \
            until(expected_conditions.element_to_be_clickable((By.XPATH,'//div[@class="index_nav_left"]/ul/li[1]/a')))
            if res is not None:
                break

        self.main.goto_Login_Register().csdn_app_scan().get_csdn_scan()

    def teardown(self):
        self.main._driver.close()