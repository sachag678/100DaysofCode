"""Recursion."""
import unittest
from search_algorithms import timer
import time
import numpy as np
import copy

def recursive_factorial(n):
    
    if n<=1:
        return 1
    return n*recursive_factorial(n-1)

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

def calculate_power_set(input_set, power_set = None):
    """Problem 8.4 - Cracking the coding interview.
    
    Calculate the power set using recursion. The pitfall with this approach is that it goes to 
    the case of n = 0, n times. So we are extending the tree n^n times instead of 2^n times.
    """
    if power_set is None:
        power_set = [] 

    if len(input_set) == 0:
        power_set.append([])
        return power_set
    
    power_set.append(copy.deepcopy(input_set))

    for i in range(len(input_set)):
        removed_value = input_set.pop(i)
        power_set = calculate_power_set(input_set, power_set)
        input_set.insert(i, removed_value)
    
    return power_set

def calculate_power_set_2(input_set, index=0):
    """Book version - Uses the idea that the powerset of n is made up of the powerset of n - 1 plus
    a clone of powerset of n - 1 with n added to it.

    P(1) = [[], [1]]
    P(1) + 2 = [[2], [1, 2]]   +
    -----------------------------
    P(2) = [[], [1], [2], [1, 2]]

    """
    power_set = [] 

    if len(input_set) == index:
        power_set.append([])
    else:
        power_set = calculate_power_set_2(input_set, index + 1)
        item = input_set[index]
        moresubset = []
        for subset in power_set:
            newsubset = []
            newsubset.extend(subset)
            newsubset.append((item))
            moresubset.append(newsubset)
        power_set.extend(moresubset)
    
    return power_set

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

def test_time_complexity_of_power_set():
    """Test my version of power set vs the text book version. My version is much slower and after 9 numbers in the set
    starts to become too slow."""
    
    s = [1, 2, 4, 5, 6, 7, 8, 9, 10]
 
    begin = time.time()
    (calculate_power_set(s))
    print('Time taken for my version is {} s.'.format((time.time()-begin)*1000.0))

    begin = time.time()
    (calculate_power_set_2(s))
    print('Time taken for book version is {} s.'.format((time.time()-begin)*1000.0))

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
