from abc import ABC,abstractmethod

class Volo:

    def __init__(self,codiceVolo:str,CapMaxPosti:int):
        self.codiceVolo=codiceVolo
        self.CapMaxPosti=CapMaxPosti
        self.prenotazioni=0
        

    @abstractmethod
    def prenotaPosto():
        pass
    
    
    def postiDisponibili():
        pass




class VoloCommerciale(Volo):
     def __init__(self, codiceVolo: str, CapMaxPosti: int):
         super().__init__(codiceVolo, CapMaxPosti)
         diz:dict[str,float]={"Posti disponibili: ":self.CapMaxPosti,"Classe economica: ":self.CapMaxPosti*70/100,"Classe business: ":self.CapMaxPosti*20/100,"prima classe: ":self.CapMaxPosti*10/100}
         self.prenotaClasseEco=0
         self.prenotaClasseBus=0
         self.prenotaPrimaClasse=0

        
