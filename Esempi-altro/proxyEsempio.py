class Implementation:
    def f(self):
        print("Sono f")

    def g(self):
        print("Sono g")

    def h(self):
        print("Sono h")


class Proxy:
    def __init__(self):
        self.__implementation = Implementation()

    def f(self):
        self.__implementation.f()

    def g(self):
        self.__implementation.g()

    def h(self):
        self.__implementation.h()

def main():
    p = Proxy()
    p.f()
    p.g()
    p.h()


if __name__ == "__main__":
    main()
