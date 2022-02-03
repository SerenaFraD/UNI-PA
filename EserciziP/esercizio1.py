# Scrivere una funzione che prende in input una lista L e restituisce una
# lista di |L|! liste in cui ciascuna lista contiene una diversa
# permutazione degli elementi della lista input L
import math
import random


output = list()
lista = list(["a", "b", "c"])

lenght = len(lista)
fact = math.factorial(lenght)

for i in range(0, fact):
    indexs = random.sample(range(0, lenght), lenght)
    tmp = list([lista[i] for i in indexs])

    output.append(tmp)

print(output)
