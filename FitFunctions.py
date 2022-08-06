from scipy.optimize import curve_fit
import numpy as np
from numpy import e, pi, log, sin, cos, tan, sqrt
import matplotlib.pyplot as plt


def fitData(xDados, yDados):
    xDados = np.array(xDados)
    yDados = np.array(yDados)

    def funcaoLinear(x, a, b):
        return a * (x) + b

    def funcaoExponencial(x, Yo, k, b):
        return Yo * e ** (-k * (x + b))

    def funcaoExponencialSuporte(x, Yo, M, k):
        A = (M - Yo) / Yo
        return M / (1 + A * e ** (-k * x))

    def funcaoLogaritmica(x, a, b, c):
        return a * log(abs(x + b)) + c

    def funcaoQuadratica(x, a, b, c):
        return a * (x ** 2) + b * x + c

    def funcaoCubica(x, a, b, c, d):
        return a * (x ** 3) + b * (x ** 2) + c * x + d

    def funcaoQuadrupla(x, a, b, c, d, e):
        return a * (x ** 4) + b * (x ** 3) + c * (x ** 2) + d * x + e

    def funcaoQuintupla(x, a, b, c, d, e, f):
        return a * (x ** 5) + b * (x ** 4) + c * (x ** 3) + d * (x ** 2) + e * x + f

    def funcaoPotencia(x, a, b, c):
        return a * (x ** b) + c

    def funcaoRaiz(x, a, b, c, d):
        return a * sqrt(abs(b * x + c)) + d

    def funcaoSeno(x, a, b, c, d):
        return a * sin(b * (x + c)) + d

    def funcaoTangente(x, a, b, c, d):
        return a * tan(b * (x - d)) + c

    def funcaoHiperbole(x, a, b, c, n, d):
        return (a) / (b * x + c)**n + d

    def funcaoNormal(x, a, media, desvio):
        return (a) / (desvio * ((2 * pi) ** (0.5))) * (e ** (-1 * ((x - media) ** 2) / (2 * (desvio ** 2))))

    def FuncaoSenoideQuadratica(x, a, b, c, d, e, f, g):
        return a * (x + b) ** 2 - c * (x + d) * np.cos(e * x) + f * x + g

    def PolinomioGrau13(x, a, b, c, d, e, f, g, h, i, j, k, l, m, n):
        return a * (x ** 13) + b * (x ** 12) + c * (x ** 11) + d * (x ** 10) + e * (x ** 9) + f * (x ** 8) + g * (x ** 7) \
               + h * (x ** 6) + i * (x ** 5) + j * (x ** 4) + k * (x ** 3) + l * (x ** 2) + m * x + n

    listaFuncoes = {
        'Função Linear': funcaoLinear,
        'Função Exponencial': funcaoExponencial,
        'Função Exponencial Suporte': funcaoExponencialSuporte,
        'Função Logaritmica': funcaoLogaritmica,
        'Função Quadratica': funcaoQuadratica,
        'Função Cubica': funcaoCubica,
        'Polinômio Grau 4': funcaoQuadrupla,
        'Polinômio Grau 5 ': funcaoQuintupla,
        'Função Potência': funcaoPotencia,
        'Função Raiz': funcaoRaiz,
        'Função Seno': funcaoSeno,
        'Função Tangente': funcaoTangente,
        'Função Hiperbólica': funcaoHiperbole,
        'Função Normal': funcaoNormal,
        'Função Senoide Quadrática': FuncaoSenoideQuadratica,
        'Polinomio Grau 13': PolinomioGrau13
    }

    for nome, funcao in listaFuncoes.items():
        coeficientes = curve_fit(funcao, xDados, yDados, maxfev=1000000)  # MÁXIMO DE ITERAÇÕES
        print('COEFICIENTES: ', list(coeficientes[0]))

        xFuncao = np.linspace(min(xDados), max(xDados), 10000)
        yFuncao = funcao(xFuncao, *coeficientes[0])  # RECEBE UMA LISTA COM OS VALORES F(XDados)

        plt.scatter(xDados, yDados, color='Orange')
        plt.plot(xFuncao, yFuncao, color='blue', linewidth=2.5)
        plt.title(nome, fontsize=16)
        plt.xlabel('Valores de X')
        plt.ylabel('Valores de Y')
        plt.show()


xDados = [12.6, 12.5, 12.42, 12.32, 12.20, 12.06, 11.9, 11.75, 11.58, 11.31, 10.5]
yDados = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
fitData(xDados, yDados)