#Classe Float
#Float -> classe Immutable

print("Uso del costruttore float(), con 1 e 2.3")
f = float() #restituisce 0.0 di default
print('La variabile f vale', f)
f = float(1) #restiruisce 1.0
print('La variabile f vale', f)
f = float(2.3) #restituisce 2.3
print('La variabile f vale', f)

print("Rappresentazione come rapporto di interi")
f = 0.2
print(f, " = ", f.as_integer_ratio())

#assegando un nuovo valore a f si crea una nuova instanza di float

f1 = float(3.8)
print("Operatore +:", f1 + 4) #il + invoca il metodo __add__()
print("Metodo __add__:", f1.__add__(4)) #fa overloading del +