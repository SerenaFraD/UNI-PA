# Funzioni classe Bool
# Bool -> classe tipo immutable

b = bool() # assegna False di default
if b == False:
    print('La variabile b vale', b)
else:
    print('La variabile b vale ', b)

print('\nCreazione di valori booleani a partire da altri tipi')
b = bool(0) # b vale False
print('Valore 0 -> la variabile b vale', b)
b = bool(1) # b vale True
print('Valore 1 -> la variabile b vale', b)
