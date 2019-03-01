import os
from 练习.abs_test import AbsTestCase
from 练习.sort_test import SortTestCase
import unittest
import HTMLTestRunner
cur_path = os.path.dirname(os.path.relpath(__file__))
report_path = os.path.join(cur_path,"report")
if not  os.path.exists(report_path):os.mkdir(report_path)


suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite(AbsTestCase))
suit.addTest(unittest.makeSuite(SortTestCase))

if __name__=='__main__':
    html_report = report_path + r"\result.html"
    fp=open(html_report,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试",description="测试用例执行")
    runner.run(suit)