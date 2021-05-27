import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def test_email(self):
        emp_1 = Employee('Brian', 'Moo', 50000)
        emp_2 = Employee('Brianna', 'Smith', 60000)
        
        self.assertEqual(emp_1.email, 'Brian.Moo@email.com')
        self.assertEqual(emp_2.email, 'Brianna.Smith@email.com')
        
        emp_1.first ='Jimmy'
        emp_2.first = "Janey"
        
        self.assertEqual(emp_1.email, 'Jimmy.Moo@email.com')
        self.assertEqual(emp_2.email, 'Janey.Smith@email.com')
        
    def test_fullname(self):
        emp_1 = Employee('Brian', 'Moo', 60000)
        emp_2 = Employee('Jess', 'Alc', 50000)
        
        self.assertEqual(emp_1.fullname, 'Brian Moo')
        self.assertEqual(emp_2.fullname, 'Jess Alc')
        
        emp_1.first = 'Bee'
        emp_2.first = 'Jetsa'
        
        self.assertEqual(emp_1.fullname,'Bee Moo')
        self.assertEqual(emp_2.fullname, 'Jetsa Alc')
        
    def test_apply_raise(self):
        emp_1 = Employee('Brian', 'Moo', 50000)
        emp_2 = Employee('Brianna', 'Smith', 60000)
        emp_1.apply_raise()
        emp_2.apply_raise()
        
        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)
        
if __name__ == '__main__':
    unittest.main()