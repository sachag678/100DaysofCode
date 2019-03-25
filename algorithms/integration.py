import numpy as np


def trap(a, b, k):
    '''This function approximates the integration numerically
    using the trapezod method
    params: a - limit0
            b - limit1
            k - number of intervals or rectangles to place under the curve
    return: the numerical integration over the limit

    change the function y to whatever the user wants
    '''
    sum = 0
    for i in range(k+1):
        x = a+(b-a)*i/k
        y = np.cos(x)
        if i == 0 or i == k:
            y = y/2
        sum += y

    sum = sum*(b-a)/k
    return sum


print(trap(-1, 1, 1000000))

print(np.sin(1)-np.sin(-1))
