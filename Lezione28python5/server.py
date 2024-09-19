from flask import Flask, render_template, request

utenti = [
          ["Patricio","NAMO123","0"],
          ["Giovannino","Picante19","0"],
          ["Giordanina","PasswordSicura","0"],
          ["Marietta","MoLoCorco","0"]
          ]




api=Flask("__name__")

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/registrati', methods=['GET'])
def index2():
    nome= request.args.get('fname')
    cognome= request.args.get('lname')
    password=request.args.get('password')
    for i in utenti:
        if nome == i[0] and password in i:
            return render_template('index2.html')

    return render_template('indexko.html')








api.run(host="0.0.0.0", port=8085)

