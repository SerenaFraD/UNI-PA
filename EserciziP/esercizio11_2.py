# Scrivere la funzione ricorsiva myDeepCopy che prende in input una lista
# che potrebbe contenere al suo interno elementi di tipo lista che a loro
# volta potrebbero contenere elementi di tipo lista, e cosi` via. La funzione
# restituisce la deep copy della lista


def funzione(lista: list, copia: list):
    return ricorsiva(lista, copia, len(lista)-1)

def ricorsiva(lista: list, copy: list, index: int):
    if index == -1:
        return copy
    else:
        if isinstance(lista[index], list):
            tmp = list()
            tmp = ricorsiva(lista[index], tmp, len(lista[index])-1)
            copy.append(tmp)

        if not isinstance(lista[index], list):
            copy.append(lista[index])

        index -= 1
        return ricorsiva(lista, copy, index)


copy = list()
print(funzione([1, 2, 3, 4, [5, 6], [7, [8, 9], 10]], copy))
