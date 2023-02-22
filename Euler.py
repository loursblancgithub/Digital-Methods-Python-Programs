"""
Name : un_ours_blanc
Version : 1.0 un_ours_blanc 15/12/2022
Language : Python
Object : Euler's method algorithm

inputs : Number of points to calculate

Output : csv file containing all the values
"""

import math
import csv

n = int(input("Entrez le nombre de points à étudier"))

def f(x, y):
  return (math.sin(x))**2 - (2/5)*y

def euler(f, x0, y0, x1, n):
    # Calcul de la longueur des pas h
    h = (x1 - x0) / n

    # Initialisation des variables
    x = x0
    y = y0

    # Liste pour stocker les valeurs de y à chaque étape
    y_values = []

    # Implémentation de la méthode d'Euler
    for i in range(n):
        y += h * f(x, y)
        x += h
        y_values.append(y)

    return y_values


#Résolution de l'équation différentielle
y_values = euler(f, 0.5, 1, 0.6, n)

# Affichage des valeurs de y en chaque étape
print(y_values)

# data rows of csv file
for i in range(0,n-1):
    rows = [y_values[i]]

outfile = open('E:/csvdataset100.csv','w')
out = csv.writer(outfile)
out.writerows(map(lambda x: [x], y_values))
outfile.close()


