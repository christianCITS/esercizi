from abc import ABC
from abc import abstractmethod


class CodificatoreMessaggio:
    @ abstractmethod
    def codifica(self,testoInChiaro):
        self.testoInChiaro=testoInChiaro



class DecodificatoreMessaggio:
    
    def decodifica(self,testoCodificato):
        pass