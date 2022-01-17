from typing import Collection


class Pacco():
    ORDINATO, SPEDITO, RICEVUTO = ("ORDINATO", "SPEDITO", "RICEVUTO")

    def __init__(self):
        self.state = Pacco.ORDINATO
        self.callbacksForEvents = Collection.defaultdict(list)





def main():
	print("\nCreo il pacco")
	pacco=Pacco()
	pacco.stampaStato()
	print("\nInoltro il pacco all'ufficio postale")
	pacco.next()
	pacco.stampaStato()
	print("\nConsegno il pacco al destinatario")
	pacco.next()
	pacco.stampaStato()
	print("\nProvo a passare ad uno stato successivo")
	pacco.next()
	pacco.stampaStato()

if __name__== "__main__":
	main()


"""Il  programma deve stampare:
Creo il pacco
Il pacco e` stato ordinato ma non ancora spedito

Inoltro il pacco all'ufficio postale
Il pacco e` stato spedito ma non ancora ricevuto

Consegno il pacco al destinatario
Il pacco e` stato ricevuto 

Provo a passare ad uno stato successivo
Il pacco e` gia` stato ricevuto
Il pacco e` stato ricevuto 
"""