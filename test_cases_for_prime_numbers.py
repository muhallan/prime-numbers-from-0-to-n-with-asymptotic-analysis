"""Unit tests for the prime_numbers function."""

import unittest
from prime_numbers import prime_numbers

class TestPrimeNumbersGenerated(unittest.TestCase):
    """Function to generate test cases for the prime_numbers function"""

    def test_prime_numbers(self):
        """Testing if prime numbers are correctly generated."""
        self.assertEqual(prime_numbers(14), [2, 3, 5, 7, 11, 13])

    def test_ten(self):
        """Testing if prime numbers are correctly generated."""
        self.assertEqual(prime_numbers(10), [2, 3, 5, 7])

    def test_one_hundred(self):
        """Testing if prime numbers are correctly generated."""
        self.assertEqual(prime_numbers(100),
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_one_hundred_thirty_three(self):
        """Testing if prime numbers are correctly generated."""
        self.assertEqual(prime_numbers(133), 
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131])


    def test_zero(self):
        """Testing if zero is correctly determined not to be prime."""
        self.assertEqual(prime_numbers(0), "Zero or One cannot be prime numbers.")

    def test_one(self):
        """"Testing if one is correctly determined not to be a prime number."""
        self.assertEqual(prime_numbers(1), "Zero or One cannot be prime numbers.")

    def test_two(self):
        """Testing if error is returned if integer entered is 2."""
        self.assertEqual(prime_numbers(2), [2])

    def test_invalid_type_is_string(self):
        """Testing if error is returned if input is not integer."""
        self.assertEqual(prime_numbers("String"), "Only integers are allowed.")

    def test_invalid_type_is_list(self):
        """Testing if error is returned if input is not integer."""
        self.assertEqual(prime_numbers([]), "Only integers are allowed.")

    def test_invalid_type_is_set(self):
        """Testing if error is returned if input is not integer."""
        self.assertEqual(prime_numbers(set()), "Only integers are allowed.")

    def test_only_positive_numbers(self):
        """Testing if error is returned if a negative number is input."""
        self.assertEqual(prime_numbers(-1), "Negative numbers cannot be prime.")

if __name__ == "__main__":
    unittest.main()
