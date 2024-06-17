from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str,specializzazione:str,parcella:float):
        super().__init__(first_name, last_name)
        self.__specializzazione:str=specializzazione
        self.__parcella:float=parcella
        if type(specializzazione)!= str:
            self.__specializzazione= None
            print("L'attributo specializzazione deve essere una stringa!")
        if type(parcella)!=float:
            self.__parcella=None
            print("L'attributo parcella deve essere una float!")
    

    def setSpecialization(self,specialization):
        if type(specialization) == str:
            self.__specializzazione= specialization
        else:
            return f"La specializzazione inserita non è una stringa!"
    

    def setParcel(self,parcel):
        if type(parcel)== float:
            self.__parcella=parcel
        else:
            return f"La parcella deve essere un float!"


    def getSpecialization(self)-> str: 
        return self.__specializzazione
    


    def getParcel(self)-> str:
        return self.__parcella
    

    def isAValidDoctor(self)-> str:
        if self.getAge() > 30:
            print(f"Doctor {self.getName()} {self.getLastName()} is Valid!")
            return True
        else:
            print( f"Doctor {self.getName} {self.getLastName} is NOT Valid!")
            return False


    def doctorGreet(self)-> str:
         return self.greet() +  f"Sono un medico  {self.__specializzazione}"
    

        

    



        

    
    



    









        

        

    
        