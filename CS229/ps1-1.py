import pandas as pd
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def sigmoid(x, theta):
    return 1/(1 + np.exp(-(np.dot(x, theta))))

def logistic_regression_using_batch_gradient_descent(x, y, theta, alpha, num_epochs):

    for _ in range(num_epochs):
        theta += alpha*(np.dot(x.T, (y - sigmoid(x, theta))))

    return theta 

def logistic_regression_using_stochastic_gradient_descent(x, y, theta, alpha, num_epochs):
    
    for i in range(num_epochs):
        for x_val, y_val in zip(x, y):
            theta += alpha*((y_val - sigmoid(x_val, theta))*x_val)

    return theta

def logisitic_regression_using_newton_raphson_method(x, y, theta, num_epochs):
    
    for _ in range(num_epochs):
        hypothesis = sigmoid(x, theta)
        H = np.dot(-(hypothesis * (1-hypothesis)) * x.T, x)
        grad = np.dot(x.T, (y - hypothesis))
        theta -= np.dot(inv(H), grad)
    
    return theta

def visualize_loss(y_val, x_val):
    theta = np.zeros((3,))
    theta[0] = -2.6205116
    loss = np.zeros((100, 100))
    for i in range(100):
        theta[1] = i/100
        for j in range(100, 200):
            theta[2] = j/100
            loss[i][j-100] = ((y_val - sigmoid(x_val, theta))**2)

    print(np.argwhere(loss == np.min(loss)))
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(0, 1, 0.01)
    Y = np.arange(1, 2, 0.01)
    X, Y = np.meshgrid(X, Y)

    surf = ax.plot_surface(X, Y, loss)

    plt.show()


def test_all(x, y):

    #print(logistic_regression_using_batch_gradient_descent(x.values, y.values.reshape(len(y)), np.zeros((3,)), 5e-4, 30000))

    #print(logistic_regression_using_stochastic_gradient_descent(x.values, y.values.reshape(len(y)), np.zeros((3,)), 2e-4, 10000))
    
    print(logisitic_regression_using_newton_raphson_method(x.values, y.values.reshape(len(y)), np.zeros((3,)), 10))
 
    #from sklearn.linear_model import LogisticRegression

    #clf = LogisticRegression(fit_intercept=False, C = 1e15)
    #clf.fit(x.values, y.values.reshape(len(y)))

    #print (clf.coef_)

if __name__ == '__main__':

    x = pd.read_csv('q1x.dat', names = ['x1', 'x2'], skipinitialspace=True, delimiter=' ')
    y = pd.read_csv('q1y.dat', names = ['y'])

    x.insert(0, 'x0', np.ones((len(x), 1)))

    test_all(x, y)

    visualize_loss(y.ix[0], x.ix[0])
