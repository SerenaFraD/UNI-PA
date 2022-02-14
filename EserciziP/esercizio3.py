# Definire un decoratore di classe che permette alla classe decorata di
# contare le sue istanze.
def conta(cls):
    cls.istanze = 0

    return cls

@conta
class Classe:
    def __init__(self):
        Classe.istanze += 1

@conta
class Classe2(Classe):
    def __init__(self):
        Classe2.istanze += 1


c = Classe()
d = Classe()
e = Classe2()
f = Classe2()
g = Classe2()
print(Classe.istanze)
print(Classe2.istanze)
