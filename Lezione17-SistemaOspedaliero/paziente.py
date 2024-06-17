from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str,codice:str):
        super().__init__(first_name, last_name)
        self.__codice:str=codice

    def setIdCode(self,idCode:str):
        if type(idCode)== str:
            self.__codice=idCode
        else:
            return f"Il codice id deve essere una stringa!"
    


    def getIdCode(self):
        return self.__codice
    



    def patientInfo(self):
        print(f"Paziente: {self.getName()} \nID: {self.getIdCode()}")




paziente=Paziente("Alby","Bak","T1F4")
paziente1=Paziente("bob","Bik","RE8E")
paziente2=Paziente("clerk","Bok","")
paziente3=Paziente("fil","Buk","T1F4")
paziente4=Paziente("sil","Bek","T1F4")
paziente5=Paziente("giov","Btk","T1F4")










        
        
