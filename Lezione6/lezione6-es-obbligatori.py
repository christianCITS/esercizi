#9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
#Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message 
#indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
print(f"\nESERCIZIO 9-1")
class Restaurant:
    def __init__(self,restaurant_name:str,cuisine_type:str,number_served:int=0):
        self.restaurant_name:str=restaurant_name
        self.cuisine_type:str=cuisine_type
        self.number_served=number_served
    
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name},{self.cuisine_type}")

    
    def open_restaurant(self):
        print(f"Il ristorante è APERTO!")
    
    def set_number_served(self,numb_serv:int)-> int:
        self.number_served=numb_serv
        return self.number_served
        
    def increment_number_served(self,incr_serv:int)-> int:
        self.number_served+=incr_serv 
        return self.number_served  

    
ristorante1=Restaurant("Da Giggetto","cucina italiana")
print(ristorante1.restaurant_name)
print("-"*30)
print(ristorante1.cuisine_type)
print("-"*30)
ristorante1.describe_restaurant()
ristorante1.open_restaurant()



#9-2. Three Restaurants: Start with your class from Exercise 9-1. 
#Create three different instances from the class, and call describe_restaurant() for each instance.
print(f"\nESERCIZIO 9-2")
ristorante2=Restaurant("Barcellona sabores","cucina spagnola")
ristorante3=Restaurant("american's flavour","cucina americana")
ristorante4=Restaurant("Sakura","cucina giapponese")

print("-"*30)
ristorante2.describe_restaurant()
ristorante3.describe_restaurant()
ristorante4.describe_restaurant()


#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
#and then create several other attributes that are typically stored in a user profile. 
#Make a method called describe_user() that prints a summary of the user’s information... 
#Make another method called greet_user() that prints a personalized greeting to the user. 
#Create several instances representing different users, and call both methods for each user.
print(f"\nESERCIZIO 9-3")
class Users:
    def __init__(self,first_name:str,last_name:str,gender:str,age:int,login_attempts:int):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.age=age
        self.login_attempts=login_attempts

    def describe_user(self):
        print(f"nome: {self.first_name}\ncognome: {self.last_name}\nsesso: {self.gender}\netà: {self.age}")

    def greet_user(self):
        print(f"Ciao {self.first_name} grazie per esserti connesso!")

    def increment_login_attempts(self):
        self.login_attempts+=1
        return self.login_attempts
        
    
    def reset_login_attempts(self):
        self.login_attempts=0
        return self.login_attempts

user1=Users("Romualdo","Franceschini","UOMO",35,0)
user2=Users("Christian","Errini","DONNA",54,0)
user3=Users("Alberto","Bonavista","UOMO",65,0)
user4=Users("Francesco","Salomoni","UOMO",18,0)

print("-"*30)
user1.describe_user()
print("-"*30)
user2.describe_user()
print("-"*30)
user3.describe_user()
print("-"*30)
user4.describe_user()
print("-"*30)
user1.greet_user()
print("-"*30)
user2.greet_user()
print("-"*30)
user3.greet_user()
print("-"*30)
user4.greet_user()
print("-"*30)


#9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. 
#Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
#Add a method called set_number_served() that lets you set the number of customers that have been served. 
#Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number 
#of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
print(f"\nESERCIZIO 9-4")

restaurant=Restaurant("Da Walter","cucina tipica abbruzzese",50)
print("le persone che sono state servite sono: ",restaurant.number_served)
print("-"*30)
restaurant.number_served=10
print("le persone che sono state servite sono: ",restaurant.number_served)
print("-"*30)


print("numero di persone servite settato a : ",restaurant.set_number_served(70))
print("con questo incremento le persone servite sono: ",restaurant.increment_number_served(30))
print("-"*30)



#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
#Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. 
#Print the value of login_attempts to make sure it was incremented properly, 
#and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
print(f"\nESERCIZIO 9-5")

user5=Users("Giovanni","Lucifora","UOMO",43,0)
print("numero login attuale: ",user5.login_attempts)
user5.increment_login_attempts()
user5.increment_login_attempts()
user5.increment_login_attempts()
user5.increment_login_attempts()
print("numero login attuale: ",user5.login_attempts)
user5.reset_login_attempts()
print("numero login attuale: ",user5.login_attempts)
print("-"*30)


