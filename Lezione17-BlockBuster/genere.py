from film import Film



class Azione(Film):
    def __init__(self,codiceID: int, title: str, genere:str,penale:float):
        super().__init__(codiceID, title)
        self.__genere="Azione"
        self.__penale=3.0
    

    def getGenere(self):
        return self.__genere
    

    def getPenale(self):
        return self.__penale
    


    def calcolaPenaleRitardo(), che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.






class Commedia(Film):

    pass




class Drama(Film):


    pass
