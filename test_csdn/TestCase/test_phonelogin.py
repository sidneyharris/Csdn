from test_csdn.Page.main import Main

class TestPhoneLogin:
    def setup(self):
        self.main = Main()

    def test_phonelogin(self):
        self.main.goto_Login_Register().phone_nopasswd_login().phone_login()
        return True

    def teardown(self):
        pass