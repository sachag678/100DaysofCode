import matplotlib.pyplot as plt
import numpy as np
from recursion import factorial

x = np.arange(1, 5, 1)
n_squared = x**2
n = x
two_to_the_n = 2**x
n_log_n = x*np.log(x)
log_n = np.log(n)
fact_n = []
for val in x:
    fact_n.append(factorial(val))

plt.plot(x,n, x, n_squared, x, two_to_the_n, x, n_log_n, x, log_n, x, fact_n)
plt.legend(['O(n)','O(n^2)','O(2^n)','O(nlog(n))', 'O(log_n)', 'O(n!)'])
plt.xlabel('n')
plt.ylabel('Time Complexity')
plt.show()