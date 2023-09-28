import numpy as np
from scipy.optimize import curve_fit
from scipy import stats

x = np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70])
y = np.array([100,100,98,90,88,85,79,75,70,64,56,47,39,29,11])


def parabola(x,a,b,c):
    return a * x**2 + b * x + c

def recta(x,m,b):
    return m * x + b


parametros_parabola, covariance_para = curve_fit(parabola, x, y)


parametros_recta, covariance_recta = curve_fit(recta, x, y)

r_parabola, _ = stats.pearsonr(y, parabola(x, *parametros_parabola))
r_parabola_2 = r_parabola**2

r_recta, _ = stats.pearsonr(y, recta(x, *parametros_recta))
r_recta_2 = r_recta**2

print("Parámetros de la parábola (a, b, c):", parametros_parabola)
print("Parámetros de la recta (m, b):", parametros_recta)
print(f"Coeficiente R^2 para la parábola: {r_parabola_2:.3f}")
print(f"Coeficiente R^2 para la recta: {r_recta_2:.3}")