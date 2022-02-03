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

    def __getattr__(self, name):
        return getattr(self.__implementation, name)

def main():
    p = Proxy()
    p.f()
    p.g()
    p.h()


if __name__ == "__main__":
    main()
