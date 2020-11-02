from selenium.webdriver.common.by import By

from test_csdn.Page.base import Base

class Search(Base):
    # send_value = "python自动化面试题"
    def seach_csdn(self):
        self.find(By.ID,'toolbar-search-input').send_keys("python自动化面试题")
        self.find(By.ID,'toolbar-search-button').click()
        return True