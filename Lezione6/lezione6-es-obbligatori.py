#9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
#Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message 
#indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

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


user5=Users("Giovanni","Lucifora","UOMO",43,0)
print("numero login attuale: ",user5.login_attempts)
user5.increment_login_attempts()
user5.increment_login_attempts()
user5.increment_login_attempts()
user5.increment_login_attempts()
print("numero login attuale: ",user5.login_attempts)
user5.reset_login_attempts()
print("numero login attuale: ",user5.login_attempts)


# #######FINIRE ESERCIZI E AGGIUNGERE NUMERO ESERCIZIO CON \N ########





    





