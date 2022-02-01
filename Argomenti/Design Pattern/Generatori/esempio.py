# Esempio slides raddoppio
def raddoppio():
    while True:
        x = yield
        x = yield x * 2


g = raddoppio()
r = next(g)
if r is None:
    print("niente")
r = g.send(5)
print("r = {}". format(r))
r = next(g)
if r is None:
    print("niente")
r = g.send(8)
print("r = {}". format(r))
