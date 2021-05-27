#using unit test to test calc functions
#add, sub multiply and divide whole numbers decimals and negatives
import unittest
import calc

#inherit from testcase to access test case functions
class TestCalc(unittest.TestCase):
    def test_add(self):
        #assert equal to test if calc is getting proper return value
        self.assertEqual(calc.add(10, 10), 20)
        self.assertEqual(calc.add(22, 3), 25)
        self.assertEqual(calc.add(1024, 8), 1032)
        self.assertEqual(calc.add(-10, 20),10)
        self.assertEqual(calc.add(.01, 3.14), 3.15)
        self.assertEqual(calc.add(-.1, 3.14), 3.04)
    def test_sub(self):        
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(11,6), 5)
        self.assertEqual(calc.subtract(12,7), 5)
        self.assertEqual(calc.subtract(-32, 10), -42)
        self.assertEqual(calc.subtract(.1, 1), -.9)
        self.assertEqual(calc.subtract(-.1, 1), -1.1)
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5),50)
        self.assertEqual(calc.multiply(11, 10), 110)
        self.assertEqual(calc.multiply(512, 2), 1024)
        self.assertEqual(calc.multiply(.5, 2), 1)
        self.assertEqual(calc.multiply(-.5, 2), -1)
    def test_div(self):
        self.assertEqual(calc.divide(20, 1), 20)
        self.assertEqual(calc.divide(64, 8), 8)
        self.assertEqual(calc.divide(2048, 4), 512)
        self.assertEqual(calc.divide(.5, 2), .25)
        self.assertEqual(calc.divide(-.5, 2), -.25)
        
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
        
        
        
if __name__ == '__main__':
    unittest.main()