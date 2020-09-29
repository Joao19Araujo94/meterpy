import meterpy.testplan
from meterpy.testplan.structure import TestPlan
import unittest

class TestSuite(unittest.TestCase):
    def test_name(self):
        tester = TestPlan("A")
        self.assertEqual(tester.test_name, "A")

    def test_add_element(self):
        tester = TestPlan("A")
        self.assertRaises(TypeError, tester.add_element("A"))

if __name__ == '__main__':
    unittest.main()