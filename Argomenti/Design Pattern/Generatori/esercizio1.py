# Scrivere una funzione generatrice myGenerator(n) che prende in
# input un intero n>=1 e restituisce un iteratore dei primi n fattoriali. In
# altre parole, la prima volta che viene invocato next viene restituito 1!,
# la seconda volta 2!, la terza volta 3!, e cosi` via fino ad n! 

def myGenerator(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact


print("I fattoriali")
for f in myGenerator(20):
    print(f)
