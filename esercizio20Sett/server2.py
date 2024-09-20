from flask import Flask, render_template, request

utenti = [["pinco","pallo","123"],["pinco2","pallo","123"]]

api=Flask("__name__")

@api.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/ordini_old', methods=['GET'])
def ordiniold():
    return render_template('ordiniold.html')


@api.route('/ordini_new', methods=['GET'])
def ordininew():
    return render_template('ordininew.html')





@api.route('/gestisci_login', methods=['GET'])
def accedi():
    nome= request.args.get('fname')
    cognome= request.args.get('lname')
    password=request.args.get('password')
    for utente in utenti:
        if nome==utente[0] and cognome==utente[1] and password==utente[2]:
            return render_template('lista_servizi.html')
    return render_template('lista_servizi.html')

@api.route('/registrazione', methods=['GET'])
def registrazione():
    nome= request.args.get('fname')
    cognome= request.args.get('lname')
    password=request.args.get('password')
    return render_template('registrazione.html')

@api.route('/benvUtente', methods=['GET'])
def benvUtente():
    return render_template('benvUtente.html')






api.run(host="0.0.0.0", port=8085)

