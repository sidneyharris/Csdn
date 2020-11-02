from selenium.webdriver.common.by import By

from test_csdn.Page.base import Base


class PhoneLogin(Base):
    def phone_login(self):
        # 切换到手机免密登录窗口
        self.find(By.ID, 'tabTwo').click()
        self.find(By.ID, "phone").send_keys("13696056340")
        self.find(By.XPATH, '//div[@class="col-xs-12 col-sm-12 control-col-pos col-pr-no col-pl-no"]/button').click()
        return True
