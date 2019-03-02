import  numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


# this are the requirements how we want to map our values to colours
max_value=50
ys=[0.25, 0.333,   0.8, 0.95,         1]
xs=[0,    1,        5,    16, max_value]


def map_values_lin(x):
    return np.interp(x, xs, ys)

x = np.arange(0,100)
yl = map(map_values_lin, x)


def fun(t, a, b, c):
    return a*np.exp(-b*t)+c


poly_res = optimize.curve_fit(fun,  xs,  ys)
print(poly_res)
a=poly_res[0][0]
b=poly_res[0][1]
c=poly_res[0][2]
mapping="{0} * 1/(e^({1}*x )+ {2}".format(a, b, c)
print(mapping)


def map_values(x):
    return fun(x, a, b, c)


def inv_fun(y, a, b, c):
    # y = a*1/np.exp(b* t )+c
    # (y- c)/a = 1/np.exp( b * t)
    x = np.log(a/(y-c))/b
    return x

def test_colors():
    plt.imshow([ys],cmap="jet", vmax=1, vmin=0)
    plt.figure()
    plt.plot(x, yl)
    y =  fun(x, a, b, c)
    plt.plot(x, y)
    plt.title(mapping)
    plt.savefig("res/mapping.svg")
    plt.figure()
    plt.imshow(map_values(np.array([np.arange(0, 15, 0.5)]).T), vmin=0, vmax=1, cmap="jet")
    plt.savefig("res/values.svg")
