from ddt import ddt,data,unpack
from 练习.sort import sort
import unittest
@ddt
class SortTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start.......")
    @data([0,0,0],[1,0,2],[1,1,10],[1,2,20])
    @unpack
    def test_sort(self,x,y,expect):
         result = sort(x,y)
         self.assertEqual(result, expect, msg = result)
         print(self.assertEqual(result, expect, msg = result))
    #@classmethod
    def tearDown(self):
        print("end.........")
if __name__=='__main__':
    unittest.main(verbosity=2)