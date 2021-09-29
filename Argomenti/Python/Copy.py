# Differenze tra shallow copy e deep copy
# shallow -> nuovo oggetto e inserisce i riferimenti agli oggetti nell'originale

print("Shallow Copy")
l1 = ['a', 'b', ['ab', 'ba']]
l2 = l1.copy()  # shallow copy
print("Lista ", l1)
print("Lista copia ", l2)

l2[0] = 'c'
l2[2][1] = 'd'  # secondo elemento della lista
print("Lista ", l1)
print("Lista copia ", l2)  # da problemi con la modifica della lista interna

print("\nDeeepCopy")
from copy import deepcopy

l1 = ['a', 'b', ['ab', 'ba']]
l2 = deepcopy(l1)  # deep copy
print("Lista ", l1)
print("Lista copia ", l2)

l2[0] = 'c'
l2[2][1] = 'd'  # secondo elemento della lista
print("Lista ", l1)
print("Lista copia ", l2)  # no problemi con la modifica della lista interna
