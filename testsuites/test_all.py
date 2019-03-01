
import time
import unittest
import HTMLTestRunner
from testsuites.test_Discuz_login import DiscuzLogin
from testsuites.test_Discuz_admin import DiscuzAdmin
from testsuites.test_Discuz_user import DiscuzUser
from testsuites.test_Discuz_toupiao import DiscuzToupiao
import os

cur_path = os.path.dirname(os.path.relpath(__file__))
report_path = os.path.join(cur_path,"report")
if not  os.path.exists(report_path):os.mkdir(report_path)


suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite(DiscuzLogin))
suit.addTest(unittest.makeSuite(DiscuzAdmin))
suit.addTest(unittest.makeSuite(DiscuzUser))
suit.addTest(unittest.makeSuite(DiscuzToupiao))





if __name__=='__main__':
    html_report = report_path + r"\result.html"
    fp=open(html_report,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试",description="测试用例执行")
    runner.run(suit)

