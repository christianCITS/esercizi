#Prima lezione Python 5
import os
import PyPDF2

def CercaParolaInNomeFile(parola,file):
    a = file.lower()
    b = parola.lower()

    risp = a.find(b)

    if risp >= 0:
        return True

    return False


def CercaParolaInContenutoFile(parola,pathfile):
    sFilename, sFileext = os.path.splitext(pathfile)
    asganaflow = False

    if sFileext.lower() == ".txt":
        asganaflow = CercaParolaInFileTxt(parola,pathfile)

    if sFileext.lower() == ".pdf":
        asganaflow = CercaParolaInFilePdf(parola,pathfile) 

    return asganaflow


def CercaParolaInFileTxt(parola,pathfile):
    with open (pathfile,"r") as file:
        sLine = file.readline()

        while(len(sLine)>0):

            rip = sLine.lower().find(parola.lower())

            if rip >= 0:

                return True

            sLine =file.readline()

    return False


def CercaParolaInFilePdf(parola,pathfile):
    pdf = PyPDF2.PdfFilereader(file)
    numPag = len(pdf.pages)

    print(f"Il file {pathfile} contiene {numPag}")

    for i in range(0,numPag):

        pagei = pdf.pages[i]
        text = pagei.extract_text()
        ira = text.lower().find(parola.lower())

        if ira >= 0:
            return True

    return False




sRoot = input("Inserisci la directory dove cercare")
sParola = input("Inserisci la parola da cercare")
sOutDir = input("Inserisci la directory dove mettere i file trovati")
for root, ListDir, ListFiles in os.walk(sRoot):

    print(f"Nella directory {root} ci sono {len(ListDir)} sottodirectory e {len(ListFiles)} file")

    for file in ListFiles:

        print(f"Devo cercare {sParola} in {file}")

        bRet = CercaParolaInNomeFile(sParola, file)

        if bRet == True:
            print(f"La parola {sParola} c'é nel file {file}")

        else:
            sFilePathCompleto = os.path.join(root,file)
            bRet = CercaParolaInContenutoFile(sParola, sFilePathCompleto)

            if bRet == True:
                print(f"Trovata parola all'interno del file {file}")
