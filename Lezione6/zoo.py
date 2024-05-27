
#Christian Cioeta progetto zoo.py 14/05/2024

class Zoo:

    _instance=None
    @staticmethod
    def get_instance()->object:
        if Zoo._instance is None:
            Zoo()
        return Zoo._instance

    def __init__(self,fences:list["Fence"],zookeeper:list["Zookeeper"]):
        if Zoo._instance is not None:
            raise Exception("Non può esistere più di uno zoo.")
        else:
            Zoo._instance=self
            self.set_fences(fences)                                                                     
            self.set_zookeeper(zookeeper)
            
        
        

    def set_fences(self,fences:list["Fence"]):
        self.fences=fences
        

    def set_zookeeper(self,zookeeper:list["Zookeeper"]):
        self.zookeeper=zookeeper
    

    def get_fences(self)->list["Fence"]:
        return self.fences
    

    def get_zookeeper(self)->list["Zookeeper"]:
        return self.zookeeper
    @staticmethod
    def find_animal(animal:"Animal")->"Fence": 
        v:list[Fence]=Zoo.get_instance().get_fences()
        for fence in v:
            if animal in fence.get_animals():
                return fence
                
        raise Exception("L'animale non è stato trovato")
    @staticmethod
    def describe_zoo() -> str:
        keepers:list[Zookeeper]=Zoo.get_instance().get_zookeeper()
        fences:list[Zookeeper]=Zoo.get_instance().get_fences()
        output:str=f""  
        output+=f"Guardians:\n\n"
        for zookeeper in keepers:
            output+=f"Zookeeper(name={zookeeper.get_name()}, surname={zookeeper.get_surname()}, id={zookeeper.get_id()})\n\n"
        output+=f"Fences:\n\n"
        for fence in fences:
            output+=f"Fence(area={fence.get_area()}, temperature={fence.get_temperature()}, habitat={fence.get_habitat()})\n\n"
            output+=f"with animals:\n\n"
            animals:list[Animal]=fence.get_animals()
            for animal in animals:
                output+=f"Animal(name={animal.get_name()}, species={animal.get_species()}, age={animal.get_age()}, height={animal.get_height()}, width={animal.get_width()}, pre_habitat={animal.get_pre_habitat()}, health={animal.get_health()})\n\n"
            output+=f"#"*30
            output+=f"\n\n"

        return output

        

    
    



class Animal:
    def __init__(self,name:str,species:str,age:int,height:float,width:float,pre_habitat:str):
        self.set_name(name)
        self.set_species(species)
        self.set_age(age)
        self.set_height(height)
        self.set_width(width)
        self.set_pre_habitat(pre_habitat)
        self.health=round(100 * (1 / age), 3)
        if self.health==0:
            raise Exception(f"errore età non valida ")
        self.set_area_anim(height*width)
        

     
    def set_name(self,name:str):
        self.name=name

    def set_species(self,species:str):
        self.species=species

    def set_age(self,age:int):
        self.age=age

    def set_height(self,height:float):
        self.height=height

    def set_width(self,width:float):
        self.width=width

    def set_pre_habitat(self,pre_habitat:str):
        self.pre_habitat=pre_habitat

    def set_health(self,health:int):
        self.health=health

    def set_area_anim(self,area_anim:float):
        self.area_anim=area_anim
    

    def get_name(self)->str:
        return self.name
    
    def get_species (self)->str:
        return self.species
    
    def get_age(self)->int:
        return self.age
    
    def get_height(self)->float:
        return self.height
    
    def get_width(self)->float:
        return self.width
    
    def get_pre_habitat(self)->str:
        return self.pre_habitat
    
    def get_health(self)->int:
        return self.health
    
    def get_area_anim(self)->float:
        return self.area_anim    
    





class Fence:
    def __init__(self,temperature:float,area:float,habitat:str):
        self.set_temperature(temperature)
        self.set_area(area)
        self.set_habitat(habitat)
        self.animals=[]


    def set_temperature(self,temperature:float):
        self.temperature=temperature
    
    def set_area(self,area:float):
        self.area=area

    def set_habitat(self,habitat:str):
        self.habitat=habitat

    def set_animals(self,animals:list[Animal]):
        self.animals=animals

    def get_temperature(self)-> float:
        return self.temperature
    
    def get_area(self)->float:
        return self.area
    
    def get_habitat(self)->str:
        return self.habitat
    
    def get_animals(self)->list[Animal]:
        return self.animals
    
    def get_area_rem(self)-> float:
        anim:list[Animal]=self.get_animals()
        area_rem:float=self.get_area()
        for animal in anim:
            area_rem-= animal.get_area_anim()
        return area_rem


    


class Zookeeper:
    def __init__(self,name:str,surname:str,id:int):
        self.name=name
        self.surname=surname
        self.id=id


    def set_name(self,name:str):
        self.name=name

    def set_surname(self,surname:str):
        self.surname=surname

    def set_id(self,id:int):
        self.id=id

    def get_name(self)->str:
        return self.name
    
    def get_surname(self)->str:
        return self.surname
    
    def get_id(self)->str:
        return self.id


    def add_animal(self,animal: Animal, fence: Fence):
        if animal.get_age()>0:      
            if animal not in fence.animals:
                if fence.habitat==animal.get_pre_habitat() and fence.get_area_rem() >= animal.get_area_anim():
                    fence.animals.append(animal)
                else:   
                    raise Exception(f"l'animale {animal} non può essere ammesso nel recinto per incompatibilità!")
            else:
                raise Exception(f"Non puoi aggiungere due animali uguali all'interno del recinto.")
    
    def remove_animal(self,animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
        else:
            raise Exception(f"animale non trovato!")

    
    def feed_animal(self,animal: Animal):
        if animal.get_age() > 0:
            new_h:float = animal.get_height() * 1.02  
            new_w:float = animal.get_width() * 1.02  

            if new_h * new_w <= Zoo.find_animal(animal).get_area_rem():
                animal.set_height(new_h)
                animal.set_width(new_w)
                animal.set_health(animal.get_health()*1.01)
                
            else:
                raise Exception(f"Non c'è spazio per dar da mangiare a: {animal.get_name()}.")
        else:
            raise Exception(f"L'età dell'animale {animal.get_name()} non è valida.")


    def clean(self,fence:Fence)-> float:
        if fence.get_area_rem()==0:
            return fence.get_area()
        return (fence.get_area()-fence.get_area_rem())/fence.get_area_rem()
    
    




        
    
    
        
 







 







        

           



            
