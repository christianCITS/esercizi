import os

sRoot= input("Inserisci la directory dove cercare")
sParola= input("Inserisci la parola da cercare")
sOutDir= input("Inserisci la directory dove mettere i file trovati")


for root,ListDir,ListFiles in os.walk(sRoot):
    print(f"Nella directory {root} ci sono {len(ListDir)} sottodirectory e {len(ListFiles)} file.")
    for file in ListFiles:
        print(f"Devo cercare {sParola} in {file}")
        test=cercaParolaInNomeFile()
        if test== True:
            print(f"La parola {sParola} c'è nel file: {file}.")
        else:
            pathCompleto= os.path.join(root,file) 
           # test= creare funzione e metterla qui : cercaParoleinContenutoFile(pathCompl,sParola
            pass






        def cercaParolaInNomeFile(file,sParola):
            a=file.lower()
            b=sParola.lower()
            ret=a.find(b)
            if ret >= 0:
                return True
            elif ret < 0:
                return False
            








            


            
            
            


    


