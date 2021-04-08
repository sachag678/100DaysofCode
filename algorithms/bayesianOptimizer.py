import numpy as np
from scipy.stats import norm
from numpy.linalg import cholesky

def expectedImprovement(bestPoint, x):
    mu, sigma = gp_pred(x)
    numerator = mu - bestPoint - eta
    Z = numerator/sigma

    return numerator * norm.cdf(Z) + sigma * norm.pdf(Z)

def gp_pred(x_, x, y):
    '''
    Contains the gaussian process and returns sigma and mu for the value of x.
    '''
    K = kernel(x, x)
    L = cholesky(K + 1e-6*np.eye(len(x)))
    invL = np.linalg.inv(L)
    temp = invL.dot(y)
    alpha = invL.transpose().dot(temp)
    k = kernel(x, x_)
    mu = k.transpose().dot(alpha)
    sigma = np.sqrt(kernel(x_, x_) - k.transpose().dot(invL.transpose().dot(invL)).dot(k))

    return mu, sigma

def kernel(xi, xj):
    return np.exp(-0.5*(np.sum(xi**2, 1).reshape(-1, 1) + np.sum(xj**2,1) - 2*np.dot(xi, xj.T)))

x = np.array([[1, 3, 7]]).reshape(-1, 1)
y = np.array([[2/9.0, 4/9.0, 9/9.0]]).reshape(-1, 1)
xstar = np.array([[5]])
print(gp_pred(xstar, x, y))
