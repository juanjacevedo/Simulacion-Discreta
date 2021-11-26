#Sacar una carta al azar de un baraja de estas.

import random

cartas = []

for i in range(1,53):
    cartas.append(i)
    
print(cartas[random.randint(0, len(cartas))])


