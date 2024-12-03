import requests,json
import sys

base_url = "https://127.0.0.1:8080"
auth = False

def GetDatiVeicolo():
    modello = input("Qual'è il modello? ")
    colore = input("Di che colore?")
    filiale = input("Qual'è la filiale ")
    


while True:
    if not auth:
        print("Operazioni disponibili:")
        print("1. cerca automobile")
        print("2. cerca motoveicolo")
        print("3. Esci")
        
       
        
        
