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
famous_person: str="Giuseppe Ungaretti"
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
#aaa




 










