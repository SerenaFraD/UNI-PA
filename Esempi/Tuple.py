#Class Tupla
#Versione immutabile delle liste

t = () #definizione vuota
print("t = ", t)
t = (12,) #contiene solo elemento 12
print("t = ", t)

print("\nLunghezza tupla")
i = len(t)
print("La lunghezza è ", i)

print("\nUnpacking")
t = (1, 's', 4)
print("Tupla ", t, " tipo ", type(t))
x, y, z = t #assegna ad ogni variabile un elemento della tupla
print("x ", x, " tipo ", type(x))
print("y ", y, " tipo ", type(y))
print("z ", z, " tipo ", type(z))

print("\nEsempio di immutable con tuple")
try:
    t[0] = 0
except Exception as e: print(e)

