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







