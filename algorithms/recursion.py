"""Recursion."""
import unittest

def factorial(n, sum=None):
    """Recursive factorial."""
    if sum is None:
        sum = n
    if n == 1:
        return sum
    sum *= n-1
    return factorial(n-1, sum)

def iterative_factorial(n):
    """Iterative factorial."""
    sum = 1
    for i in range(1, n + 1):
        sum*=i
    return sum

def is_palindrome(word):
    if word[0] != word[-1]:
        return False
    elif len(word) == 1 or len(word) == 0:
        return True
    else:
        return is_palindrome(word[1:len(word)-1])

def powers(n, x):
    if n == 0:
        return 1
    
    if n % 2 != 0 and n > 0:
        return x*powers(n-1,x)
    
    if n % 2 == 0:
        return powers(n/2, x)*powers(n/2, x)
    
    if n<0:
        return 1/powers(-n, x)

class TestRecursion(unittest.TestCase):
    """Testing recursion."""

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(iterative_factorial(5), 120)
    
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('rotor'), True)
        self.assertEqual(is_palindrome('rater'), False)
        self.assertEqual(is_palindrome('mater'), False)
    
    def test_powers(self):
        self.assertEqual(powers(0, 2), 1)
        self.assertEqual(powers(1, 2), 2)
        self.assertEqual(powers(2, 2), 4)
        self.assertEqual(powers(-1, 2), 1/2)
        

if __name__ == "__main__":
    unittest.main()