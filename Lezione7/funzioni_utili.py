#Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
#Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codie
    dizionario = {}
    for i, j in tuples:
        if i in dizionario:
            dizionario[i].add(j)
        else:
            dizionario[i] = set([j])
             
    dizionario= {k: list(v) for k, v in dizionario.items()}
    return dizionario




#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre 
#c'è la corrispondente parentesi che chiude.

def check_parentheses(expression: str) -> bool:
    # cancella pass e scrivi il tuo codice
    count=0
    for i in expression:
        if i == "(":
            count += 1
        elif i == ")":
                if count != 0:
                    count -= 1
                else:
                    return (False)

    if count == 0:
        return (True)
    else:
        return (False)
    






    #Scrivi una funzione che accetti un dizionario 
    #di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.




def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    # cancella pass e scrivi il tuo codice
        dizionario:dict[str,float]={}
        for k,v in prodotti.items():
            if v > 20:
                dizionario[k]=v-v*10/100
        return dizionario
            



#Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

def aggrega_voti(voti: dict) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codice

        risultato:dict={}

        for stud in voti:
            nome=stud["name"]
            voto=stud["voto"]
            

            if nome in risultato:
                risultato[nome].append(voto)
            else:
                risultato[nome]=[voto]
            return risultato
        













####################################################################################################################





def create_contact(name: str, email: str=None, telefono: int=None) -> dict:

    contatti:dict={"profile":name,"email":email,"telefono":telefono}
            
    return contatti




def update_contact(contatti: dict, name: str, email: str =None, telefono: int=None) -> dict:
    if contatti["profile"]== name:
         contatti["email"]=email
         contatti["telefono"]=telefono






#scrivi una funzione che ruota glie elementi di una lista verso sinistra di un numero specificato di k posizioni la rotazione verso sinistra significa che ciuascun elemento viene spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista.
#per la rotazione utilizzare lo slicing e gestire il caso in cui vada out of range 

def rotate_left(elements:list[int],k:int):
     n:int=len(elements)
     ruotati:list[int]=[]
     if k> n:
          k=k%n   #trick per calcolare le posizioni in cui è possibile ruotare gli elementi della lista anche se con meno spazi

     
     
     ruotati=elements[k:] + elements[:k]     

     return ruotati     





        



