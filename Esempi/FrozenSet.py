#Class Dict
#Classe dict -> coppie (chiave, valore)
#chiave -> immutabile e distinte

d = {} #dizionario vuoto
print("Dict ", d)
d = {'ga':'Irish', 'de':'German'} #tipo 1 costruttore
print("Dict ", d)
d = {}
pairs = [('ga', 'Irish'), ('de', 'German')] 
d = dict(pairs) #tipo2 con uso di una lista pairs
print("Dict ", d)

print("\nAggiunta di una coppia")
d['it'] = 'Italian' #aggiunge un elemento di chiave 'it'
print("Dict ", d)
d['en'] = 'Italian' #aggiunge una coppia di chiave con valore 'Italian', no problem
print("Dict ", d)

d['it'] = 'Spanish' #se la chiave è già presente, ne cambia il valore
print("Dict ", d)

print("\nEliminazione")
del d['it']
print("Dict ", d)

print("\nPrelevo le chiavi")
key = d.keys() #restituisce solo le chiavi
print("Le chiavi ", key)

print("\nPrelevo gli elementi")
value = d.values() #restituisce valore
print("Gli elementi ", value)

print("\nIterazione sugli elementi")
elementi = d.items() #restituisce le coppie
for k, v in elementi: #chiave k e valore v
    print("Chiave ", k, " Valore ", v)

print("\nIterazione sulle chiavi")
for k in d.keys():
    print("Chaive ", k)


print("\nCopy")
d1 = d.copy() #copia superficiale shallow
print("Copia dict ", d1)

print("\nGet")
value = d.get('en') #restiruisce il valore di un chiave presente
print("Value ", value)

value = d.get('it') #chiave non presente, restiruisce None
print("Value ", value)

print("\nPop")
value = d.pop('en') #elimina la chiave e restituisce il valore, chiave presente
print("Value ", value)
try:
    value = d.pop('it') #chiave non presente, restiruisce eccezione.
except Exception as e: 
    print(e) #Nell'eccezione c'è la chiave passata

print("\nUpdate")
l = [('ga', 'American')] #sovrascrive la coppia con chiave k
d.update(l) #accetta un dizionario o un oggetto iterabile
print("Dict ", d)

print("\nClear")
d.clear() #elimina tutti gli elementi
print("Dict ", d)
