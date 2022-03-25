import functools
import re


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper

@coroutine
def find(w, c):
    while True:
        testo = (yield)

        print(testo)
        if testo is not None:
            pass
            #for parola in re.findall(r'\w+', testo):
            #    if parola[0:1] == c:
            #        try:
            #            w.send(parola)
            #        except StopIteration:
            #            break

@coroutine
def write(file_name):
    while True:
        parola = (yield)
        file = open(file_name, "a")
        file.write("{} ".format(str(parola)))


def function(matchers, testi):
    print(matchers)
    try:
        for t in testi:
            matchers.send(t)
    finally:
        for m in matchers:
            m.close()


matchers = [find(write("file_c"), "c"), find(write("file_s"), "s")]
testi = (
    "Ci curiamo tanto ma siamo come brutti cani",
    "Siamo sereni fino al successivo temporale"
)

function(matchers, testi)
