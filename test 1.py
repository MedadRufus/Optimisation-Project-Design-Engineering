# Created by Medad Rufus Newman on 11/10/2019

from scipy.optimize import minimize, rosen, rosen_der


def func_w(x0):
    d,t  = x0
    return 88.9*d*t
res = minimize(func_w, (2, 0), method='SLSQP')
print(res)