#Christian Cioeta
#18/04/2024

print("Hello World")

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person.
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

#this variable contain a name
a:str="Claudio"
print(f"hello {a} Would you like to learn...")


#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name 
#in lowercase, uppercase, and title case.

#this variable contain a name
b="Antonio"
#this variables contains the the same name in: lower,upper,title
b_lower:str=b.lower()
b_upper:str=b.upper()
b_title:str=b.title()
print(b_lower,b_upper,b_title)
#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake
# never tried anything new.”

print ("Giuseppe Ungaretti una volta disse:"  ' "Mi illumino di immenso."')


#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called 
#famous_person. Then compose your message and represent it with a new variable called message. Print your message. 


#this variables contains the name and the quote 
famous_person:str="Giuseppe Ungaretti"
message:str=' "Mi illumino di immenso."'

print(f"{famous_person} una volta disse{message}")

#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
filename:str='python_notes.txt'
print(filename.removesuffix(".txt"))
 
#3-1. Names: Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.

names:str=["Gabriele","Cristian","Pietro","Mattia"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.
print(f"{names[0]} Sei stato invitato alla festa.")
print(f"{names[1]} Sei stato invitato alla festa.")
print(f"{names[2]} Sei stato invitato alla festa.")
print(f"{names[3]} Sei stato invitato alla festa.")

#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

#
cars:list=["Ford","Ferrari","Bmw","Bugatti"]

print(f"I motori {cars[0]} sono tra i più affidabili.")
print(f"le {cars[1]} sono sopravvalutate.")
print(f"In futuro vorrei possedere una {cars[2]}.")
print(f"la {cars[3]} è una delle macchine più veloci.")



#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.


lista_invitati:list=["Diego Abatantuono","Bill Gates","Leonardo Di Caprio","Gigi Proietti"]

for x in lista_invitati:
    print(f"Ciao, {x} sei ufficialmente invitato alla cena.")


#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

print(f"{lista_invitati[2]} non potrà partecipare alla cena.")

nuova_lista:list=["Diego Abatantuono","Bill Gates","Bob Marley","Gigi Proietti"]

for x in nuova_lista:
    print(f"Ciao {x} Ecco il tuo nuovo invito alla cena. ")


#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

for n in nuova_lista:
    print(f"Ciao {n} abbiamo trovato un tavolo più grande! a breve riceverai i nuovi inviti.")
nuova_lista.insert(0,"Cassius Clay")
nuova_lista.insert(3,"Francesco Totti")
nuova_lista.append("Micheal Schumacher")

print(f"Ciao {nuova_lista[0]} ecco finalmente il nuovo invito alla cena. ")
print(f"Ciao {nuova_lista[1]} ecco finalmente il nuovo invito alla cena. ")
print(f"Ciao {nuova_lista[2]} ecco finalmente il nuovo invito alla cena. ")
print(f"Ciao {nuova_lista[3]} ecco finalmente il nuovo invito alla cena. ")
print(f"Ciao {nuova_lista[4]} ecco finalmente il nuovo invito alla cena. ")
print(f"Ciao {nuova_lista[5]} ecco finalmente il nuovo invito alla cena. ")
print(f"Ciao {nuova_lista[6]} ecco finalmente il nuovo invito alla cena. ")

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. ch timEae you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.


nuova_lista1:list=nuova_lista
for n in nuova_lista1:
    print(f"Signor {n} a causa di un disservizio la prenotazione potrà essere solo per due invitati. Ci scusiamo per il disagio.")



while len(nuova_lista1)>2:
    print(f"Ci scusiamo Signor {nuova_lista1[-1]} ma il suo invito è stato cancellato.")
    nuova_lista1.pop()


del nuova_lista1[0]
del nuova_lista1[0]
print(nuova_lista1)



#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
#Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse()  to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.

places:list=["Giappone","Irlanda","America","Brasile","Cina","Costa Rica"]
places1:list=sorted(places)
print(places1)
print(places)

places1:list=sorted(places,reverse=True)
print(places1)
print(places)

places1.reverse()
print(places1)
places1.reverse()
print(places1)

places1.sort()
print(places1)

places1.sort(reverse=True)
print(places1)


#3-9. Dinner Guests: Working with one of the programs from Exercises 3,
# use len() to print a message indicating the number of people you’re inviting to dinner.

print(f"Il numero di invitati alla festa è di {len(lista_invitati)} persone")



#3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.


things:list=["Italiano","Cinese","Greco","Francese","Spagnolo","Giapponese"]

print(len(things))
print(sorted(things))
things.append("Turco")
print(things)
things.pop()
print(things)
things.reverse()
print(things)
things.insert(2,"thailandese")
print(things)





#6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

schedario:dict={"first_name":"Arturo","last_name":"Brancozzi","age":99,"city":"Kentucky"}
print(schedario["first_name"])
print(schedario["last_name"])
print(schedario["age"])
print(schedario["city"])



#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, 
#and store each as a value in your dictionary. Print each person’s name and their favorite number. 
#For even more fun, poll a few friends and get some actual data for your program.

num_fort:dict={"Filippo":7,"Alberto":10,"Mario":57,"Pasquale":17}
print(num_fort["Filippo"])
print(num_fort["Alberto"])
print(num_fort["Mario"])
print(num_fort["Pasquale"])


#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary:dict={"insert":"Inserisce un elemento all'interno della lista. ","pop":"toglie l'ultimo elemento della lista e lo restituisce.","sort":"organizza la lista.", "append":"aggiunge un elemento alla fine della lista.","len":"restituisce la lunghezza della lista."}

for k,v in glossary.items():
    print(f"{k} \n {v}")


#6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people.   
#As you loop through the list, print everything you know about each person.


schedario2:dict={"first_name":"Giovanni","last_name":"Ciccolli","age":78,"city":"Catania"}
schedario3:dict={"first_name":"Francesco","last_name":"Pertolini","age":80,"city":"Milano"}

people:list=[schedario,schedario2,schedario3]
print(people)

#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
#you do, print everything you know about each pet. 

pet1:dict={"pet":"dog","Owner":"Lillo"}
pet2:dict={"pet":"cat","Owner":"Phil"}
pet3:dict={"pet":"bird","Owner":"Albert"}
pet4:dict={"pet":"snake","Owner":"David"}

pets:list=[pet1,pet2,pet3,pet4]
print(pets)




#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
#To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.


favorite_places:dict={"Massimo":"Parigi","Gabriele":"Barcellona","Alfonso":"India"}


for k,v in favorite_places.items():
    print(k,v)

#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
#Then print each person’s name along with their favorite numbers.


num_fort["Filippo"]= 7,23
num_fort["Alberto"]= 10,12
num_fort["Mario"]= 57,99
num_fort["Pasquale"]=17,34

print(num_fort)

#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, 
#and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities:dict={"Lugano":{"population":"approx.60.000","country":"Svizzera","fact":"Lugano è famosa per i suoi istituti bancari"},
             "Roma":{"population":"approx.2.000.000","country":"Italia","fact":"Roma è una delle città più antiche del mondo."},
             "Tokyo":{"population":"approx.14.000.000","country":"Giappone","fact":"Tokyo è una delle città più densamente popolate del mondo."}


}

for k,v in cities.items():
    print(k,"\n",v)










#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
    #Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, 
    #or improving the formatting of the output.
    

#aggiungo altre info al dizionario, lo converto in due liste (chiavi,valori) e stampo in  output il numero preferito della prima e dell'ultima persona formattando la stringa
num_fort:dict={"Filippo":7,"Alberto":10,"Mario":57,"Pasquale":17,"Massimo":68,"Alessandro":19}
num_fortch:list=list[str](num_fort.keys())
num_fortva:list=list[int](num_fort.values())
print(f"Il numero preferito di {num_fortch[0]} è: {num_fortva[0]}. \nmentre quello di {num_fortch[-1]} è: {num_fortva[-1]}.")



###






























 










