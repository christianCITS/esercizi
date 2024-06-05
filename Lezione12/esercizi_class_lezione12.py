'''Sistema di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, 
restituirli e visualizzare quali libri sono disponibili in un dato momento.'''




class Libro:
    def __init__(self,titolo:str,autore:str,is_borrowed:bool=False):
        self.titolo:str=titolo
        self.autore:str=autore
        self.is_borrowed=is_borrowed


    def __str__(self) -> str:
        return f"{self.titolo}"



class Biblioteca:
    def __init__(self):
        self.lista_libri:list[Libro]=[]



    def aggiungi_libro(self,libro:Libro)-> str:
        if libro not in self.lista_libri:
            self.lista_libri.append(libro)
            return f"Il libro: {libro} è stato aggiunto alla colezione!"
        return f"il libro: {libro} è già nella collezione!"
    

    def presta_libro(self,titolo:str):
        for libro in self.lista_libri:
            if titolo == libro.titolo and libro.is_borrowed==False:
                libro.is_borrowed=True
                return f"Il libro: {titolo} è stato prestato!"
        return f"Il  libro non è diponibile"
    
    def restituisci_libro(self,titolo:str):
        for libro in self.lista_libri:
            if titolo == libro.titolo and libro.is_borrowed==True:
                libro.is_borrowed=False
                return f"Il libro: {titolo} è stato restituito!"
        return f"Il libro non è diponibile"

    def mostra_libri_disponibili(self):
        for libri in self.lista_libri:
            if libri.is_borrowed== False:
                print(f"DISPONIBILE: {libri.titolo}")
            
            elif libri.is_borrowed!= False:
                print(f"NON DISPONIBILE: {libri.titolo}")





            

    
'''Catalogo Film 
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. 
Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.
Metodi:
 add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
    Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, 
    il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
    Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene 
    la parola cercata nel titolo.'''











class MovieCatalog:
    def __init__(self,):
        pass



"commit prova"


    
            
                





