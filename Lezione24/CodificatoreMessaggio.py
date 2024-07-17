from abc import ABC
from abc import abstractmethod


class CodificatoreMessaggio(ABC):
    @ abstractmethod
    def codifica(self,testoInChiaro):
        pass



class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self,testoCodificato):
        pass


class CifratoreAScorrimento(CodificatoreMessaggio,DecodificatoreMessaggio):
    def __init__(self,chiave:int):
        super().__init__()
        self.chiave=chiave
    
    def decodifica(self, testoCodificato):
        pass
    
        





    def codifica(self, testoInChiaro):
        diz:dict={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
        passo:int=self.chiave
        d:str=""
        
        for i in testoInChiaro:
            for k,v in diz.items():
                if i==v:
                    e:int=k+passo
                    d+=diz[e]
        return d

                
            


ci=CifratoreAScorrimento(4)
print(ci.codifica("ciao"))