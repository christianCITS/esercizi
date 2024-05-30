import random
t:int=4
h:int=0

def visualizza_pos(t:int,h:int):
    tracciato:list[str]=["_"]*70
    if t==h:
          print("OUCH")
    for _ in range(len(tracciato)):
          tracciato[t]="T"
          tracciato[h]="H"


          
def tartaruga(pos):
    dado:int=random.randint(1,10)
    if 1<= dado<=5:
           pos+=3
    if 6<= dado <=7:
           pos-=6
    if 8<=dado<=10:
           pos+=1
    return pos   
    


    
def lepre(pos):
      dado:int=random.randint(1,10)
      if 1<= dado<=2:
            pass
      if 3<= dado <=4:
            pos+=9
      if dado==5:
            pos-=12
      if 6<= dado <=8:
            pos +=1
      if 9<= dado <=10:
            pos-=2
      return pos


def gara():
    print("'BANG !!!!! AND THEY'RE OFF !!!!!'")
    while True:
          
            
            
      


      


   




    










