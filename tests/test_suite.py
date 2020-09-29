import meterpy
from meterpy.testplan import TestPlan
import unittest

class TestSuite(unittest.TestCase):
    def test_name(self):
        tester = TestPlan("A")
        self.assertEqual(tester.test_name, "A")

if __name__ == '__main__':
    unittest.main()