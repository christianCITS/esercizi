
#1. Create a Playlist:
#Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
#The function should return a dictionary with the playlist name and a set of songs. 
#Call the function with different numbers of songs to demonstrate flexibility.
#Example: create_playlist("Road Trip", {"Song 1", "Song 2"})
#Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating whether it is liked (True or False). 
#This function should return an updated dictionary.
#Example: add_like(dictionary, “Road Trip”, liked=True)

def function_playlist(p_name:str,*song_t:set) ->dict:
    new_diz:dict={}
    new_diz[p_name]=set(song_t)
    return new_diz


print(function_playlist("nome playlist","song 1","song 2","song 3"))
print(function_playlist("nome playlist","song 1","song 2","song 3","song 4","song 5","song 3"))
print(function_playlist("nome playlist","song 1"))
dizionario1:dict=function_playlist("CANZONI ESTATE","SONG 1","SONG 2")





def add_like(diz:dict,name_p:str,response:bool) -> dict:
   diz2:dict={} 
   for k,v in dizionario1.items():
       diz2[k]=v
       diz2["CANZONI ESTATE"]=name_p
       diz2["Favorite"]=response
       return diz2




print(add_like(dizionario1,"gionni playlist",True))





#2. Book Collection:
#Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. This function should return a dictionary where the author's name is the key and the value is a list of their books. Demonstrate this function by adding books for different authors.
#Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
    
def add_book(author:str,*book_t:str) ->dict:
    diz_aut:dict={}
    diz_aut[author]=book_t
    return diz_aut


print(add_book("autore random",["libro1","libro2","libro3"]))

#Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. This function should return an updated dictionary.
#Example: delete_book(dictionary, “Mark Twain”)

dizionario_autori:dict=add_book("j.k rowling",["la pietra filosofale","la camera dei segreti"])
def delete_book(diz:dict,author:str)-> dict:
    if author in diz:
        del diz[author]
    return diz


print(delete_book(dizionario_autori,"j.k rowling"))

