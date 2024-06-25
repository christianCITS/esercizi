class Film:
    def __init__(self,codiceID:int,title:str):
        self.__codiceID=codiceID
        self.__title=title



    
    def setID(self,id):
        if id != self.__codiceID:
            self.__codiceID= id
    

    def setTitle(self,title):
        if title != self.__title:
            self.__title=title
    
    def getId(self):
        return self.__codiceID
    
    def getTitle(self):
        return self.__title
    

    def isEqual(self,otherFilm:"Film"):
        if self.__codiceID== otherFilm.getId():
            return True
        else:
            return False
    








    


    

        
