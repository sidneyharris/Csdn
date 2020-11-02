from test_csdn.Page.base import Base
from test_csdn.Page.main import Main

class TestLogin:
    def setup(self):
        self.main = Main()

    def test_login(self):
        self.main.goto_Login_Register().account_password().login()
        return True

    def teardown(self):
        pass