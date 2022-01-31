from bmi import *
import unittest


class BMITestCase(unittest.TestCase):
    """Tests for BMI calculation method"""

    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up some stuff for [" + self.shortDescription() + "]")
        print("==========================")

    def tearDown(self):
        """Tear Down Method!"""
        print("==========================")
        print("Cleaning mess after [" + self.shortDescription() + "]")

    def test_normal_evaluation(self):
        """Normal BMI evaluation test"""
        print("test id: " + self.id())
        self.assertEqual(bmi_evaluate(BMI(75, 1.83)),
                         "Normal (healthy weight)")

    def test_normal(self):
        """Normal BMI value test"""
        print("test id: " + self.id())
        self.assertEqual(BMI(75, 1.83).__round__(3),
                         22.395)


if __name__ == '__main__':
    unittest.main()
