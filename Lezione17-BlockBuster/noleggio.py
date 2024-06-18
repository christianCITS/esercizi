from film import Film

class Noleggio:
    def __init__(self):
        self.film_list:list[str]=[]
        self.rented_film:dict[int,list[str]]={}




    def isAvaible(self,film:Film): 
        for _ in self.film_list:
            if film.getTitle() in self.film_list:
                print(f"il film scelto è disponibile: {film.getTitle()}")
                return True
            else:
                print(f"il film scelto NON è disponibile: {film.getTitle()}")
                return False
            


    def rentAmovie(self,film:Film,clientID:int):
        film_noleggiati:list[Film]=[]
        for _ in self.film_list:
            if film not in self.film_list:
                print(f"Il film non è presente nel negozio!")
            else:
                self.film_list.remove(film)
                film_noleggiati.append(film)
                self.rented_film[clientID]=film_noleggiati
                print(f"il cliente ha potuto noleggiare il film: {film.getTitle()}")

                

        


    