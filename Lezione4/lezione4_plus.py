
#funzione che sottrae ad una lista di numeri (x) un numero inizializzat a y(10 in questo caso )
#e ritorna il risultat 
def subtract_all(x:list[float],y:list[float])->list[float]:

    ris:list=[]
    for n in x:
         sot:float=n-y
         ris.append(sot)
    return ris
         




mylist:list[float]=[1,2,3,4,5]
y:float=10
result=subtract_all(mylist,y)
#print(result)



#funzione che sottrae gli elementi da due liste con uguale numero di elementi e restituisce i risultati all'interno di u
# un'altra lista vuota 

def sottra_piu_liste(x:list[float],y:list[float])->list[float]:
    listav:list=[]    
    for el in range(len(x)):
               op:list=x[el]-y[el]
               listav.append(op)
    return listav

     
        


lis=[2,3,4,5,6]       

#print(sottra_piu_liste(mylist,lis))








s:str="La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."
def counter(s:str) -> list[int]:
      testo:list=[]
      testo.append(len(s))
      testo.append(len(s.split()))
      #testo[2] =
      testo.append(len(s.split('.'))) 
      return testo

#creo diz vuoto poi con s replace tolgo punti e punteggiature creo lista "parollee" e ci mettodentro il contenuto dlla stringa (s) che ho anche splittato
#con un ciclo for dico Se gli elementi nella lista parole non sono ancora stati visti segnali, altrimenti aggiungi a somma
def word_count(s:str) -> dict[str,int]:
      wordfl:dict[str,int]={}
      word:dict[str,int]={}
      s=s.replace(',','').replace(';','').replace('.','')
      parolee:list[str]=s.split()
      for p in parolee:
            if p not in word:
                  word[p]=1
            else:
                  word[p]+=1
 #con il secono for scandiamo il diz e gli diciamo che SE e' presente più di una volta all'interno aggiungiamolo ad un altro diz appena creato
      for k,v in word.items():
            if v >1:
                  wordfl[k]= v
      return wordfl, word



#print(word_count(s))












st:str="Amo Roma?"

def is_palindrome(s:str) -> bool:
      s:str=st.lower().replace(' ','').strip('?')
      i:int=0
      while i<len(s):
         j=len(s) -(i+1)
         if s[i]!=s[j]:
               return False
         i+=1
         return True
      




print(is_palindrome(st))
                
           
         

      
             
             

                  
                  
                  
                  
                  
                  
                  
                  
print(is_palindrome(st))
                  






            









     













 
          