class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


class Lavoratore:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "il lavoratore {}".format(self.nome)

    def lavora(self, lavoro):
        return "svolge il seguente {}".format(lavoro)


class Commesso:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Il commesso {}".format(self.nome)

    def vende(self, merce):
        return "vende {}".format(merce)


class Cuoco:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Il cuoco {}".format(self.nome)

    def cucina(self, pietanza):
        return "cucina {}".format(pietanza)


class Musicista:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Il musicista {}".format(self.nome)

    def suona(self, tipoMusica):
        return "suona {}".format(tipoMusica)


def main():
    objects = []
    musicista = Musicista('Veronica')
    commesso = Commesso('Paolo')
    cuoco = Cuoco('Antonio')
    objects.append(Adapter(musicista, dict(lavora=musicista.suona('musica pop'))))
    objects.append(Adapter(commesso, dict(lavora=commesso.vende('abiti'))))
    objects.append(Adapter(cuoco, dict(lavora=cuoco.cucina('una lasagna'))))

    for o in objects:
        print("{} {}".format(o.__str__(), o.lavora))


if __name__ == "__main__":
    main()
