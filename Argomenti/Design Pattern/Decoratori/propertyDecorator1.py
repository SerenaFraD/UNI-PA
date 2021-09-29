import numbers


# è un factory function che restituisce una funzione
def is_in_range(minimum=None, maximum=None):
    assert minimum is not None or maximum is not None

    def is_in_range(name, value):
        if not isinstance(value, numbers.Number):
            raise ValueError("{} must be a number".format(name))

        if minimum is not None and value < minimum:
            raise ValueError("{} {} is too small".format(name, value))

        if maximum is not None and value > maximum:
            raise ValueError("{} {} is too big".format(name, value))

    return is_in_range


def is_not_empty_str(name, value):
    if not isinstance(value, str):
        raise ValueError("{} must be of type str".format(name))

    if not bool(value):
        raise ValueError("{} may not be empty".format(name))


def ensure(name, validate, doc=None):
    def decorator(Class):
        privateName = "__" + name + "__"

        def getter(self):
            return getattr(self, privateName)

        def setter(self, value):
            validate(name, value)
            setattr(self, privateName, value)

        setattr(Class, name, property(getter, setter, doc=doc))
        return Class

    return decorator


def is_valid_isbn(name, value):
    pass


if __name__ == '__main__':
    # decorator factory -> una funzione he restiruisce un decoratore
    @ensure("title", is_not_empty_str)  # 4
    @ensure("isbn", is_valid_isbn)  # 3
    @ensure("price", is_in_range(1, 10000))  # 2
    @ensure("quantity", is_in_range(0, 100000))  # 1 ordine applicazione
    class Book:
        def __init__(self, title, isbn, price, quantity):
            self.title = title
            self.isbn = isbn
            self.price = price
            self.quantity = quantity

        @property
        def value(self):
            return self.price * self.quantity


    gg = Book("The Great Gatsby", "", 9, 200)
    ddd = Book("Dance, dance, dance", "", 12, 201)

    ddd.price = 15
    print(ddd.value)
    print(ddd.price)
    print(ddd.__dict__)
