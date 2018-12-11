import numpy as np
from decimal import *
import unittest

def is_prime(x):
    if x % 2 == 0 and x > 2:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False

    return True

def find_primes(prec=1000):
    getcontext().prec = prec

    factorial = 1
    euler = 2

    for i in range(2, 100):
        factorial *= i
        euler += Decimal(1)/Decimal(factorial)

    euler = str(euler).replace('.','')

    size = 10
    found = False

    for j in range(1, len(euler)-size):
        number = int(euler[j:j+size])
        if is_prime(number):
            print('The first prime in the decimals of eulers number is {} which is found at the {}th decimal.'.format(number, j))
            found = True
            break
        print('{}: Not Prime'.format(number))

    if not found:
        print('Didnt find - keep looking further')

class TestPrime(unittest.TestCase):

    def test_primes(self):
        primes = [2, 3, 5, 7, 11]
        for p in primes:
            self.assertEqual(is_prime(p), True)

    def test_non_primes(self):
        non_primes = [4, 6, 8, 9, 10, 7182818284]
        for p in non_primes:
            self.assertEqual(is_prime(p), False)

if __name__ == '__main__':
    find_primes()
