from myPair import MyPair


class MyDictionary:
    def __init__(self, *args):
        if args:
            self.pairs = []
            for arg in args:
                self.pairs.append(arg)
        else:
            self.pairs = []

    def pairs(self):
        return self.pairs

    def __getitem__(self, key):  # lancia KeyError
        for pair in self.pairs:
            if key == pair.getKey():
                return pair.getValue()
        raise KeyError(key)

    def __setitem__(self, key, value):
        for pair in self.pairs:
            if key == pair.getKey():
                pair.setValue(value)
                return
        self.pairs.append(MyPair(key, value))

    def __delitem__(self, key):
        for pair in self.pairs:
            if key == pair.getKey():
                self.pairs.remove(pair)
                return
        raise KeyError(key)

    def __contains__(self, key):
        for pair in self.pairs:
            if key == pair.getKey():
                return True
        return False

    #per equals uso il built in di python per il confronto tra liste

    def __ne__(self, myDict):
        return not self.__eq__(MyDictionary)

    def __str__(self):
        toReturn = '{'
        for pair in self.pairs:
            toReturn += str(pair)
        toReturn += '}'
        return toReturn


if __name__ == '__main__':
    print("Instanzio un oggetto d di tipo MyDict vouto")
    d = MyDictionary()
    print("d=", d, end="\n\n")

    print("Aggiungo un elemento a d, chiave= 'a', valore= 1")
    d['a'] = 1
    print("d=", d, end="\n\n")

    print("Aggiungo un elemento a d, chiave= 'b', valore= 2")
    d['b'] = 2
    print("d=", d, end="\n\n")

    print("Aggiungo un elemento a d, chiave= 'c', valore= 3")
    d['c'] = 3
    print("d=", d, end="\n\n")

    print("Modifico la coppia con chiave= 'b', setto il valore= 12")
    d['b'] = 12
    print("d=", d, end="\n\n")

    print("Cancello la coppia con chiave= 'b'")
    del d['b']
    print("d=", d, end="\n\n")

    print("È presente una coppia con chiave= 'b'?", 'b' in d, "aspettato: False")

    print("È presente una coppia con chiave= 'a'?", 'a' in d, "aspettato: True")

    print("Non è presente una coppia con chiave= 'b'?", not 'b' in d, "aspettato: True", end="\n\n")

    print("Creo un nuovo dizionario f con le stesse coppie presenti in d")
    p1 = MyPair('a', 1)
    p2 = MyPair('c', 3)
    f = MyDictionary(p1, p2)
    print('f=', f, end="\n\n")

    print("f=", f, "e d=", d, "sono uguali?",
          d == f,
          "aspettato: True", end="\n\n")

    print("modifico la coppia con chiave= 'a' di f con un valore= 11")
    f['a'] = 11
    print('f=', f, end="\n\n")
    print("f=", f, "e d=", d, "sono uguali?", d == f, "aspettato: False", end="\n\n")
