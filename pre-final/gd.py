import math
import numpy as np


def f(x):
    return float(math.pow(np.exp(-x) - 4 / np.exp(2*x), 2))


def f1(x):
    delta = 0.000000001
    return float((f(x+delta)-f(x)))/delta


alpha = 0.0001
x = -0.3
esp = 0.001
while abs(f1(x)) > esp:
    x -= alpha*f1(x)

print("x = %.6f" % x)
print("f(x) = %.6f" % f(x))
