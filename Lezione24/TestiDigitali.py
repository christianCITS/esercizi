class Documento:
    def __init__(self,testo:str):
        self.testo=testo



    def setText(self,ntesto:str):
        self.testo=ntesto


    def getText(self):
        return self.testo
    


    def isinText(self,keyword:str):
        if keyword in self.testo:
            return True
        

    
class Email(Documento):
    def __init__(self, testo: str,mittente:str,destinatario:str,titolo_messaggio:str):
        super().__init__(testo)
        self.mittente=mittente
        self.destinatario=destinatario
        self.titolo_messaggio=titolo_messaggio
    
    def setMittente(self,mittente:str):
        self.mittente=mittente

    def setDestinatario(self,destinatario:str):
        self.destinatario=destinatario
    
    def setTitoloMess(self,tit_mess:str):
        self.titolo_messaggio=tit_mess
    
    def getMittente(self):
        return self.mittente

    def getDestinatario(self):
        return self.destinatario
    
    def getTitoloMess(self):
        return self.titolo_messaggio

    def getText(self):
        return f"Da:{self.getMittente()}, A:{self.getDestinatario()}\nTitolo:{self.getTitoloMess()}\nMessaggio:{self.testo}"


    def WriteToFile(self,percorso:str):
        with open(percorso, "w") as  file:
            testo=self.getText()
            file.write(testo)
            



class File(Documento):
    def __init__(self, nome_percorso:str):
        self.nome_percorso=nome_percorso
        super().__init__(self.leggiTestoDaFile())
        
    

    def leggiTestoDaFile(self):
        with open(self.nome_percorso,"r") as pagina:
            return pagina.read()
    
    
    def getText(self):
        return f"Percorso:{self.nome_percorso}\nContenuto:{self.testo}"
    



email=Email("questo è il testo della mail","Ambrogio","Ambrogina","Messaggino")
file=File('Lezione24/document.txt')

print(email.getText())
print("#"*40)
print(file.getText())




    

    

    
        