#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits 
#from the Restaurant class you wrote in Exercise 9-1  
#Add an attribute called flavors that stores a list of ice cream flavors. 
#Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 
print(f"\nESERCIZIO 9-6")
class Ice_Cream_Stand(Restaurant):

    def __init__(self, restaurant_name: str, cuisine_type: str,flavors:list[str], number_served: int = 0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors=flavors
        

    def flavour_Display(self) -> str:
       return f"I gusti disponibili sono: {self.flavors}"
    


gelateria=Ice_Cream_Stand("gelateria IGLOO","gelati e frullati",["banana","fragola","melone","cioccolato","pistacchio"],20)
print(gelateria.flavour_Display())
print("-"*30)





#9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. 
#Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
#Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 
print(f"\nESERCIZIO 9-7")

class Admin(Users):
    def __init__(self, first_name: str, last_name: str, gender: str, age: int, login_attempts: int,privileges:list[str]):
        super().__init__(first_name, last_name, gender, age, login_attempts)
        self.privileges=privileges

    def show_privileges(self) ->str:
        return f"i privilegi dell'utente sono: {self.privileges}"
    
user6=Admin("Ernesto","Capobianco","MASCHIO",40,0,["add user","ban user","reset the login attempts cont.","delete post"])



print(user6.show_privileges())
print("-"*30)

#9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings.  
#Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
#Create a new instance of Admin and use your method to show its privileges.
print(f"\nESERCIZIO 9-8")
class Privileges:
    def __init__(self,privileges:list[str]):
        self.privileges=privileges

    def show_privileges(self) ->str:
        return f"i privilegi dell'utente sono: {self.privileges}"


class Admin(Users):
    def __init__(self, first_name: str, last_name: str, gender: str, age: int, login_attempts: int,privileges:Privileges):
        super().__init__(first_name, last_name, gender, age, login_attempts)
        self.privileges=privileges

impost_priv=Privileges(["watch other profiles","no ads"])
utente7=Admin("Alessio","Giacomini","UOMO",40,3,impost_priv)

print(utente7.privileges.show_privileges())
print("-"*30)



                                       
                                       





            

#9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). 
#This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric car with a default battery size, call get_range() 
#once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.
print(f"\nESERCIZIO 9-9")
print("-"*30)


"""ESERCIZIO NON PRESENTE """






#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. 
#Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
print(f"\nESERCIZIO 9-10")
print("-"*30)

"""CONTROLLARE FILE: modulorestaurant.py e file-Restaurant.py"""
    




    
#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. 
#Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
print(f"\nESERCIZIO 9-11")
print("-"*30)

"""ESEGUITO IN ESERCIZIO PRECEDENTE"""







#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
#In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
print(f"\nESERCIZIO 9-12")
print("-"*30)
    
"""ESEGUITO IN ESERCIZIO PRECEDENTE"""




#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() 
#that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. 
#Make a 10-sided die and a 20-sided die. Roll each die 10 times.
print(f"\nESERCIZIO 9-13")
import random

class Die:
    def __init__(self,sides:int=6):
        self.sides=sides

    def roll_die(self):
        ris=random.randint(1,self.sides)
        print(f"Il dado da {self.sides} ha fatto: {ris}")
    

dado6=Die()
dado6.roll_die()
dado6.roll_die()
dado6.roll_die()
dado6.roll_die()
dado6.roll_die()
dado6.roll_die()
dado6.roll_die()
dado6.roll_die()
dado6.roll_die()
dado6.roll_die()
print("-"*30)
dado10=Die(10)
dado10.roll_die()
dado10.roll_die()
dado10.roll_die()
dado10.roll_die()
dado10.roll_die()
dado10.roll_die()
dado10.roll_die()
dado10.roll_die()
dado10.roll_die()
dado10.roll_die()
print("-"*30)
dado20=Die(20)
dado20.roll_die()
dado20.roll_die()
dado20.roll_die()
dado20.roll_die()
dado20.roll_die()
dado20.roll_die()
dado20.roll_die()
dado20.roll_die()
dado20.roll_die()
dado20.roll_die()


#9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
#Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
print(f"\nESERCIZIO 9-14")
lottery:list[int,str]=[8,1,10,7,4,9,2,6,3,5,"H","A","P","F","Z"]
lucky:list[int,str]=[]

lucky=random.sample(lottery,4)
print(f"Qualsiasi ticket che corrisponde a: {lucky} sarà vincente!")
print("-"*30)

#9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
#Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.
print(f"\nESERCIZIO 9-15")
my_ticket:list[int,str]=[10,3,9,4]
cont=0

while True:
    lucky=random.sample(lottery,4)
    cont+=1
    valid=True
    for e in lucky:
        if e not in my_ticket:
            valid=False
            break
    if valid:
        break



print(f"Hai vinto!!! i tentativi sono stati: {cont}")
print("-"*30)



   












        




