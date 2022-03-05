class Singleton:
    class __impl:
        __slots__ = {'nome', 'cognome', 'eta'}

    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = Singleton.__impl()
        self.__dict__['_Singelton__instance'] = Singleton.__instance

    def __getattr__(self, attr):
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)

    __instance = None


if __name__ == "__main__":
    s = Singleton()
    s.nome = "pincopallino"
    print(s.nome)
    try:
        s.prova = "prova"
        print(s.prova)
    except:
        print("Non è possibile modificare questo valore")

    x = Singleton()
    print(x.nome)
