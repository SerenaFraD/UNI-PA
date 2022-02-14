# Scrivere una funzione ricorsiva che prende in input una lista e un
# elemento x. La funzione restituisce True non appena trova x nella lista. Se
# x non e` nella lista, la funzione restituisce False

def funzione(lista: list, x: int):
    return ricorsiva(lista, x, len(lista)-1)

def ricorsiva(lista: list, x: int, index: int):
    if index < 0:
        return False
    else:
        if lista[index] == x:
            return True
        else:
            index -= 1
            return ricorsiva(lista, x, index)


print(funzione([1, 2, 3, 4, 5, 6, 7], 10))
print(funzione([1, 2, 3, 4, 5, 6, 7], 5))
