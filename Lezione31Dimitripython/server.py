from flask import Flask, json, request
from Lezione32Dimitripython.myjson import JsonSerialize,JsonDeserialize


sAnagrafe = "./anagrafe.json"
api = Flask(__name__)

listaCitt=[
  {
    "nome": "Luca",
    "cognome": "Rossi",
    "data_nascita": "1985-04-15",
    "codice_fiscale": "RSSLCU85D15H501F"
  },
  {
    "nome": "Giulia",
    "cognome": "Bianchi",
    "data_nascita": "1990-09-22",
    "codice_fiscale": "BNCGLI90P62F205T"
  },
  {
    "nome": "Marco",
    "cognome": "Verdi",
    "data_nascita": "1978-12-03",
    "codice_fiscale": "VRDMRC78T03L219Y"
  },
  {
    "nome": "Chiara",
    "cognome": "Esposito",
    "data_nascita": "1995-07-11",
    "codice_fiscale": "SPSCHR95L51E472U"
  },
  {
    "nome": "Alessandro",
    "cognome": "Ferri",
    "data_nascita": "1983-02-27",
    "codice_fiscale": "FRRLSS83B27L736D"
  }
]


#la chiave è il codice fiscale



@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale not in anagrafe:
            dNuovoCittadino = jsonReq
            anagrafe[sCodiceFiscale] = dNuovoCittadino
            JsonSerialize(anagrafe,sAnagrafe)
            jsonResp = {"Esito":"000", "Msg":"ok"}
            return json.dumps(jsonResp),200
        else:
            jsonResp = {"Esito":"001", "Msg":"Cittadino gia presente"}
            return json.dumps(jsonResp),200
    else:
        return 'Content-Type not supported!',401
    


@api.route('/read_cittadino', methods=['POST'])
def ReadCittadino(cf):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        for diz in listaCitt:
            for v in diz.values():
                if v == cf:
                    cittadino=diz

        if cittadino:
            return json.dumps(cittadino)
        else:
            return json.dumps({"Esito": "404", "Msg": "Cittadino non trovato"})
        
        



@api.route('/update_cittadino', methods=['PUT'])
def GestisciUpdateCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale in anagrafe:
            anagrafe[sCodiceFiscale] = jsonReq
            JsonSerialize(anagrafe, sAnagrafe)
            jsonResp = {"Esito": "000", "Msg": "Cittadino aggiornato"}
            return json.dumps(jsonResp), 200
        else:
            jsonResp = {"Esito": "002", "Msg": "Cittadino non trovato"}
            return json.dumps(jsonResp), 200
    else:
        return 'Content-Type not supported!', 401
             
    
    

        

@api.route('/delete_cittadino', methods=['POST'])
def DeleteCittadino(cf):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        for diz in listaCitt:
            for v in diz.values():
                if v== cf:
                    listaCitt.remove(diz)
                    return json.dumps({"Esito": "200", "Msg": "Cittadino cancellato con successo"})
        else:
            return json.dumps({"Esito": "404", "Msg": "Cittadino non trovato"})
    else:
        return 'Content-Type non supportato!'




api.run(host="127.0.0.1", port=8080)
