import random
t:int=0
h:int=0

def visualizza_pos(t:int,h:int):
    tracciato:list[str]=["_"]*70
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while True:
              for e in range(len(tracciato)):
                     tracciato[t]="T"
                     tracciato[h]="H"
                     if tracciato[e]=="T":
                           
      

              pas_t:int=tartaruga()
              pas_h:int=lepre()
                     
              
              
              
              

    

       

          
def tartaruga():
    pos:int=0
    dado:int=random.randint(1,10)
    if 1<= dado<=5:
           pos+=3
    if 6<= dado <=7:
           pos-=6
    if 8<=dado<=10:
           pos+=1
    return pos   
    


    
def lepre():
      dado:int=random.randint(1,10)
      pos:int=0
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


'''print(tartaruga())
print(lepre())'''


print(visualizza_pos(t,h))


            
      


      


   




    










