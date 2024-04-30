#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

print("ESERCIZIO 4-1:")
pizza:list[str]=["Diavola","Napoli","Margherita","Capricciosa"]


for p in pizza:
    print(p)



for p in pizza: 
    print(f"\nUna delle pizze più mangiate in Italia è la {p}!")



print(f"\nLa pizza che più mi piace è la {pizza[0]}, deve essere però fatta in un certo modo, con i prodotti giusti e la cottura ad una temperatura ottimale.")


#4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# Modify your program to print a statement about each animal, such as A dog would make a great pet.
# Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!


print("ESERCIZIO 4-2:")
animals:list[str]=["cane","gatto","tigre","lupo"]

for a in animals:
    print(a)


for a in animals:
    print(f"\nGli esemplari di {a} sono mammiferi.")


print(f"\nSia il {animals[0]} che il {animals[3]} fanno parte della famiglia dei canidi, mentre il {animals[1]} e la {animals[2]} fanno parte della famiglia dei felini!")




#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
print("\nESERCIZIO 4-3:")
for i in range(1,21):
    print (i)



#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

print("\nESERCIZIO 4-4:(togliere commento per far partire il print)")
one_million:list[int]=[x for x in range(1,1000001)]

#for i in one_million:
    #print(i)







#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.
print("ESERCIZIO 4-5:")
print(f"\nIl numero più piccolo della lista è:{min(one_million)}")
print(f"\nIl numero più grande della lista è:{max(one_million)}")
print(f"\nLa somma di tutti i numeri è di:{sum(one_million)}")


#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
num_disp:list[int]=[i for i in range(1,21,2)]
print(f"\nESERCIZIO 4-6: {num_disp}")


#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
multipli3:list[int]=[index for index in range(3,33,3)]
print(f"\nESERCIZIO 4-7: {multipli3}")



#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cubi:list[int]=[c for c in range(1,11)]
print("\nESERCIZIO 4-8:")
for e in cubi:
    print(e**3)


#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubi_comprehension:list[int]=[index**3 for index in range(1,11)]
print(f"ESERCIZIO 4-9: {cubi_comprehension}")



#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
# Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

#lista presa da esercizio 4-6
print("ESERCIZIO 4-10:")
print(f"\nI primi 3 elementi della lista sono: {num_disp[:3]}.")
print(f"\n3 elementi dal centro della lista sono: {num_disp[4:7]}")
print(f"\nGli ultimi 3 elementi della lista sono: {num_disp[-3:]}")

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

print("ESERCIZIO 4-11:")
friend_pizzas:list[str]=pizza.copy()
pizza.insert(0,"Boscaiola")
friend_pizzas.insert(0,"Cacio e Pepe")
print("Le mie pizze preferite sono: ")
for i in pizza:
    print(i)


print("Le pizze preferite del mio miglior amico sono: ")
for x in friend_pizzas:
    print(x)




#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
#Choose a version of foods.py, and write two for loops to print each list of foods.

print("ESERCIZIO 4-12: ")
for x in pizza:
    print(x)
for y in friend_pizzas:
    print(y)


#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.
print("\nESERCIZIO 5-1/5-2:")
bike:str="bici"
print("is bike == bici? I predict True.")
print(bike=="bici")
print("\nis bike == macchina? I predict False.")
print(bike=="macchina")
print("\nIs len(bike)== 4? I predict True.")
print(len(bike)== 4)
print("\nIs len(bike)== 3? I predict False.")
print(len(bike)== 3)
print("\nIs 'ic' in bike? I predict True.")
print("ic" in bike)
print("\nIs 'ii' in bike? I predict False.")
print("ii" in bike)
print("\nIs len(bike)==len('bici')? I predict True.")
print(len(bike)==len("bici"))
print("\nIs len(bike)==len('biciii')? I predict False.")
print(len(bike)==len("biciii"))
print("\nIs bike.lower()== 'bici'? I predict True")
print(bike.lower()=='bici')
print("\nIs bike.upper()== 'bici'? I predict False")
print(bike.upper()=='bici')
print("\nis bike == 'Bici'? I predict False.")
print(bike=="Bici")
print("\nIs bike != 'Ktm'? I predict True")
print(bike!='Ktm')
print("\nIs bike == 'Ktm'? I predict False")
print(bike=='Ktm')
print("\nIs 'bici' in bike? I predict True")
print("bici" in bike)
print("\nIs bike in 'bici'? I predict True")
print(bike in "bici")


