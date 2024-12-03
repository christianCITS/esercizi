from flask import Flask, json, request, render_template
import random
import os
import dbclient as db
import sys

api = Flask(__name__)
mydb = db.connect()
if mydb is None:
    print("Errore connessione al DB")
    sys.exit()

    
    
@api.route('/read_macchina', methods=['POST'])
def GestisciReadMacchina():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
            dati = request.json[0]
        
            sQuery = f"select * from automobili where modello = '{dati[0]}'and colore='{dati[1]}' "
            iRetValue = db.read_in_db(mydb, sQuery) 
            if iRetValue:
                rows=db.read_all(mydb)
                if rows!= [1,None]:
                    for row in rows[1]:
                        if row["disponibilita" + dati[2]] > 0:
                            print(f"modello:  {row["modello"]}, colore:  {row["colore"]}, è disponibile nella nostra filiale!")
                        else:
                            print(f"modello:  {row["modello"]}, colore:  {row["colore"]},  NON disponibile nella nostra filiale!!!")
                else:
                    print("Nessuna corrispondenza")
    else:
        return 'Content-Type non supportato!'
    



@api.route('/read_motoveicoli', methods=['POST'])
def GestisciReadMoto():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
            dati = request.json[0]
        
            sQuery = f"select * from motoveicoli where modello = '{dati[0]}'and colore='{dati[1]}' "
            iRetValue = db.read_in_db(mydb, sQuery) 
            if iRetValue:
                rows=db.read_all(mydb)
                if rows!= [1,None]:
                    for row in rows[1]:
                        if row["disponibilita" + dati[2]] > 0:
                            print(f"modello:  {row["modello"]}, colore:  {row["colore"]}, è disponibile nella nostra filiale!")
                        else:
                            print(f"modello:  {row["modello"]}, colore:  {row["colore"]},  NON disponibile nella nostra filiale!!!")
                else:
                    print("Nessuna corrispondenza")
    else:
        return 'Content-Type non supportato!'
    

api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')