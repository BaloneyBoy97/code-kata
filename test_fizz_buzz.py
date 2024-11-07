import unittest
from kata import fizz_buzz  # Importing the fizz_buzz function from kata.py

class TestFizzBuzz(unittest.TestCase):
    
    def test_multiple_of_three(self):
        """Test that multiples of 3 (but not 5) return 'Fizz'."""
        results = fizz_buzz()  # Call the fizz_buzz function to get the list of results
        for i in range(1, 101):
            # Check if 'i' is a multiple of 3 but not a multiple of 5
            if i % 3 == 0 and i % 5 != 0:
                # Assert that the result for this index (i - 1) is 'Fizz'
                self.assertEqual(results[i - 1], "Fizz", f"Failed at index {i}")
    
    def test_multiple_of_five(self):
        """Test that multiples of 5 (but not 3) return 'Buzz'."""
        results = fizz_buzz()  # Call the fizz_buzz function to get the list of results
        for i in range(1, 101):
            # Check if 'i' is a multiple of 5 but not a multiple of 3
            if i % 5 == 0 and i % 3 != 0:
                # Assert that the result for this index (i - 1) is 'Buzz'
                self.assertEqual(results[i - 1], "Buzz", f"Failed at index {i}")
    
    def test_multiple_of_three_and_five(self):
        """Test that multiples of both 3 and 5 return 'FizzBuzz'."""
        results = fizz_buzz()  # Call the fizz_buzz function to get the list of results
        for i in range(1, 101):
            # Check if 'i' is a multiple of both 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                # Assert that the result for this index (i - 1) is 'FizzBuzz'
                self.assertEqual(results[i - 1], "FizzBuzz", f"Failed at index {i}")
    
    def test_neither_multiple_of_three_nor_five(self):
        """Test that numbers not multiples of 3 or 5 return the number itself as a string."""
        results = fizz_buzz()  # Call the fizz_buzz function to get the list of results
        for i in range(1, 101):
            # Check if 'i' is neither a multiple of 3 nor a multiple of 5
            if i % 3 != 0 and i % 5 != 0:
                # Assert that the result for this index (i - 1) is the string version of 'i'
                self.assertEqual(results[i - 1], str(i), f"Failed at index {i}")

if __name__ == '__main__':
    unittest.main()