#5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
# Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
print("\nESERCIZIO 5-3")
alien_color:str="red"
if alien_color is "red":
    print("\nYou earned 5 points!")
else:
    print("\n")



if alien_color == "green":
    print("\n")
elif alien_color == "yellow":
     print("\n")
elif alien_color == "red":
    print("\nYou earned 5 points!")




print("\nESERCIZIO 5-4/5-5")
lista_colori:list[str]=["yellow","red","green"]
alien_color2:str="green"
alien_color3:str="yellow"
alien_color4:str="red"

if alien_color2 in lista_colori:
    print("\nYou earned 5 points!")
elif alien_color2 not in lista_colori:
    print("\nIl colore non èpresente nella lista.")
else:
    print("\n")



if alien_color3 in lista_colori:
   print("\nYou earned 10 points!") 
elif alien_color3 not in lista_colori:
    print("\nIl colore non è presente nella lista.")
else:
    print("\n")





if alien_color4 in lista_colori:
   print("\nYou earned 15 points!") 
elif alien_color4 not in lista_colori:
    print("\nIl colore non è presente nella lista.")
else:
    print("\n")


#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
# If the person is less than 2 years old, print a message that the person is a baby.
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# If the person is age 65 or older, print a message that the person is an elder.
print("\nESERCIZIO 5-6")
age:int=int(input("Inserisci l'età desiderata: ").strip())
if age <2:
    print("\nThe person is a baby")
elif age >=2 and age <=4:
    print("\nThe person is a toddler")
elif age>4 and age <13:
    print("\nThe person is a kid.")
elif age>=13 and age <20:
    print("\nThe person is a teenager.")
elif age>=20 and age <=65:
    print("\nThe person is a adult.")
else:
    print("\nThe person is an elder.")



#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
# Make a list of your three favorite fruits and call it favorite_fruits.
# Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!
print("\nESERCIZIO 5-7")
lista_frutta:list[str]=["ananas","cocomero","cocco","melone","mele","pere"]
trefrutti_prefe:list[str]=["fico d'India","ananas","mango","albicocca","cocomero"]
if "banana" in lista_frutta:
    print("\nla banana è presente nella lista della frutta!")
else:
    print("\nla banana NON è presente nella lista della frutta!")

if "cocco" in lista_frutta:
    print("\nil cocco è presente nella lista della frutta!")
else:
    print("\nil cocco NON è presente nella lista della frutta!")




if trefrutti_prefe[0] in lista_frutta:
    print(f"\n{trefrutti_prefe[0]} è nella lista.")
if trefrutti_prefe[1] in lista_frutta:
    print(f"\n{trefrutti_prefe[1]} è nella lista. ")
if trefrutti_prefe[2] in lista_frutta:
    print(f"\n{trefrutti_prefe[2]} è nella lista. ")
if trefrutti_prefe[3] in lista_frutta:
    print(f"\n{trefrutti_prefe[3]} è nella lista. ")
if trefrutti_prefe[4] in lista_frutta:
    print(f"\n{trefrutti_prefe[4]} è nella lista. ")


    
#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
# If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
print("\nESERCIZIO 5-8")
usernames = ['admin', 'Alice', 'Bob', 'Charlie', 'Dave']

for utente in usernames:
    
    if utente == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {utente}, thank you for logging in again.")




#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!
#Remove all of the usernames from your list, and make sure the correct message is printed.
print("\nESERCIZIO 5-9")
usernames = []


if usernames:
    for u in usernames:
        if u == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"\nHello {u}, thank you for logging in again.")
else:
    print("We need to find some users!")




#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# Store the numbers 1 through 9 in a list.
# Loop through the list.
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
print("\nESERCIZIO 5-11")
numeri = list(range(1, 10))

for num in numeri:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
