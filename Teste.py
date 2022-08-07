import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

x, y = sp.symbols('x y')

def sympyFuncion(coeficients):
    global x
    pol = 0
    tot = len(coeficients) - 1
    
    for n in range(tot, 0, -1):
        pol += coeficients[tot-n] * x**n
    
    pol += coeficients[tot]
    return pol





print(lagrangeStringR3(xDados, yDados, zDados))
poly1 = sympyFuncion(lagrange(xDados, zDados).coefficients)
poly2 = sympyFuncion(lagrange(yDados, zDados).coefficients)
poly2 = eval(str(poly2).replace('x', 'y'))

print()
print(poly1)
print(poly2)
print(sp.expand(poly1*poly2).subs(x, 2).subs(y, 5))

