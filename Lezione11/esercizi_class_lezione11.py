"""Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato."""



from typing import Any


class Film:

    def __init__(self,titolo:str,durata:int):
        self.titolo:str=titolo
        self.durata:int=durata




class Sala:
    def __init__(self,num_sala:int,film_progr:str,post_disp:int,post_pren:int):
        self.num_sala:int=num_sala
        self.film_progr:str=film_progr
        self.post_disp:int=post_disp
        self.post_pren:int=post_pren
    




    def posti_disponibili(self):
       if self.post_pren != None:
           a:int=self.post_disp - self.post_pren
           return a
       else:
           return self.post_disp

        

    def prenota_posti(self,posti_da_pren:int):

        if posti_da_pren > self.post_disp:
            return(f"Siamo spiacenti, la sala è al completo!")
        else:
            self.post_disp= self.post_disp - posti_da_pren
            return (f"la prenotazione di {posti_da_pren} è stata eseguita!")
            



class Cinema():
    def __init__(self):
        self.lista_sale:list[Sala]=[]

    def aggiungi_sala(self,new_sala:Sala):
        if new_sala not in self.lista_sale:
            self.lista_sale.append(new_sala)
        else:
            print(f"la sala numero {new_sala} non può essere aggiunta poichè esiste già!")
            

    def prenota_film(self,titolo_film:str,num_posti:int):
        for s in self.lista_sale:
            if titolo_film == s.film_progr.titolo and num_posti <= s.post_disp:
                s.post_disp-=num_posti
                print(f"I biglietti sono stati prenotati per il film: {titolo_film} e il numero di biglietti prenotati è: {num_posti}")

            elif titolo_film!= s.film_progr:
                print(f"Siamo spiacenti il film non è diponibile")
            




'''Gestione di un magazzino
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, 
cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.'''


class Prodotto:
    def __init__(self,nome:str,quant:int):
        self.nome:str=nome
        self.quant:int=quant

    def __str__(self):
        return f"{self.nome},(quant: {self.quant})"



class Magazzino:
    def __init__(self):
        self.lista_prodotti:list[Prodotto]=[]






    def aggiungi_prodotto(self,prodotto:Prodotto):
        if prodotto not in self.lista_prodotti:
            self.lista_prodotti.append(prodotto)
            print(f"il prodotto: {prodotto} è stato aggiunto correttamente nel magazzino!")

    
    def cerca_prodotto(self,nome: str)-> Prodotto:
        for prod in self.lista_prodotti:
            if nome == prod.nome:
                return prod
        
        return f"Il prodotto che cerchi non è in magazzino!" 
        
    
    def verifica_disponibilità(self,nome: str) -> str:
        for prod in self.lista_prodotti:
            if nome == prod.nome:
                return f" Il prodotto che cerchi è disponibile in queste quantità: {prod}"
        
        return f"Il prodotto che cerchi NON è DISPONIBILE!"


    
    
    
    
    





