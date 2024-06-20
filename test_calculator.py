import unittest
from calculator import multiply
import xmlrunner
import os

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(2.5, 4), 10)

if __name__ == "__main__":
    # Ensure the test-results directory exists
    if not os.path.exists('test-results'):
        os.makedirs('test-results')

    with open('test-results/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))
