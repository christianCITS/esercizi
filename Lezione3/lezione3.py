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



#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)


one_million:list[int]=[x for x in range(1,1000001)]

#for i in one_million:
    #print(i)







#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.
print(min(one_million))
print(max(one_million))
print(sum(one_million))


#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
num_disp:list[int]=[i for i in range(1,21,2)]
print(num_disp)


#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
multipli3:list[int]=[index for index in range(3,33,3)]
print(multipli3)



#




