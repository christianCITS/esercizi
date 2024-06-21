from film import Film
from movie_genre import Azione, Commedia,Drama

class Noleggio:
    def __init__(self,film_list:list[Film]):
        self.film_list:list[Film]=film_list
        self.rented_film:dict[int,list[Film]]={}




    def isAvaible(self,film:Film): 
            if film in self.film_list:
                print(f"il film scelto è disponibile: {film.getTitle()}")
                return True
                
            else:
                print(f"il film scelto NON è disponibile: {film.getTitle()}")
                return False
            


    def rentAmovie(self,film:Film,clientID:int):
        if film not in self.film_list:
            print(f"Il film non è disponibile per il noleggio!: {film.getTitle()}")
        if clientID not in self.rented_film:
           film_noleggiati:list[Film]=[]
           self.film_list.remove(film)
           film_noleggiati.append(film)
           self.rented_film[clientID]=film_noleggiati
           print(f"il cliente {clientID} ha potuto noleggiare il film: {film.getTitle()}")
        else:
            self.rented_film[clientID].append(film)
            print(f"il cliente {clientID} ha noleggiato un altro  film: {film.getTitle()}")



    
    def giveBack(self,film:Film, clientID, days):
        for fil in self.rented_film.items():
            

 
 
 
 
    #questo metodo consente di restituire un film noleggiato in negozio, ed ha come argomenti il film da restituire, 
    # il codice ID del client che restituisce il film, il numero dei giorni in cui il cliente ha tenuto il film per se.  
    # Il film da restituire deve essere rimosso dalla lista dei film noleggiati dal cliente con id clientID, e tale film, 
    # deve essere riaggiunto alla lista dei film disponibili in negozio (film_list). Successivamente, 
    # il metodo deve calcolare la penale che il cliente deve pagare utilizzando l'opposito metodo. 
    # Stampare la penale che il cliente deve pagare: "Cliente: {clientID}! La penale da pagare per il film {titolo_film} 
    # e' di {tot} euro!".







                


film1 =Azione(112,"Inception")
film2 = Azione(111,"Interstellar")
noleggio = Noleggio([film1,film2])
print(noleggio.film_list)


noleggio.rentAmovie(film1,112)
noleggio.rentAmovie(film2,112)



print(noleggio.rented_film)

noleggio.giveBack(film1,112,3)


                

        


    