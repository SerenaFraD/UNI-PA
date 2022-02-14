class C:
    @classmethod
    def aggiungiProprieta(cls):
        def setter(self, val):
            if isinstance(val, str):
                getattr(cls, self)
                setattr(cls, privateName, val)
                print(privateName)
            else:
                raise TypeError("Non e`possibile assegnare {} alla variabile {}".format(val, privateName))
            setattr(cls, key, property(getter, setter, doc=None))


C.x = 2
C.y = "a"
C.z = "b"
C.w = (1, 2)

C.aggiungiProprieta()
c = C()
print("c e` un'istanza della classe C che ha le variabili di classe x di tipo int,y e z di tipo str, e w di dipo tuple")
try:
    c.z = "anna"
    print("c.z={}. Tutto ok.".format(c.z))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    c.x = [1, 2]
    print("c.x={}. Tutto ok.".format(c.x))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    c.y = 3
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")


class D(C):
    n = "u"


print("\nLa classe D ha come classe base C e, oltre alle variabili di classe di D, ha la variabile n di tipo str")
D.aggiungiProprieta()
print("d e` un'istanza della classe D. ")

d = D()
try:
    d.z = "anna"
    print("d.z={}. Tutto ok.".format(d.z))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    d.x = [1, 2]
    print("d.x={}. Tutto ok.".format(d.x))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    d.y = 3
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")

try:
    d.n = 3
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")

print("\nOra assegnamo a D variabili di classe omonime a quelle di C ma con valori diversi")
D.x = "papera"
D.y = 11
D.z = [1, 2, 3]
D.w = "airone"

D.aggiungiProprieta()
d = D()
try:
    d.z = set((1, 4))
    print("d.z={}. Tutto ok.".format(d.z))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    d.x = [1, 2]
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")

try:
    d.w = "pop"
    print("d.w={}. Tutto ok.".format(d.w))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    d.w = 6
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")

try:
    d.n = 3
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")

"""
Il programma deve stampare:
c e` un'istanza della classe C che ha le variabili di classe x di tipo int,y e z di tipo str, e w di dipo tuple
c.z=anna. Tutto ok.
c.x=[1, 2]. Tutto ok.
Non e` possibile assegnare 3 alla variabile y ed e` corretto che sia cosi`

La classe D ha come classe base C e, oltre alle variabili di classe di D, ha la variabile n di tipo str
d e` un'istanza della classe D. 
d.z=anna. Tutto ok.
d.x=[1, 2]. Tutto ok.
Non e` possibile assegnare 3 alla variabile y ed e` corretto che sia cosi`
Non e` possibile assegnare 3 alla variabile n ed e` corretto che sia cosi`

Ora assegnamo a D variabili di classe omonime a quelle di C ma con valori diversi
d.z={1, 4}. Tutto ok.
Non e` possibile assegnare [1, 2] alla variabile x ed e` corretto che sia cosi`
d.w=pop. Tutto ok.
Non e` possibile assegnare 6 alla variabile w ed e` corretto che sia cosi`
Non e` possibile assegnare 3 alla variabile n ed e` corretto che sia cosi`

"""""
