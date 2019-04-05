import unittest
import io, sys
from planets import *

class Test_planets(unittest.TestCase):

    def test_01(self):
        sys.stdin = io.StringIO("136")
        sys.stdout = student_output = io.StringIO()        
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 51.68 pounds.\nOn Jupiter you would weigh 318.24 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_02(self):
        sys.stdin = io.StringIO("105")
        sys.stdout = student_output = io.StringIO()        
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 39.9 pounds.\nOn Jupiter you would weigh 245.7 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())
 
    def test_03(self):
        sys.stdin = io.StringIO("600")
        sys.stdout = student_output = io.StringIO()        
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 228.0 pounds.\nOn Jupiter you would weigh 1404.0 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())  

    def test_04(self):
        sys.stdin = io.StringIO("45.5")
        sys.stdout = student_output = io.StringIO()        
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 17.29 pounds.\nOn Jupiter you would weigh 106.47 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())  



if __name__ == "__main__":
        unittest.main()
