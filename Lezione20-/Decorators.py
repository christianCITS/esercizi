import time
import random
from concurrent.futures import ThreadPoolExecutor





'''

def saluta(func):
    func("Flavio")

saluta(sayHello)




def parent():
    print(f"sonio in parent")

    def firstChild():
        print(f"sono in firstchild")
    
    def seconChild():
        print(f"sono in second child")'''




''''def getTime(func):
    def wrapper(*args):
        start=time.time()

        func(*args)

        end=time.time()
        elapsed_time= end - start
        print(f"{elapsed_time}")


    return wrapper

@getTime
def sayHello(name:str)-> None:
    print(f"Hello {name}")
@getTime
def randomList(upper_bound:int):


    sleep_time:int=random.randint(0,upper_bound)
    time.sleep(sleep_time)





sayHello("Flavio")

randomList(10)




def generatore():
    yield "A"
    yield "B"
    yield "C"



prova_generatore=generatore()


print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))'''



def funzione(id:int):
    import time
    import random


    sleep_time:int=random.randint(1,10)
    print(f"{id=} time {time.time()}")
    time.sleep(sleep_time)
    print(f"{id=} time {time.time()}")

if __name__=="__main__":
    import threading
    lista_thread:list[threading.Thread]=[]
    for id in range(3):

        x:threading.Thread=threading.Thread(target=funzione, args=(1,))
        lista_thread.append(x)
        print(f"Prima fi runnare il thread {time.time()}")
        x.start()
        print(f"Ho runnato il thread {time.time()}")
        

    for t in lista_thread:
        t.join()
        print(f"Termionato!!")





#IMPORTANTISSIMO PER CREARE PIU THREADS
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(funzione,range(10))





    



