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

def cercaAutomobile():
    for k, v in user.items():
        sQuery = f"select privilegi from utenti where username = '{k}' and password = '{v[0]}';"
        print(sQuery)
        iNumRecord = db.read_in_db(mydb, sQuery)
        if iNumRecord == 1:
            lRecord = db.read_next_row(mydb)
            iStato = lRecord[1][0]
            if iStato == 1:
                return iStato
        return False

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if controllo_privilegi_admin(accesso) == 1:
            for key, value in request.json.items():
                sQuery = f"insert into cittadini(codfis, nome, cognome, data_nascita) values ('{key}', '{value['nome']}', '{value['cognome']}', '{value['dataNascita']}')"
                iRetValue = db.write_in_db(mydb, sQuery)
                if iRetValue == -2:
                    return "Nome utente già in uso"
                elif iRetValue == 0:
                    return "Registrazione avvenuta con successo"
                else:
                    return "Errore non gestito nella registrazione"
            return "Errore richiesta formulata non correttamente"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
    
@api.route('/read_cittadino', methods=['POST'])
def GestisciReadCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if controllo_privilegi_admin(accesso) == 1:
            sQuery = f"select * from cittadini where codfis = '{dati[0]}'"
            iRetValue = db.read_in_db(mydb, sQuery) 
            if iRetValue == 1:
                return db.read_next_row(mydb)
            return "Cittadino non trovato"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/update_cittadino', methods=['POST'])
def GestisciUpdateCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if controllo_privilegi_admin(accesso) == 1:
            sQuery = f"select * from cittadini where codfis = '{dati[0]}'"
            iRetValue = db.read_in_db(mydb, sQuery) 
            if iRetValue != 1:
                return db.read_next_row(mydb)
            for i in range(len(dati) -1):
                if dati[i+1]:
                    if i + 1 == 1:
                        sQuery = f"update cittadini set nome = '{dati[i+1]}' where codfis = '{dati[0]}'"
                        db.write_in_db(mydb, sQuery)
                    elif i + 1 == 2:
                        sQuery = f"update cittadini set cognome = '{dati[i+1]}' where codfis = '{dati[0]}'"
                        db.write_in_db(mydb, sQuery)
                    elif i + 1 == 3:
                        sQuery = f"update cittadini set data_nascita = '{dati[i+1]}' where codfis = '{dati[0]}'"
                        db.write_in_db(mydb, sQuery)
            return "Modifica avvenuta con successo"   
        else:
            return "Dati errati"     
    else:
        return 'Content-Type not supported!'

@api.route('/delete_cittadino', methods=['POST'])
def GestisciDeleteCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if controllo_privilegi_admin(accesso):
            sQuery = f"delete from cittadini where codfis = '{dati}'"    
            db.write_in_db(mydb, sQuery)
            return "Eliminazione avvenuta con successo"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        iStato = -1
        for key, value in request.json.items():
            sQuery = f"select privilegi from utenti where username = '{key}' and password = '{value[0]}';"
            print(sQuery)
            iNumRecord = db.read_in_db(mydb, sQuery)
            if iNumRecord == 1:
                print("Login terminato correttamente")
                lRecord = db.read_next_row(mydb)
                iStato = lRecord[1][0]
                return '{"Esito":"ok", "Stato": ' + str(iStato) + '}'
            elif iNumRecord == 0:
                print("Credenziali errate")
                return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
            elif iNumRecord <= -1:
                print("Dati errati")
                return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
            else:
                print("Attenzione: attacco in corso")
                return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
    else:
        return 'Content-Type not supported!'

@api.route('/registrazione', methods=['POST'])
def Registrazione():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        for key, value in request.json.items():
            sQuery = f"insert into utenti(username,password,privilegi) values ('{key}', '{value[0]}',{random.randint(0,1)})"
            print(sQuery)
            iRetValue = db.write_in_db(mydb, sQuery) #restituisce 0 se è andato tutto bene, -1 errore, -2 duplicate key
            print(iRetValue)
            if iRetValue == -2:
                return "Nome utente già in uso"
            elif iRetValue == 0:
                return "Registrazione avvenuta con successo"
            else:
                return "Errore non gestito nella registrazione"
        return "Errore richiesta non conforme"
    else:
        return 'Content-Type not supported!'

api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')