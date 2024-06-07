class Media:
    def __init__(self):
        self.title=None
        self.reviews:list[int]=[]


    def set_title(self, title:str):
        self.title:str= title
    
    

    def get_title(self):
        return self.title
    


    def aggiungiValutazione(self,voto:int):
        if 0 < voto <= 5:
            self.reviews.append(voto)
            return (self.reviews)



    def getMedia(self):
        return round(sum(self.reviews) / len(self.reviews),2)
    



    def  getRate(self):
        f:int=self.getMedia()
        if 1 <=  f  <= 1.9:
            return f"TERRIBILE"
        if 2 <= f <= 2.9:
            return f"BRUTTO"
        if 3 <= f <=3.9:
            return f"NORMALE"
        if 4 <= f <= 4.9:
            return f"BELLO"
        if 5 <= f <= 5.9:
            return f"GRANDIOSO"
        


    
    def ratePercentage(self, voto:int):
        cont=0 
        for i in self.reviews:
            if i ==voto:
                cont+=1
        return cont /len(self.reviews)*100
    


    def recensione(self):
        return f"{self.title}, \nIl voto medio è: {self.getMedia()}, \n{self.getRate()}"



class Film(Media):

    def __init__(self,title:str=None):
        super().__init__()
        self.set_title(title)



film=Film()
film.set_title("filmone")
film.aggiungiValutazione(4)
film.aggiungiValutazione(5)
film.aggiungiValutazione(4)

print(film.recensione())
