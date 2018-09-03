"""This code is implementing the following papers reccomendations - On Comparing Classifiers: Pitfalls to Avoid and a
Recommended Approach. 
http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=21D16E681FF16B0BA91D741A63806A31?doi=10.1.1.29.5194&rep=rep1&type=pdf"""

import numpy as np
import pandas as pd    
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import StratifiedKFold
from math import factorial as fact

def load_data():
    """Load datasets."""
    x = pd.read_csv('q1x.dat', names = ['x1', 'x2'], skipinitialspace=True, delimiter=' ')
    y = pd.read_csv('q1y.dat', names = ['y'])

    x.insert(0, 'x0', np.ones((len(x), 1)))

    return x, y

def init_algo():
    """Initialize Logistic Regression and Dummy Classifier."""
    lr = LogisticRegression(fit_intercept=False, C = 1e15)
    dm = DummyClassifier(strategy='uniform')
    nb = GaussianNB()

    return lr, nb, dm

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

def get_succeses(a, b, x, y, number_of_folds=2):
    """Calculate the counts of where a has correctly classified a test case and b hasn't and where
    b has correctly classified a test case and a hasn't.
    params: a - classifier a
            b - classifier b
            x - inputs
            y - labels
    return:
        a_counts - counts of a where a is correct and b isn't
        b_counts - counts of b where b is correct and a isn't 
    """

    skfold = StratifiedKFold(n_splits=number_of_folds, random_state=42)
    a_pred = []
    b_pred = []
    y_fold = []

    for train_index, test_index in skfold.split(x.values, y.values.reshape(len(y))):
        x_train_fold = x.values[train_index]
        y_train_fold = y.values.reshape(len(y))[train_index]
        x_test_fold = x.values[test_index]
        y_test_fold = y.values.reshape(len(y))[test_index]

        a.fit(x_train_fold, y_train_fold)
        a_pred.append(a.predict(x_test_fold))
        
        b.fit(x_train_fold, y_train_fold)
        b_pred.append(b.predict(x_test_fold))

        y_fold.append(y_test_fold)

    a_counts = 0
    b_counts = 0

    for i in range(len(y_fold)):
        different = a_pred[i] != b_pred[i]

        for lry, nby, y_act in zip(a_pred[i][different], b_pred[i][different], y_fold[i][different]):

            if lry == y_act and lry != nby:
                a_counts += 1
            elif nby == y_act and nby != lry:
                b_counts += 1
    
    return a_counts, b_counts

if __name__ == '__main__':
    x, y = load_data()
    a, b, c = init_algo()
    a_counts, b_counts = get_succeses(a, b, x, y)
    a_name = a.__class__.__name__
    b_name = b.__class__.__name__

    print('The number of successes for {} and {} are {} and {}.'.format(a_name, b_name, a_counts, b_counts))
    print('The percent chance that {}\'s results are better than {}\'s results by random chance is {:.1f}%.'.format(a_name, b_name, calculate_p_value(a_counts+b_counts, a_counts)*100.0))