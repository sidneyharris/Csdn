from test_csdn.Page.main import Main


class TestSearch:
    def setup(self):
        self.main = Main()

    def test_search(self):
        self.main.search().seach_csdn()
        return True

    def teardown(self):
        pass