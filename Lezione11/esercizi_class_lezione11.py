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
            print(f"la sala numero {}")
            

    def prenota_film(self,titolo_film:str,num_posti:int):
        for s in self.lista_sale:
            if titolo_film == s.film_progr.titolo

                







        











cinema=Cinema()
film1=Film("titolo_film",120)
sala1=Sala(1,film1,100,0)
cinema.aggiungi_sala(sala1)
print(sala1.posti_disponibili())
print(sala1.prenota_posti(10))
print(sala1.posti_disponibili())