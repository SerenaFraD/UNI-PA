#[TRCCIA]Creare un array di 20 numeri casuali. Creare una funzione sommario, che dice minimo, massimo, la media e la deviazione standard
#[SPIEGAZIONE] Ho creato una lista con i 20 valori da analizzare e un dizionario che contiene le coppie-valori che devono essere ritornati dalla funzione
#minimo e massimo sono inizializzati con il primo valore della lista così da non essere falsati da un valore di default come 0
#nel primo for calcolo la somma, il minimo e il massimo
#appena fuori calcolo la media dei valori come la divisione tra la somma dei valori e il numero totale di questi
#assegno a scartoQuadMed e rho un oggetto int() che le inizializza a 0, giusto per essere sicuri di non avere valori sporchi
#nel secondo for calcolo la scartoQuadMed = E(1 a N)(xi - media)^2
#in rho calcolo rho = scartoQuadMedio/N
#infine, calcolo la deviazione come rad(rho)
#ho fatto un piccolo troncamento a due cifre decimali usando trunc della classe math
#[SITO DA CUI HO PRESO LA FORMULA] https://www.okpedia.it/deviazione-standard-scarto-quadratico-medio

import math

l = [123, 45, 1, 23, 2, 67, 54, 65, 90, 345, 234, 0, 2, 43, 98, 87, 21, 12, 37, 678]
d = dict([('minimo', l[0]), ('massimo', l[0]), ('somma', 0), ('media', 0), ('deviazione', 0)]) #contiene tutti i valori di ritorno
DECIMALS = 2 #decimali dopo la virgola

def funzione(l, d):
    for i in range(0, len(l)):
        if(l[i] <= d['minimo']): #confronto il minimo
            d['minimo'] = l[i]

        if(l[i] >=  d['massimo']): #confronto il massimo
            d['massimo'] = l[i]
        
        d['somma'] += l[i] #calcolo la somma degli elementi

    factor = 10.0 ** DECIMALS
    #calcolo la media troncata a due cifre decimali
    d['media'] = math.trunc((d['somma'] / len(l)) * factor) / factor

    scartoQuadMed = int()
    rho = int()
    for i in range(0, len(l)):
       scartoQuadMed += (l[i] - d['media'])**2

    rho = scartoQuadMed / len(l)

    #calcolo di rho e troncamento a due delle cifre decimali (è un di più)
    d['deviazione'] = math.trunc((rho**(1/2)) * factor) / factor


#chiamata funzione: non toccare
funzione(l, d)
print("Valori calcolati:", d)