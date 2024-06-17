from paziente import Paziente
from dottore import Dottore

class Fattura:
    def __init__(self,patient:list[Paziente],doctor:Dottore):
        self.doctor:Dottore=doctor
        if doctor.isAValidDoctor()== True:
            self.salary:int=0
            self.lista_pazienti=patient
            self.fatture:int=len(self.lista_pazienti)

        else:
            self.lista_pazienti=None
            self.doctor=None
            self.fatture=None
            self.salary=None
            print(f"Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def __str__(self) -> str:
             return f"pazienti: {self.lista_pazienti}"
            

    def getSalary(self):
        self.salary:int=self.doctor.getParcel()*len(self.lista_pazienti)
        return self.salary
    

    def getFatture(self): 
        self.fatture=len(self.lista_pazienti)
        return self.fatture
    

    def addPatient(self,newPatient:Paziente):
        if newPatient not in self.lista_pazienti:
            self.lista_pazienti.append(newPatient)
            print(f"Alla lista del Dottor cognome è stato aggiunto il paziente {newPatient.getIdCode}")


    def removePatient(self,idCode:str):
        for paziente in self.lista_pazienti:
            if paziente.getIdCode()== idCode:
                self.lista_pazienti.remove(paziente)
                print(f"Alla lista del Dottor cognome è stato rimosso il paziente {idCode}")




dottore1=Dottore("Albus","Silente","Ginecologo",900.99)
dottore1.setAge(70)
paziente1=Paziente("LUisa","adfg","G14C0")
paziente2=Paziente("Marina","qewtrqrr","M4r1")
paziente3=Paziente("Giuseppa","sgfssds","G1US")
paziente4=Paziente("Alfonsa","gkjhgkj","4lf0")
fattura=Fattura([paziente1,paziente2,paziente3],dottore1)


print(fattura.getFatture())

fattura.addPatient(paziente4)
fattura.removePatient("G1US")
print(fattura.getSalary())













        
                

        

    




            





        

        







        