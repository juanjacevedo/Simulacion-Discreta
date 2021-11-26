# calcular el area de un triangulo por montecarlo

import random as r
import numpy as np
total=int(input("Ingrese numero de ensayos: "))
H=0.0
for i in range(total):
  x=r.random()
  y=r.random()
  if y <= 1-x:
    H=H+1
print("El area aproximada es:", H/total)