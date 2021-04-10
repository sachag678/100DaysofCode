import numpy as np
from scipy.stats import norm
from numpy.linalg import cholesky
import matplotlib.pyplot as plt

def expectedImprovement(bestPoint, x_, x, y):
    mu, sigma = gp_pred(x_, x, y)
    eta = 0.001
    numerator = mu - bestPoint - eta
    Z = numerator/sigma

    return numerator * norm.cdf(Z) + sigma * norm.pdf(Z), mu, sigma

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

points = [0.1*i for i in range(100)]

EI = []
GPmu = []
GPsigma = []

for i in points:
    xstar = np.array([[i]]).reshape(-1, 1)
    bestPoint = np.array([[1.0]]).reshape(-1, 1)
    ei, mu, sigma = expectedImprovement(bestPoint, xstar, x, y)
    EI.append(ei.flatten()[0])
    GPmu.append(mu.flatten()[0])
    GPsigma.append(sigma.flatten()[0])

# Find the max point
maxEIIdx = np.argmax(EI)

fig = plt.figure()
gs = fig.add_gridspec(2, hspace=0)
axs = gs.subplots(sharex=True)
axs[0].plot(x, y, 'ro', points, GPmu, 'b--')

GPmu = np.array(GPmu)
GPsigma = np.array(GPsigma)
points = np.array(points)
bot = GPmu - GPsigma
top = GPmu + GPsigma

axs[0].fill_between(points, bot, top, alpha=0.5)
axs[1].plot(points, EI, [points[maxEIIdx]], EI[maxEIIdx], 'r+')

for ax in axs:
    ax.label_outer()

plt.show()
