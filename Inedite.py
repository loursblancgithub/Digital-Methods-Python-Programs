"""
Name : un_ours_blanc
Version : 1.0 un_ours_blanc 15/12/2022
Language : Python
Object : Runge-Kutta method algorithm

inputs : Number of points to calculate

Output : csv file containing all the values
"""

import math
import csv

n = int(input("Entrez le nombre de points à étudier"))

# Définition de la fonction f(x, y)
def f(x, y):
  return (math.sin(x))*2 - (2/5)*y


def methode_inedite(f, x0, y0, x1, n):
    # Calcul de la longueur des pas h
    h = (x1 - x0) / n

    # Initialisation des variables
    x = x0
    y = y0

    # Liste pour stocker les valeurs de y en chaque étape
    y_values = []

    # Implémentation de la méthode de Heun
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/3, y + k1/2)
        k3 = h * f(x + (2*h)/3, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y += y+2/13*(k1+3*k2+3/2*k3+k4)
        x += h
        y_values.append(y)

    return y_values


# Résolution de l'équation différentielle sur l'intervalle [0, 2]
# avec un pas de 0.1 et en utilisant la méthode de Heun
y_values = methode_inedite(f, 0, 1, 2, 10)

# Affichage des valeurs de y en chaque étape
print(y_values)

# data rows of csv file
for i in range(0,n-1):
    rows = [y_values[i]]

outfile = open('E:/csvdataset2.csv','w')
out = csv.writer(outfile)
out.writerows(map(lambda x: [x], y_values))
outfile.close()