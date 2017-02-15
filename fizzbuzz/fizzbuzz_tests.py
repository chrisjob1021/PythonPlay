import unittest
from fizzbuzz import fizzbuzz

class FizzbuzzTestCase(unittest.TestCase):

    def test_divide_by_three(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(33), 'Fizz')
        self.assertEqual(fizzbuzz(99), 'Fizz')

    def test_divide_by_five(self):
        self.assertEqual(fizzbuzz(5), 'buzz')
        self.assertEqual(fizzbuzz(50), 'buzz')
        self.assertEqual(fizzbuzz(500), 'buzz')

    def test_empty_string(self):
        self.assertEqual(fizzbuzz(4), '')
        self.assertEqual(fizzbuzz(11), '')
        self.assertEqual(fizzbuzz(22), '')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'Fizzbuzz')
