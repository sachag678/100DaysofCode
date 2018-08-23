
import pandas as pd
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

x = pd.read_csv('q2x.dat', names = ['x1'])
y = pd.read_csv('q2y.dat', names = ['y'])

x.insert(0, 'x0', np.ones((len(x), 1)))
x['x2'] = x['x1']**2
x['x3'] = x['x1']**3
x['x4'] = x['x1']**4
x['x5'] = x['x1']**5

def linear_regression_using_normal_equations(x, y):
    return np.dot(inv(np.dot(x.T, x)), np.dot(x.T, y))

def linear_regression_using_normal_equations_with_regularization(x, y, lamda):
    """The model learned using linear regression has a high bias problem.
        Using regularization with a smaller lamda will lead to lowering 
        the bias - Though given that there are only two parameters, 
        I wonder how much it can improve the result.
    """
    diag = np.diag(np.diag(np.ones((x.shape[1], x.shape[1]))))
    diag[0][0] = 0
    return np.dot(inv(x.T.dot(x)+lamda*diag), np.dot(x.T, y))

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
theta_regularized = linear_regression_using_normal_equations_with_regularization(x.values, y.values.reshape(len(y)), 50)
weighted_line = linear_regression_using_weighted_normal_equations(x[['x0', 'x1']].values, y.values.reshape(len(y)))

print('theta:', theta)
print('regularized_theta:', theta_regularized)

# plot the unweighted normal and regularized linear regression 
xline = np.arange(np.min(x['x1']), np.max(x['x1']), 0.1)
yline = theta[0] + theta[1]*xline + theta[2]*xline**2 + theta[3]*xline**3 + theta[4]*xline**4 + theta[5]*xline**5
yline_regularized = theta_regularized[0] + theta_regularized[1]*xline + theta_regularized[2]*xline**2 + theta_regularized[3]*xline**3 + theta_regularized[4]*xline**4 + theta_regularized[5]*xline**5

plt.scatter(x['x1'], y)
plt.plot(xline, yline)
plt.plot(xline, yline_regularized)
plt.plot(xline, weighted_line)
plt.show()