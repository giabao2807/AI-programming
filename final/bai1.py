import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
np.random.seed(2)


def prod(w, X):
    return np.dot(w.T, X)


def sigmoid(s):
    return 1 / (1 + np.exp(-s))


def my_logistic_sigmoid_regression(X, y, w_init, eta, tol=1e-4, max_count=10000):
    w = [w_init]
    it = 0
    N = X.shape[1]
    d = X.shape[0]
    count = 0
    check_w_after = 20
    while count < max_count:
        # mix data
        w_new = 0
        Sum = 0
        mix_id = np.random.permutation(N)
        for i in mix_id:
            xi = X[:, i].reshape(d, 1)
            yi = y[i]
            zi = sigmoid(np.dot(w[-1].T, xi))
            Sum += (yi - zi)*xi

        w_new += w[-1] + eta*Sum/N
        count += 1
        # stopping criteria
        if count % check_w_after == 0:
            if np.linalg.norm(w_new - w[-check_w_after]) < tol:
                return w
        w.append(w_new)
    return w

# method display


def display(w):

    X0 = X[0, np.where(y == 0)][0]
    y0 = y[np.where(y == 0)]

    X1 = X[0, np.where(y == 1)][0]
    y1 = y[np.where(y == 1)]

    plt.plot(X0, y0, 'ro', markersize=8)
    plt.plot(X1, y1, 'bs', markersize=8)
    xx = np.linspace(0, 6, 1000)
    w0 = w[-1][0][0]
    w1 = w[-1][1][0]
    threshold = -w0 / w1
    yy = sigmoid(w0 + w1 * xx)
    plt.axis([-2, 8, -1, 2])
    plt.plot(xx, yy, 'g-', linewidth=2)
    plt.plot(threshold, .5, 'y^', markersize=8)
    plt.xlabel('studying hours')
    plt.ylabel('predicted probability of pass')
    plt.show()


if __name__ == '__main__':
    print("ok")
    # data:
    X = []
    y = []
    dict = {
        'Iris-setosa': 0,
        'Iris-versicolor': 1
    }

    with open('/Users/dinhgiabao/Desktop/HK2-nam3/TTNT/final/input.csv') as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if i != 0:
                X.append(row[0:4])
                y.append(dict[row[4]])
            i = i+1

    # extended data
    X = np.array(X).T.astype(np.float32)
    y = np.array(y)
    X = np.concatenate((np.ones((1, X.shape[1])), X), axis=0)

    epsilon = .05
    d = X.shape[0]
    w_init = np.random.randn(d, 1)

    w = my_logistic_sigmoid_regression(X, y, w_init, epsilon)
    print('Ma trận trọng số nhận được:', w[-1])
    print('Kết quả phân loại của file input.csv', sigmoid(np.dot(w[-1].T, X)))
    display(w)

    print("=====Output.csv=======")

    # data:
    X1 = []
    dict = {
        'Iris-setosa': 0,
        'Iris-versicolor': 1
    }

    with open('/Users/dinhgiabao/Desktop/HK2-nam3/TTNT/final/output_02.csv') as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if i != 0:
                X1.append(row[0:4])
            i = i+1

    # extended data
    X1 = np.array(X1).T.astype(np.float32)
    X1 = np.concatenate((np.ones((1, X1.shape[1])), X1), axis=0)
    print('Kết quả phân loại của file output.csv',
          sigmoid(np.dot(w[-1].T, X1)))
