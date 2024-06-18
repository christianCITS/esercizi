from film import Film



class Azione(Film):
    def __init__(self,codiceID: int, title: str):
        super().__init__(codiceID, title)
        self.__genere:str="Azione"
        self.__penale:float=3.0
    

    def getGenere(self):
        return self.__genere
    

    def getPenale(self):
        return self.__penale
    


    def calcolaPenaleRitardo(self,numero_giorni:int):
        penale_calcolo:float=numero_giorni* self.__penale
        return penale_calcolo
         






class Commedia(Film):
    def __init__(self,codiceID: int, title: str):
        super().__init__(codiceID, title)
        self.__genere:str="Commedia"
        self.__penale:float=2.5
    

    def getGenere(self):
        return self.__genere
    

    def getPenale(self):
        return self.__penale
    


    def calcolaPenaleRitardo(self,numero_giorni:int):
        penale_calcolo:float=numero_giorni* self.__penale
        return penale_calcolo






class Drama(Film):
    def __init__(self,codiceID: int, title: str):
        super().__init__(codiceID, title)
        self.__genere:str="Drama"
        self.__penale:float=2.0
    

    def getGenere(self):
        return self.__genere
    

    def getPenale(self):
        return self.__penale
    


    def calcolaPenaleRitardo(self,numero_giorni:int):
        penale_calcolo:float=numero_giorni* self.__penale
        return penale_calcolo
