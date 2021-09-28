#Comprehension -> construtto sintattico per la creazione di una iterable a partire
#da un altro iterable

#fa il quadrato per tutte le k presenti nel range 1 - 10
squares = [k * k for k in range(1, 11)]
print("List ", squares)

#Doppia comprehension
a = [(x, y) for x in [1, 2, 3] for y in ['a', 'b', 'c']]
print("Lista ", a)
