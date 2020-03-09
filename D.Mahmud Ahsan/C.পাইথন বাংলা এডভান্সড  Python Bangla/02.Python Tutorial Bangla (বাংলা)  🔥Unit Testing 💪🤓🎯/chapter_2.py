#-------------------------------------
#        Unit Test
#-----------------------------------

import unittest
from mspack import msmath
from mspack import msstring

class MsPackMsMathTestCase(unittest.testCase):
    def test_sum(self):
        sum = msmath.sum(8, 12)
        self.assertEqual(sum, 20)

if __name__ == '__main__':
    unittest.main()
