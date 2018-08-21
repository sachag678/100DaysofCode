
import pandas as pd
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

x = pd.read_csv('q2x.dat', names = ['x1'])
y = pd.read_csv('q2y.dat', names = ['y'])

x.insert(0, 'x0', np.ones((len(x), 1)))

def linear_regression_using_normal_equations(x, y):
    return np.dot(inv(np.dot(x.T, x)), np.dot(x.T, y))

def linear_regression_using_weighted_normal_equations(x, y, tau=0.8):
    xline = np.arange(np.min(x[:, 1]), np.max(x[:, 1]), 0.1)
    line_val = []
    for pnt in xline:
        W = np.diag(np.diag(np.ones((len(x), len(x)))))
        W *= np.exp(-(pnt - x[:, 1])**2/(2 * tau**2))
        theta = np.dot(inv(np.dot(x.T.dot(W), x)), np.dot(x.T.dot(W), y))
        line_val.append(pnt*theta[1] +  theta[0])
    return line_val

theta = linear_regression_using_normal_equations(x.values, y.values.reshape(len(y)))
weighted_line = linear_regression_using_weighted_normal_equations(x.values, y.values.reshape(len(y)))

# plot the unweighted linear regression
xline = np.arange(np.min(x['x1']), np.max(x['x1']), 0.1)
yline = theta[1]*xline + theta[0]

plt.scatter(x['x1'], y)
plt.plot(xline, yline)
plt.plot(xline, weighted_line)
plt.show()