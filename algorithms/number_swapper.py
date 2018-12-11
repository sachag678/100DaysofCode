# Write a function to swap a number in place (that is without temporary variables.)
# hint 1: Try picturing the two numbers, a and b on a number line.
# hint 2: Let diff be the difference between a and b. Can you use the diff in some way? Then can you get rid of this
# temporary variable
# hint 3: You could also try using XOR

def swap_pythonic(a, b):
    a, b = b, a
    return a, b

def swap_with_temp(a, b):
    """With temp variable"""
    temp = a
    a = b
    b = temp
    return a, b

def swap(a, b):
    """Replace temp variable with a function."""
    b = b - diff(a, b)
    a = a + diff(a, b)
    return a, b

def diff(a, b):
    return b - a

print(swap(4, 5))

# XOR
# IN, IN, OUT
# 0, 0, 0
# 0, 1, 1
# 1, 0, 1
# 1, 1, 0
