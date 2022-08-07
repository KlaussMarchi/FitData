import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
x = sp.symbols('x')


# ESTABELECENDO OS DADOS X E Y QUE SERÃO USADOS PARA INTERPOLAÇÃO
xDados = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
yDados = np.array([1.2, 1.9, 2.6, 3.5, 4.4, 5.6, 6.8, 8, 9.5, 11, 12.7])
poly = lagrange(xDados, yDados)

# USANDO A BIBLIOTECA PARA MOSTRAR O POLINÔMIO
print(poly)                # MOSTRANDO POLINÔMIO
print(poly(0))             # ENCONTRANDO VALORES CONTÍNUOS (Y=? QUANDO X=0)
print(poly.coefficients)   # MOSTRANDO OS COEFICIENTES DO POLINÔMIO ENCONTRADO
print()


# USANDO A BIBLIOTECA SYMPY PARA IMPRIMIR O POLINÔMIO
def sympyFuncion(coeficients):
    global x
    pol = 0
    tot = len(coeficients) - 1
    
    for n in range(tot, 0, -1):
        pol += coeficients[tot-n] * x**n
    
    pol += coeficients[tot]
    return pol

f = sympyFuncion(poly.coefficients)   # GERANDO O POLINÔMIO
print(f)                              # MOSTRANDO POLINÔMIO
print(f.subs(x, 0))                   # ENCONTRANDO VALORES CONTÍNUOS (Y=? QUANDO X=0)


# GERANDO UM GRÁFICO COM OS VALORES ENCONTRADOS DA FUNÇÃO
xDados = np.linspace(min(xDados), max(xDados), 1000)
yDados = np.array([f.subs(x, c) for c in xDados])

plt.plot(xDados, yDados)
plt.title('Gráfico de Interpolação')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.show()


# EXTRA - POLINÔMIO DE LAGRANGE COM 2 VARIÁVEIS
def lagrangeString(x, y):
    n = len(x)
    string = ''

    for i in range(0, n):
        for j in range(0, n):
            if j != i:
                string += f' (x - {x[j]}) / ({x[i]} - {x[j]}) *'
        string += f" {y[i]} + "

    x = sp.symbols('x')
    expressao = eval(string[:-3])
    expressao = sp.expand(expressao)
    return expressao

xDados = [2, 3, 4]
yDados = [5, 6, 7]

f = lagrangeString(xDados, yDados)
print()
print(f)
print(f.subs(x, 2))


# EXTRA - POLINÔMIO DE LAGRANGE COM 3 VARIÁVEIS
def lagrangeStringR3(x, y, z):
    n = len(x)
    string = ''
    for i in range(0, n):
        for j in range(0, n):
            if j != i:
                X = f'(x - {x[j]}) / ({x[i]} - {x[j]})'
                Y = f'(y - {y[j]}) / ({y[i]} - {y[j]})'
                string += f'{X} * {Y} *'
        string += f" {z[i]} + "

    x, y = sp.symbols('x y')
    expressao = eval(string[:-3])
    expressao = sp.expand(expressao)
    return expressao

xDados = [2, 3, 4]
yDados = [5, 6, 7]
zDados = [8, 9, 10]

x, y = sp.symbols('x y')
f = lagrangeStringR3(xDados, yDados, zDados)

print()
print(f)
print(f.subs(x, 2).subs(y, 5))