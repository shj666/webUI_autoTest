from ddt import ddt
from ddt import data
from ddt import unpack
import unittest
from 练习.abs import abs
@ddt
class AbsTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start.............")
    @data([1,1],[-1,1],[0,0])
    @unpack
    def test_abs(self,n,expect):
        result = abs(n)
        self.assertEqual(result, expect ,msg=result)
        print(self.assertEqual(result, expect ,msg=result))
    @classmethod
    def tearDown(self):
        print("end...............")
if __name__=='__main__':
    unittest.main(verbosity=2)