# Scrivere una funzione che prende in input un intero positivo n e
# restituisce e produce un generatore degli interi 0, 1, 3, 6, 10,... . In
# altre parole, l’i-esimo elemento e` (0+1+2+...+i-1)

def generatore(n: 'intero positivo'):
    somma = 0
    i = 0

    for i in range(1, n + 1):
        yield somma
        somma += i


for x in generatore(5):
    print(x)
