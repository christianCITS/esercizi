import requests
import sys

base_url = "http://127.0.0.1:8080"

filiali = {
    1: {"partita_iva": "12345678901", "indirizzo": "Via Roma 1", "civico": 1},
    2: {"partita_iva": "98765432101", "indirizzo": "Piazza Garibaldi 2", "civico": 2},
    3: {"partita_iva": "19283746501", "indirizzo": "Viale Milano 3", "civico": 3},
    4: {"partita_iva": "56473829102", "indirizzo": "Corso Venezia 4", "civico": 4}
}

def verifica_filiale(numero_filiale):
    if numero_filiale in filiali:
        return filiali[numero_filiale]  
    return None  

def cerca_casa_vendita():
    numero_filiale = int(input("Inserisci il numero della filiale (1, 2, 3, 4): "))
    filiale = verifica_filiale(numero_filiale)
    if not filiale:
        print("Filiale non valida!")
        return

    metri_min = input("Inserisci i metri quadrati minimi: ")
    prezzo_max = input("Inserisci il prezzo massimo: ")
    stato = input("Inserisci lo stato (LIBERO, OCCUPATO): ")

    requisiti = {
        "metri_min": metri_min,
        "prezzo_max": prezzo_max,
        "stato": stato,
        "filiale": {str(filiale["partita_iva"]): {"indirizzo": filiale["indirizzo"], "civico": filiale["civico"]}}
    }

    response = requests.post(f"{base_url}/cerca_casa_vendita", json=requisiti)

    if response.status_code == 200:
        print("Risultato della ricerca:", response.json())
    else:
        print("Errore durante la ricerca della casa.")

def cerca_casa_affitto():
    numero_filiale = int(input("Inserisci il numero della filiale (1, 2, 3, 4): "))
    filiale = verifica_filiale(numero_filiale)
    if not filiale:
        print("Filiale non valida!")
        return

    tipo_affitto = input("Inserisci il tipo di affitto (PARZIALE, TOTALE): ")
    prezzo_max = input("Inserisci il prezzo massimo mensile: ")

    requisiti = {
        "tipo_affitto": tipo_affitto,
        "prezzo_max": prezzo_max,
        "filiale": {str(filiale["partita_iva"]): {"indirizzo": filiale["indirizzo"], "civico": filiale["civico"]}}
    }

    response = requests.post(f"{base_url}/cerca_casa_affitto", json=requisiti)

    if response.status_code == 200:
        print("Risultato della ricerca:", response.json())
    else:
        print("Errore durante la ricerca della casa.")

def vendere_casa():
    numero_filiale = int(input("Inserisci il numero della filiale venditrice (1, 2, 3, 4): "))
    filiale = verifica_filiale(numero_filiale)
    if not filiale:
        print("Filiale non valida!")
        return

    catastale = input("Inserisci il codice catastale della casa: ")
    prezzo_vendita = input("Inserisci il prezzo di vendita: ")

    filiale_venditrice = input("Inserisci la partita IVA della filiale venditrice: ")

    requisiti = {
        "catastale": catastale,
        "prezzo_vendita": prezzo_vendita,
        "filiale_venditrice": filiale_venditrice,
        "filiale": {str(filiale["partita_iva"]): {"indirizzo": filiale["indirizzo"], "civico": filiale["civico"]}}
    }

    response = requests.post(f"{base_url}/vendi_casa", json=requisiti)

    if response.status_code == 200:
        print("Casa venduta con successo:", response.json())
    else:
        print("Errore durante la vendita della casa.")

def affittare_casa():
    numero_filiale = int(input("Inserisci il numero della filiale che propone la casa (1, 2, 3, 4): "))
    filiale = verifica_filiale(numero_filiale)
    if not filiale:
        print("Filiale non valida!")
        return

    filiale_venditrice = input("Inserisci la partita IVA della filiale venditrice: ")
    catastale = input("Inserisci il codice catastale della casa: ")
    prezzo_affitto = input("Inserisci il prezzo di affitto mensile: ")
    durata = input("Inserisci la durata del contratto (in mesi, ad esempio '12 months'): ")

    requisiti = {
        "filiale": {str(filiale["partita_iva"]): {"indirizzo": filiale["indirizzo"], "civico": filiale["civico"]}},
        "catastale": catastale,
        "prezzo_affitto": prezzo_affitto,
        "durata": durata,
        "filiale_venditrice": filiale_venditrice
    }

    response = requests.post(f"{base_url}/affitta_casa", json=requisiti)

    if response.status_code == 200:
        print("Casa affittata con successo:", response.json())
    else:
        print("Errore durante l'affitto della casa.")

def main():
    while True:
        print("\nOperazioni disponibili:")
        print("1. Cerco un immobile in vendita")
        print("2. Cerco una casa in affitto")
        print("3. Voglio vendere casa")
        print("4. Voglio affittare casa")
        print("5. Esci")
        
        scelta = input("Cosa vuoi fare? ")
        
        if scelta == "1":
            cerca_casa_vendita()
        elif scelta == "2":
            cerca_casa_affitto()
        elif scelta == "3":
            vendere_casa()
        elif scelta == "4":
            affittare_casa()
        elif scelta == "5":
            print("Arrivederci!")
            sys.exit()
        else:
            print("Errore: Inserire un operazione valida!")

if __name__ == "__main__":
    main()
