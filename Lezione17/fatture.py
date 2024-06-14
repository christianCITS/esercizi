from paziente import Paziente
from dottore import Dottore

class Fattura:
    def __init__(self,patient:list[Paziente],doctor:Dottore):
        self.lista_pazienti:list[Paziente]=patient
        self.doctor:Dottore=doctor
        if doctor.isAValidDoctor()== True:
            self.fatture:int=len(self.lista_pazienti)
            self.salary:int=0
        else:
            self.lista_pazienti=None
            self.doctor=None
            self.fatture=None
            self.salary=None
            print(f"Non è possibile creare la classe fattura poichè il dottore non è valido!")



    def getSalary(self):
        self.salary:int=self.doctor.getParcel*len(self.lista_pazienti)
        return self.salary
    

    def getFatture(self): 
        self.fatture=len(self.lista_pazienti)



            





        

        







        