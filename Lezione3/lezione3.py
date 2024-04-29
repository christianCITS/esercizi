#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!


pizza:list[str]=["Diavola","Napoli","Margherita","Capricciosa"]


for p in pizza:
    print(p)



for p in pizza: 
    print(f"Una delle pizze più mangiate in Italia è la {p}!")



print(f"La pizza che più mi piace è la {pizza[0]}, deve essere però fatta in un certo modo, con i prodotti giusti e la cottura ad una temperatura ottimale.")


#4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# Modify your program to print a statement about each animal, such as A dog would make a great pet.
# Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!



animals:list[str]=["cane","gatto","tigre","lupo"]

for a in animals:
    print(a)


for a in animals:
    print(f"Gli esemplari di {a} sono mammiferi.")


print(f"Sia il {animals[0]} che il {animals[3]} fanno parte della famiglia dei canidi, mentre il {animals[1]} e la {animals[2]} fanno parte della famiglia dei felini!")




#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for i in range(1,21):
    print (i)



