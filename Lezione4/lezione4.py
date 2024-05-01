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
def Favorite_Book(title) ->(str):
    print(f"\nUno dei miei libri preferiti è: {title}.")



Favorite_Book("Il nome del vento")



#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. 
#Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
print("\nESERCIZIO 8-3")
def Make_Shirt(size:str,text:str)->(None):
    print(f"\nLa taglia della T-Shirt è una: {size}, ed il messaggio è: {text}.")
Make_Shirt("L","Nella vecchia fattoria")
Make_Shirt(size="L",text="Nella vecchia fattoria")





