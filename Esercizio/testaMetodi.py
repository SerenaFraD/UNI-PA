# Scrivere nel file testaMetodi il codice per testare il codice dei due moduli.
# Il codice deve eseguire (nell’ordine) quanto descritto di seguito:
# 1. effettuare 3 invocazioni di print_x per stampare nomi delle tre classi e i valori di x nelle tre classi
# 2. effettuare 2 invocazioni di modifica_x per modificare x di Base e Der1 (scegliete voi i
#    nuovi valori purche’ diversi tra loro e dai precedenti)
# 3. effettuare di 3 invocazioni di print_x per stampare nomi delle tre classi e i valori di x nelle tre classi
# 4. effettuare un’invocazione di modifica_x per modificare x di Der2 (scegliete voi il nuovo valore purche’ diverso dagli altri gia` usati)
# 5. effettuare 3 invocazioni di print_x per stampare nomi delle tre classi e i valori di x nelle tre classi
# 6. effettuare un’invocazione di ciascuno dei 6 metodi di Der2

from Esercizio.moduloBase import Base
from Esercizio.moduloDer1Der2 import Der1, Der2

b = Base()
d1 = Der1()
d2 = Der2()

b.print_x()
d1.print_x()
d2.printNormale()

b.modifica_x("__bho1__")
d1.modifica_x("__bho2__")

b.print_x()
d1.print_x()
d2.printNormale()

d2.modifica_x("__bho3__")

b.print_x()
d1.print_x()
d2.printNormale()

d2.printClass()
d2.printClass2()
d2.printNormale()
d2.printNormale2()
d2.printStatic()
d2.printStatic2()
