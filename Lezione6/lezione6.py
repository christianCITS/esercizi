"""class Person:


    def __init__(self,name,age):
        self.name=name 
        self.age=age


    def __str__(self)->str:
        return f"La persona ha {self.age} anni  e si chiama {self.name}"


alice=Person("Alice W.",45)
bob=Person("Bob M.",36)



print(bob.age)


if alice.age > bob.age:
    print(alice.age)
else:
    print(bob.age)

people:list=[alice,bob,Person("alberto",32),Person("filippo,",23),Person("luigino",80)]
min_age:int=float('inf')
index_min_age:int=0
for i in range(len(people)):
    if people[i].age < min_age:
        min_age=people[i].age
        index_min_age=i

print(people[3])"""






























###########################################################################################################



"""class Student:
    def __init__(self,name:str,studyProgram:str,age:int=None,gender:str=None):
        self.name:str=name 
        self.studyProgram:str=studyProgram
        self.age=age
        self.gender=gender
       
    def printInfo(self):
        return f"Il nome dello studente è {self.name} , il percorso di studi è : {self.studyProgram}, l'età è di : {self.age} anni e il sesso è : {self.gender}"
    
    



chri=Student("Christian","Cloud Developer",29,"maschio")
alb=Student("Alberto","Cloud Developer")
mar=Student("Marco","Cloud Developer")






print(Student.printInfo(chri))
print(Student.printInfo(alb))"""




class Animal:
     def __init__(self,name,legs):
          self.name=name
          self.legs=legs
     def __str__(self) ->str:
          return f"il nome dell'animale è : {self.name} e ha {self.legs} zampe."
    

     def get_legs(self) ->int:
          return self.legs


     

dog=Animal("Milo",4)
cat=Animal("Daisy",4)
bird=Animal("Lu",2)

print(dog)








