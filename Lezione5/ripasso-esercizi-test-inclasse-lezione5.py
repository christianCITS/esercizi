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









#Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. Ogni carta ha un valore compreso tra 2 e 11 compresi. 
#Tuttavia, se una mano contiene un asso, il valore dell'asso può essere 1 o 11, a seconda di quale sia più favorevole al giocatore in quel momento.
#Dato un elenco di valori delle carte che rappresentano una mano di blackjack, scrivi una funzione per determinare il valore totale della mano.

def blackjack(cards: list[int]):
    cards_sum: int = sum(cards)
    num_aces: int = cards.count(11)

    while cards_sum > 21 and num_aces > 0:
        cards_sum -= 10
        num_aces -=1
    
    return cards_sum
print(blackjack([1,10,11]))


#Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. Pertanto, data l'area specifica di una pagina Web rettangolare, 
#il tuo compito ora è progettare una pagina Web rettangolare, la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:
#1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
#2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
#3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

#Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.

#Esempio:

#construct_rectangle(4)

#L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
#Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. Quindi la lunghezza L è 2 e la larghezza W è 2.

def construct_rectangle(area: float) -> list[float]:
    combos: list = []
    for width in range(1, area  +1):
        for height in range(1, area + 1):
            if width * height == area and width >= height:
                combos.append([width, height])
    #combos = ([2,2], [4,1])
    min_diff: float = float("inf")
    for i, combo in enumerate (combos):
        curr_diff: float = combo[0] - combo[1]
        if curr_diff <= min_diff:
            min_diff = curr_diff
            index_diff = i
    return combos [index_diff]
print(construct_rectangle(4))
print(construct_rectangle(37))
print(construct_rectangle(42))

# In questi alberi in nodo principale è il più grande di quello alla sua sinistra, ma è più piccolo di quello
# alla sua destra
#
#es:               4
#               3    5
#              2   4.5  6

def search(array: list[int] , x: int) -> int :
    for i in range(len(array)):
        if array[i] == x:
            return x
    
    #se una lista non è ordinara per cercare x conviene fare questo,
    #perchè ordinare una lista richiede un numero di operazioni lunghe quanto la lista

    return None

# Seguendo questa funzione  len(erray) fa 10.000 iterazioni
# mentre così ne farebbe solo 14 log_2(len(array))   


# array = [-1 ,0 ,1 ,5 ,65 ,67 ,99 ,912 ,1207]
# x = 912

def binary_search(array: list[int] , x: int) -> int:
    
    low = 0
    high = len(array)

    while low < high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        else:
            if x > array[mid]:
                low = mid + 1
            else:
                high = mid - 1
    
    #Queste due funzioni scritte, posso semplicemnte essere sostituite con array.index(x)

    return None


def __binary_search_recursive(array: list[int] , x: int ,
                              low: int , high: int ) -> int:
   
    mid = (low + high) // 2

    if x == array[mid]:
        return mid
    elif x > array[mid]:
        return __binary_search_recursive(array ,x ,mid + 1 ,high)
    else:
        return __binary_search_recursive(array ,x ,low ,mid - 1)

def binary_search_recursive(array: list[int] , x: int) ->int:
    return __binary_search_recursive(array ,x ,0 ,len(array))