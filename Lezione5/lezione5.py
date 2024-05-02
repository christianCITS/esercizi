#Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
def countdown(n: int) -> int:
    
    while n >= 0:
        print(n)
        n=n-1


#Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
def sum_above_threshold(numbers: list[int],thre:int) -> int:
    tot:int=0
    for n in numbers:
        if n>thre:
            tot=tot+n
    return tot
    return thre
            
            


#La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
#Un errore nell'implementazione porta a risultati inaspettati.
#Trova l'errore e correggi il codice affinché soddisfi i casi di test.


def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers) 
    





#Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". Un numero magico è definito come un numero che contiene il numero 7.

def is_magic_number(num: int) -> bool:
    numero:str=str(num)
    numer_l:list[int]=[]
    for e in numero:
        numer_l.append(e)
            
    
    
    if "7" in numer_l:
        return True
    else: 
        return False
   














def rounded_average(numbers: list[int]) -> int:
 risutato:int=0 
 risultato=sum(numbers) / len(numbers) 
 return round(risultato)


    





















def convert_temperature(celsius:float,f:bool=True) -> float:
    # cancella ... e definisci i parametri della funzione, successivamente cancella pass e scrivi il tuo codice
    tot:float=0

    if f == True:
        tot=celsius *9/5 +32
    elif f== False:
        tot=celsius -32
        tot=tot*5/9
    return tot