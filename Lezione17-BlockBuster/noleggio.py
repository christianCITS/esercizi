from film import Film

class Noleggio:
    def __init__(self,film_list:list[Film]):
        self.film_list:list[Film]=film_list
        self.rented_film:dict[int,list[Film]]={}




    def isAvaible(self,film:Film): 
        for _ in self.film_list:
            if film in self.film_list:
                print(f"il film scelto è disponibile: {film.getTitle()}")
                return True
                
            else:
                print(f"il film scelto NON è disponibile: {film.getTitle()}")
                return False
            


    def rentAmovie(self,film:Film,clientID:int):
        film_noleggiati:list[Film]=[]
        for _ in self.film_list:
            if film not in self.film_list:
                print(f"Il film non è disponibile per il noleggio!: {film.getTitle()}")
            else:
                self.film_list.remove(film)
                film_noleggiati.append(film)
                self.rented_film[clientID]=film_noleggiati
                print(f"il cliente {clientID} ha potuto noleggiare il film: {film.getTitle()}")
                


film1 = Film(112,"Inception")
film2 = Film(111,"Interstellar")
noleggio = Noleggio([film1,film2])
#print(noleggio.film_list)


noleggio.rentAmovie(film1,112)
noleggio.rentAmovie(film2,112)






                

        


    