def serializzazione(mylist_1):
    mylist_1 = mylist_1.strip('[]')
    lista = mylist_1.split(',')
    
    ris= []
    
    for e in lista:
        a= e.strip("'")
        ris.append(a)
    
    return ris

def deserializzazione(mylist_2):
    punt = '['
    
    for i in range(len(mylist_2)):
        element = mylist_2[i]
        punt += "'" + element + "'"
        if i < len(mylist_2) - 1:
            punt += ', '
    
    punt += ']'
    
    return punt

mylist_1 = "['mario', 'gino', 'lucrezia']"
mylist_2 = ['mario', 'gino', 'lucrezia']

listaConvertita = serializzazione(mylist_1)
print("Stringa a Lista:", listaConvertita)

stringaConvertita = deserializzazione(mylist_2)
print("Lista a Stringa:", stringaConvertita)
