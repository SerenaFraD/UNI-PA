class StranaTupla(tuple):
    def __new__(self, lista: list):
        tmp = []
        for i in range(0, len(lista)):
            if (i % 2) == 0:
                tmp.append(lista[i])

        self.tupla = tuple(tmp)
        return self.tupla


s = StranaTupla(['a', 'h', 5, 'dado', 4])
print(s)
