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
        for clienti in self.rented_film.keys():
            if clientID == clienti:
                self.rented_film[clientID].remove(film)
                self.film_list.append(film)
                penale=film.calcolaPenaleRitardo(days)
                print(f"il cliente: {clientID} deve pagare per il film: {film.getTitle()}  {penale} euro di penale!")


    


    def printMovies(self):
        for film in self.film_list:
            print(f"{film.getTitle()} - {film.getGenere()}")




    def     printRentMovies(self,clientID):
            for cliente in self.rented_film:
                if cliente == clientID:
                    print(f" I film noleggiati da {clientID} sono : {self.rented_film[clientID]}")





                

        


    