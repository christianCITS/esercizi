from flask import Flask, request
import dbclient as db
import sys
import json

api = Flask(__name__)
db_conn = db.connect()
if db_conn is None:
    print("Errore nella connessione al database")
    sys.exit()

# Mappa delle filiali, basata sul numero della filiale (1, 2, 3, 4)
filiali = {
    1: {"partita_iva": "12345678901", "indirizzo": "Via Roma 1", "civico": 1},
    2: {"partita_iva": "98765432101", "indirizzo": "Piazza Garibaldi 2", "civico": 2},
    3: {"partita_iva": "19283746501", "indirizzo": "Viale Milano 3", "civico": 3},
    4: {"partita_iva": "56473829102", "indirizzo": "Corso Venezia 4", "civico": 4}
}

# Funzione per verificare la filiale con il numero fornito
def verifica_filiale(numero_filiale: int):
    if numero_filiale in filiali:
        filiale = filiali[numero_filiale]
        query = f"""
        SELECT * 
        FROM filiali 
        WHERE partita_iva = '{filiale['partita_iva']}' 
        AND indirizzo_sede = '{filiale['indirizzo']}' 
        AND civico = {filiale['civico']}
        """
        if db.read_in_db(db_conn, query) > 0:
            return True
    return False

@api.route('/cerca_casa_vendita', methods=['POST'])
def cerca_casa_vendita():
    if request.headers.get('Content-Type') == 'application/json':
        dati_richiesta = request.json
        numero_filiale = dati_richiesta['filiale']
        
        if verifica_filiale(numero_filiale):
            condizioni = []
            if 'metri_min' in dati_richiesta: 
                condizioni.append(f"metri >= {dati_richiesta['metri_min']}")
            if 'prezzo_max' in dati_richiesta:
                condizioni.append(f"prezzo <= {dati_richiesta['prezzo_max']}")
            if 'stato' in dati_richiesta:
                condizioni.append(f"stato = '{dati_richiesta['stato']}'")
            
            filtro = " AND ".join(condizioni) 
            query = f"SELECT * FROM case_in_vendita WHERE {filtro}"
            n_risultati = db.read_in_db(db_conn, query)
            if n_risultati > 0:
                case = []
                for _ in range(n_risultati):
                    row = db.read_next_row(db_conn)
                    case.append({
                        'catastale': row[0],
                        'indirizzo': row[1],
                        'numero_civico': row[2],
                        'piano': row[3],
                        'metri': row[4],
                        'vani': row[5],
                        'prezzo': row[6],
                        'stato': row[7],
                        'filiale_proponente': row[8]
                    })
                return {'case_vendita': case}
            else:
                return {'esito': 'Nessuna corrispondenza per la casa in vendita'}
        return {'errore': 'La filiale non è valida!'}
    return {'errore': 'Content-Type non supportato'}

@api.route('/cerca_casa_affitto', methods=['POST'])
def cerca_casa_affitto():
    if request.headers.get('Content-Type') == 'application/json':
        dati_richiesta = request.json
        numero_filiale = dati_richiesta['filiale']
        
        if verifica_filiale(numero_filiale):
            condizioni = []
            if 'tipo_affitto' in dati_richiesta:
                condizioni.append(f"tipo_affitto = '{dati_richiesta['tipo_affitto']}'")
            if 'prezzo_max' in dati_richiesta:
                condizioni.append(f"prezzo_mensile <= {dati_richiesta['prezzo_max']}")
            
            filtro = " AND ".join(condizioni) if condizioni else "TRUE"
            query = f"SELECT * FROM case_in_affitto WHERE {filtro}"
            n_risultati = db.read_in_db(db_conn, query)
            if n_risultati > 0:
                case = []
                for _ in range(n_risultati):
                    r = db.read_next_row(db_conn)
                    case.append({
                        'catastale': r[0],
                        'indirizzo': r[1],
                        'numero_civico': r[2],
                        'tipo_affitto': r[3],
                        'bagno_personale': r[4],
                        'prezzo_mensile': r[5],
                        'filiale_proponente': r[6]
                    })
                return {'case_affitto': case}
            else:
                return {'esito': 'Nessuna casa trovata'}
        return {'errore': 'La filiale non è valida!'}
    return {'errore': 'Content-Type non supportato'}

@api.route('/vendi_casa', methods=['POST'])
def vendi_casa():
    if request.headers.get('Content-Type') == 'application/json':
        dati_richiesta = request.json
        numero_filiale = dati_richiesta['filiale']
        catastale = dati_richiesta['catastale']
        prezzo_vendita = dati_richiesta['prezzo_vendita']
        filiale_venditrice = dati_richiesta['filiale_venditrice']
        
        if verifica_filiale(numero_filiale):
            query = f"SELECT * FROM case_in_vendita WHERE catastale = '{catastale}' AND stato = 'LIBERO'"
            if db.read_in_db(db_conn, query) == 1:
                query_vendi = f"""
                    INSERT INTO vendite_casa (catastale, data_vendita, filiale_proponente, filiale_venditrice, prezzo_vendita)
                    VALUES ('{catastale}', current_date, '{numero_filiale}', '{filiale_venditrice}', {prezzo_vendita});
                """
                db.write_in_db(db_conn, query_vendi)
                return {'esito': 'La casa è stata venduta!'}
            return {'errore': 'La casa non è disponibile!'}
        return {'errore': 'Inserire una filiale valida!'}
    return {'errore': 'Content-Type non supportato'}

@api.route('/affitta_casa', methods=['POST'])
def affitta_casa():
    if request.headers.get('Content-Type') == 'application/json':
        dati_richiesta = request.json
        numero_filiale = dati_richiesta['filiale']
        catastale = dati_richiesta['catastale']
        prezzo_affitto = dati_richiesta['prezzo_affitto']
        durata = dati_richiesta['durata']
        filiale_venditrice = dati_richiesta['filiale_venditrice']
        
        if verifica_filiale(numero_filiale):
            query = f"SELECT * FROM case_in_affitto WHERE catastale = '{catastale}'"
            if db.read_in_db(db_conn, query) == 1:
                query_affitta = f"""
                    INSERT INTO affitti_casa (catastale, data_affitto, filiale_proponente, filiale_venditrice, prezzo_affitto, durata_contratto)
                    VALUES ('{catastale}', current_date, '{numero_filiale}', '{filiale_venditrice}', {prezzo_affitto}, {durata});
                """
                db.write_in_db(db_conn, query_affitta)
                return {'esito': 'La casa è stata affittata!'}
            return {'errore': 'La casa non è disponibile!'}
        return {'errore': 'Inserire una filiale valida!'}
    return {'errore': 'Content-Type non supportato'}

if __name__ == '__main__':
    api.run(host='127.0.0.1', port=8080)
