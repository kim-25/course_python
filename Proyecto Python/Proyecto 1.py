#realizar un programa que calcule el binomio de newton

import re
import math

def parse_term(term):
    match = re.match(r'([+-]?\d*\.?\d*)([a-z]*)', term)
    if match:
        coef_str, var = match.groups()
        coef = float(coef_str) if coef_str not in ["", "+", "-"] else float(coef_str + "1")
        return coef, var
    else:
        raise ValueError("Introduce la varible en los terminos correctos :)")

auser = input('Introduce el término a: ')
buser = input('Introduce el término b : ')
n = int(input('Introduce la potencia n: '))

a_coef, a_var = parse_term(auser)
b_coef, b_var = parse_term(buser)

def cbinom(n, k):
    # Para calcular el coeficiente binomial de n sobre k
    return math.comb(n, k)

def bnewton(a_coef, b_coef, n):
    # Calcula el binomio de Newton
    resultado = []
    for k in range(n + 1):
        coef = cbinom(n, k)
        termino = coef * (a_coef ** (n - k)) * (b_coef ** k)
        resultado.append(termino)
    return resultado

def imprimir_resultado(a_coef, a_var, b_coef, b_var, n):
    # Imprime el binomio de Newton
    expansion = bnewton(a_coef, b_coef, n)
    terminos = []
    for k in range(n + 1):
        coef = expansion[k]
        a_term = f"{a_var}^{n-k}" if (n-k) > 0 else ""
        b_term = f"{b_var}^{k}" if k > 0 else ""
        if a_term and b_term:
            terminos.append(f"{coef}{a_term}{b_term}")
        elif a_term:
            terminos.append(f"{coef}{a_term}")
        elif b_term:
            terminos.append(f"{coef}{b_term}")
        else:
            terminos.append(f"{coef}")
    print(" + ".join(terminos))

imprimir_resultado(a_coef, a_var, b_coef, b_var, n)
