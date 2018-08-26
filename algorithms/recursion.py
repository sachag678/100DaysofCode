"""Recursion."""
import unittest
from search_algorithms import timer
import time
import numpy as np

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

@timer
def fibonacci(n):
    """Return the n'th fibonacci number - Iterative (Turns out to be the bottom up dynamic programming approach.)"""
    curr = 0
    next = 1
    for _ in range(n):
        curr, next = next, curr + next
    return curr

def fibonacci_recursive(n):
    """Return the n'th fibonacci number - Recursive"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_recursive_with_memoization(n, memory = None):
    """Return the n'th factorial number - Recursive with memoization."""
    if memory is None:
        memory = np.zeros(n)

    if n == 0 or n == 1:
        return n
    
    if memory[n - 1] == 0:
        memory[n - 1] = fibonacci_recursive_with_memoization(n - 1, memory) + fibonacci_recursive_with_memoization(n - 2, memory)
    
    return memory[n - 1]

def triple_step_with_memoization(n, memory=None):
    """Problem 8.1 - Cracking the coding interview. 
        A child running up a staircase with n-steps can hop either 1, 2 or 3 ar a time. How many
        possible ways can the child run up the stairs.
    """
    if memory is None:
        memory = np.zeros(n)

    if n == 0:
        return 1
    if n < 0:
        return 0
    if memory[n - 1] == 0: 
        memory[n - 1] = triple_step_with_memoization(n - 1, memory) + triple_step_with_memoization(n - 2, memory) + triple_step_with_memoization(n - 3, memory)
    
    return memory[n - 1].astype(np.uint64)

def triple_step(n):
    """Same solution as the previous function but without memoization and only simple recursion."""
    if n == 0:
        return 1
    if n < 0:
        return 0

    return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)

def test_time_complexity_of_fibonacci():
    """Test the speed of bottom-up dynamic programming vs recursive without caching."""
    fib_num = 5
    print(fibonacci(fib_num))

    begin = time.time()
    fibonacci_recursive(fib_num)
    print('recursive_fibonacci:', (time.time()-begin)*1000.0)

    begin = time.time()
    fibonacci_recursive_with_memoization(fib_num)
    print('recursive_fibonacci with memoization:', (time.time()-begin)*1000.0)

def test_time_complexity_of_triple_step():
    """Test regular recursive vs recursive with memoization."""
    num_steps = 23 

    begin = time.time()
    print('There is(are) {} way(s) to climb the steps when n is {}.'.format(triple_step_with_memoization(num_steps), num_steps))
    print('Time taken is: {} s.'.format((time.time() - begin)*1000))
   
    begin = time.time()
    print('There is(are) {} way(s) to climb the steps when n is {}.'.format(triple_step(num_steps), num_steps))
    print('Time taken is: {} s.'.format((time.time() - begin)*1000))

class TestRecursion(unittest.TestCase):
    """Test Recursive functions."""

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
    
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
    
    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_recursive(2), 1)
        self.assertEqual(fibonacci_recursive(3), 2)
        self.assertEqual(fibonacci_recursive(4), 3)
        self.assertEqual(fibonacci_recursive(5), 5)
    
    def test_fibonacci_recursive_with_memoization(self):
        self.assertEqual(fibonacci_recursive_with_memoization(0), 0)
        self.assertEqual(fibonacci_recursive_with_memoization(1), 1)
        self.assertEqual(fibonacci_recursive_with_memoization(2), 1)
        self.assertEqual(fibonacci_recursive_with_memoization(3), 2)
        self.assertEqual(fibonacci_recursive_with_memoization(4), 3)
        self.assertEqual(fibonacci_recursive_with_memoization(5), 5)
    
    def test_triple_step(self):
        self.assertEqual(triple_step(3), 4)
        self.assertEqual(triple_step(4), 7)
        self.assertEqual(triple_step_with_memoization(3), 4)
        self.assertEqual(triple_step_with_memoization(4), 7)


if __name__ == "__main__":
    unittest.main()