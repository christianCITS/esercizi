#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. 
#Call the function, and make sure the message displays correctly.
print("\nESERCIZIO 8-1")
def Display_Message() ->(str):
    print("In questo capitolo impareremo ad utilizzare le funzioni in modo corretto.")

Display_Message()

#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
#The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
#all the function, making sure to include a book title as an argument in the function call
print("\nESERCIZIO 8-2")
def Favorite_Book(title:str) ->(None):
    print(f"\nUno dei miei libri preferiti è: {title}.")



Favorite_Book("Il nome del vento")



#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. 
#Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
print("\nESERCIZIO 8-3")
def make_shirt(size:str,text:str)->(None):
    print(f"\nLa taglia della T-Shirt è una: {size}, ed il messaggio è: {text}.")
make_shirt("XL","Nella vecchia fattoria")
make_shirt(size="XL",text="Nella vecchia fattoria")


#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
print("\nESERCIZIO 8-4")
def make_shirt(size:str="L",text:str="I love Python")->(None):
    print(f"\nLa taglia della T-Shirt è una: {size}, ed il messaggio è: {text}.")

make_shirt()
make_shirt(size="M")
make_shirt(size="XXL",text="I love Java")


#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
#Call your function for three different cities, at least one of which is not in the default country.
print("\nESERCIZIO 8-5")

def describe_city(city:str,country:str="Inghilterra")->(None):
    print(f"\n{city} è in {country}. ")


describe_city("Parma","Italia")
describe_city(city="Venezia")
describe_city("Manchester")


#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
#The function should return a string formatted like this: "Santiago, Chile". 
#Call your function with at least three city-country pairs, and print the values that are returned.
print("\nESERCIZIO 8-6")
def city_country(city:str,country:str) ->(str):
    return f"\n{city},{country}"


print(city_country("Dublino","Irlanda"))
print(city_country("Tokyo","Giappone"))
print(city_country("Bucarest","Romania"))



#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
#The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
#Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. 
#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
#Make at least one new function call that includes the number of songs on an album.
print("\nESERCIZIO 8-7")
def make_album(artist:str,album:str,make_album:int=None) -> (dict[str,(str,int)]):
    art_album:dict[str,(str,int)]={}
    art_album[artist]=album,make_album
    return art_album



print(make_album("Kendrick Lamar","good kid, m.A.A.d city",))
print(make_album("Billie Eilish","When We All Fall Asleep, Where Do We Go?",14))
print(make_album("Artic Monkeys","AM",12))





#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
#Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
#Be sure to include a quit value in the while loop.
print("\nESERCIZIO 8-8")
a:str="c"
'''while a != "s" :
    a:str=input("Inserire album: ")
    b:str=input("Inserire titolo canzone: ")
    if a =="s":
        break
    print(make_album(a,b))'''



#8-9. Messages: Make a list containing a series of short text messages. 
#Pass the list to a function called show_messages(), which prints each text message.

print("\nESERCIZIO 8-9")
messages:list[str]=["Ciao come stai?","Ti aspetto sotto casa.","Buonanotte ci sentiamo domani.","Non potrò essere presente alla festa."]
def show_messages(mex:list[str]) ->None:
    for t in mex:
        print(f"\n{t}")




show_messages(messages)


#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() 
#that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
#After calling the function, print both of your lists to make sure the messages were moved correctly.
print("\nESERCIZIO 8-10")
def send_messages(mex:list[str],) ->list[str]:
    sent_messages:list[str]=[]
    for t in mex:
        print(f"\n{t}")
        sent_messages.append(t)
    return sent_messages



sent_messages:list[str]=send_messages(messages)
show_messages(messages)
show_messages(sent_messages)





#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
#After calling the function, print both of your lists to show that the original list has retained its messages.
print("\nESERCIZIO 8-11")      
'''Fatto nell'esercizio precedente'''






#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
#The function should have one parameter that collects as many items as the function call provides, 
#and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
print("\nESERCIZIO 8-12")
ingredienti_panini:list[str]=["bacon","cipolla","hamburger","cetriolini","pomodori"]
ingredienti_panini2:list[str]=["zucchine","peperoni","tofu"]
ingredienti_panini3:list[str]=["mozzarella","prosciutto crudo","basilico","olio"]
def ingr_sandwitch(*ingred:list[str])-> None:
    for i in ingred:
        print(f"\n{i}")





ingr_sandwitch("bacon","cipolla","hamburger","cetriolini","pomodori")
ingr_sandwitch(ingredienti_panini2)
ingr_sandwitch(ingredienti_panini3)




#8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. 
#All the values must be passed to the function as parameters. 
#The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
print("\nESERCIZIO 8-13")
def build_profile(name:str,surname:str,age:int,hair:str, weight:float)->str:
    return f"{name} {surname},age:{age},hair:{hair},weight:{weight}"




print(build_profile("Christian","Cioeta",29,"brown",70.5))






#8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. 
#Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
#Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
#Print the dictionary that’s returned to make sure all the information was stored correctly. 
print("\nESERCIZIO 8-14")
def info_car(manufacturer, model, **args):
    car_info = {'manufacturer': manufacturer, 'model': model}
    for key, value in args.items():
        car_info[key] = value
    return car_info




car = info_car('Jeep', 'Fiat', colore='nero', gps=True)
print(car)

    

    

#8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
#Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
print("\nESERCIZIO 8-15")

from printing_models import favorite_book

favorite_book("Le cronache di Narnia")




#8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
import printing_models
from printing_models import somma
from printing_models import favorite_book as fb
import printing_models as pm
from printing_models import divisione




print(divisione(10,5))