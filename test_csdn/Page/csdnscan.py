import json
from test_csdn.Page.base import Base


class CsdnScan(Base):
    def get_csdn_scan(self):
        cookies = self._driver.get_cookies()
        '''w:打开一个文件用于写入，如果没有该文件，创建新文件
            r:以只读方式打开文件，文件指针放在文件开头。这是默认的模式
        '''
        with open("csdncookies.json", "w") as f:
            json.dump(cookies, f)
        return cookies



