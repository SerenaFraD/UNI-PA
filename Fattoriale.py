#esempio dal pdf lez1_2
#esampio fattoriale

def factorial(n):
    result = 1
    for k in range(1, n+1):
        result = result  * k
    return result

print("Fattoriale di 3:", factorial(3))
print("Fattoriale di 3:", factorial(1))
print("Fattoriale di 3:", factorial(0))
