import numpy as np
import pandas as pd    
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import StratifiedKFold
from math import factorial as fact

x = pd.read_csv('q1x.dat', names = ['x1', 'x2'], skipinitialspace=True, delimiter=' ')
y = pd.read_csv('q1y.dat', names = ['y'])

x.insert(0, 'x0', np.ones((len(x), 1)))

lr = LogisticRegression(fit_intercept=False, C = 1e15)
nb = DummyClassifier(strategy='uniform')

skfold = StratifiedKFold(n_splits=2, random_state=42)
lr_y_pred = []
nb_y_pred = []
y_fold = []

for train_index, test_index in skfold.split(x.values, y.values.reshape(len(y))):
    x_train_fold = x.values[train_index]
    y_train_fold = y.values.reshape(len(y))[train_index]
    x_test_fold = x.values[test_index]
    y_test_fold = y.values.reshape(len(y))[test_index]

    lr.fit(x_train_fold, y_train_fold)
    lr_y_pred.append(lr.predict(x_test_fold))
    
    nb.fit(x_train_fold, y_train_fold)
    nb_y_pred.append(nb.predict(x_test_fold))

    y_fold.append(y_test_fold)

lr_counts = 0
nb_counts = 0

for i in range(len(y_fold)):
    different = lr_y_pred[i] != nb_y_pred[i]

    for lry, nby, y_act in zip(lr_y_pred[i][different], nb_y_pred[i][different], y_fold[i][different]):

        if lry == y_act and lry != nby:
            lr_counts += 1
        elif nby == y_act and nby != lry:
            nb_counts += 1

print(lr_counts, nb_counts)

def calculate_p_value(n, s):
    """Uses the binomial distribution to determine the p-value.
        P(s>=observed|p(s)=0.5)
        where s is the number of success which are that classifier A predicted correctly when classifier B did not.
        This can be calculated using the binomial distribution 
        (n!/(s!(n-s)!)*p^s*q^n-s

        params: n - the total number of different predictions by each classifier
                s - the total number of cases where classifier A was correct and B was wrong 
        
        return: p_val - the probability that Classifier A's results are different to Classifier B's by random chance 
    """
    p_val = 0
    for number in range(s,n + 1):
        p_val += (fact(n)/(fact(number)*fact((n - number))))*0.5**n
    
    return p_val

print('The probability that lr results are better than nb results is {}.'.format(calculate_p_value(lr_counts+nb_counts, lr_counts)))