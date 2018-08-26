"""Implement Binary Search."""
import time
import numpy as np

def timer(func):
    def wrap(*args):
        time1 = time.time()
        ret = func(*args)
        time2 = time.time()
        print(func.__name__, ':', (time2-time1)*1000.0)
        return ret 
    return wrap

@timer
def binary_search(array, target):
    """Return index of target element in array using binary search."""
    min = 0
    max = len(array) - 1
    guess = (min + max)//2
    while array[guess] != target:
        if min >= max:
            return -1
        if array[guess] < target:
            min = guess + 1
        else:
            max = guess - 1
        guess = (min + max)//2
    return guess

@timer
def binary_search_recursive(array, target):
    """Recursive version of binary search. (Slower than the regular iterative approach.)"""
    min = 0
    max = len(array) - 1
    guess = (min + max)//2
    return recurse(array, target, min, max, guess)

def recurse(array, target, min, max, guess):
    """Calls itself until a stopping condition is met."""
    if array[guess] == target:
        return guess
    
    if min>=max:
        return -1

    if array[guess] < target:
        min = guess + 1
    else:
        max = guess -1 

    guess = (min + max)//2

    return recurse(array, target, min, max, guess) 

@timer
def linear_search(array, target):
    """Return index of target element in array using linear search."""
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

@timer
def built_int_search(array, target):
    """Testing the in built version."""
    return array.index(target)

if __name__ == '__main__':
    array = list(range(10000000))
    target = 5567393
    print(binary_search(array, target))
    print(linear_search(array, target))
    print(built_int_search(array, target))
    print(binary_search_recursive(array, target))