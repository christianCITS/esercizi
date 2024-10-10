import sys
import os
import os.path
import time


import dbclient as db


print("Inizio programma prova database")
cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	sys.exit()



sQuery= "insert into cittadini (codFisc, nome, cognome, dataNascita) values ('KSSMRA85M01H501Z', 'Mario', 'Rossi', '1985-01-15')"
db.write_in_db(cur,sQuery)

sQuery = "select * from cittadini;"
iNumRows = db.read_in_db(cur,sQuery)
for ii in range(0,iNumRows):
	myrow = db.read_next_row(cur)
	print(myrow)
	