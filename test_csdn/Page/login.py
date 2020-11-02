from selenium.webdriver.common.by import By
from test_csdn.Page.base import Base

class AccountLoginPage(Base):
    def login(self):
        self.find(By.ID,'tabOne').click()
        self.find(By.ID,'all').send_keys("test")
        self.find(By.ID, "password-number").send_keys("234124")
        self.find(By.XPATH,'//div[@class="form-group"]//button').click()
        return True