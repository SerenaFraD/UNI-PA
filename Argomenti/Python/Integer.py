# Classe Int
# Int -> classe di tipo immutable

print("Uso del costruttore int() vuoto e con 1")
i = int()  # restituisce 0 di default
print('La variabile i vale', i)

i = int(1)  # valore restituito 1
print('La variabile i vale', i)

print('\nCreazione di interi a partire da stringhe')
print("Conversione della stringa 23 in base 4")
i = int("23", base=4)  # funziona solo con stringhe di numeri
print('La variabile i vale', i)
