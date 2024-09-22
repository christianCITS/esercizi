create domain PosInteger as integer check (value >= 0)
create domain StringaM as varchar(100) not null
create domain CodIATA as char (3) not null


create table Volo (codice PosInteger NOT NULL primary key, comp StringaM NOT NULL primary key, durataMinuti PosInteger NOT NULL, foreign key(comp) references Compagnia(nome),foreign key(codice,comp) references ArrPart(codice,comp))
create table ArrPart (codice PosInteger NOT NULL primary key, comp StringaM NOT NULL primary key, arrivo CodIATA NOT NULL, partenza CodIATA NOT NULL, check (arrivo > partenza), foreign key(codice, comp) references Volo(codice, comp),foreign key(arrivo) references Aeroporto(codice),foreign key(partenza) references Aeroporto(codice) )
create table Aeroporto (codice CodIATA NOT NULL primary key, nome StringaM, foreign key(codice) references LuogoAeroporto(aeroporto))


--query 1:
SELECT  Volo.codice, Volo.comp
FROM Volo
WHERE Volo.durataMinuti > 180;

--query 2:
SELECT Volo.comp
FROM Volo
WHERE Volo.durataMinuti > 180;

--query 3:
SELECT DISTINCT ArrPart.codice, ArrPart.comp
FROM ArrPart
WHERE ArrPart.partenza = 'CIA';


--query 4:
SELECT DISTINCT ArrPart.comp
FROM ArrPart
WHERE ArrPart.arrivo = 'FCO';

--query 5:
SELECT DISTINCT ArrPart.codice, ArrPart.comp
FROM ArrPart
WHERE ArrPart.partenza = 'FCO' AND ArrPart.arrivo = 'JFK';

--query 6:
SELECT DISTINCT ArrPart.comp
FROM ArrPart
WHERE ArrPart.partenza = 'FCO' AND ArrPart.arrivo = 'JFK';

--query 7:
SELECT DISTINCT ArrPart.comp
FROM ArrPart, Aeroporto A1, Aeroporto A2, LuogoAeroporto L1, LuogoAeroporto L2
WHERE ArrPart.partenza = A1.codice
AND A1.codice = L1.aeroporto
AND L1.citta = 'Roma'
AND ArrPart.arrivo = A2.codice
AND A2.codice = L2.aeroporto
AND L2.citta = 'New York';

--query 8:
SELECT DISTINCT A.codice, A.nome, L.citta, L.nazione
FROM ArrPart, Aeroporto A, LuogoAeroporto L
WHERE ArrPart.partenza = A.codice
AND A.codice = L.aeroporto
AND ArrPart.comp = 'MagicFly';

--query 9:
SELECT DISTINCT ArrPart.codice, ArrPart.comp, ArrPart.partenza, ArrPart.arrivo
FROM ArrPart, Aeroporto A1, Aeroporto A2, LuogoAeroporto L1, LuogoAeroporto L2
WHERE ArrPart.partenza = A1.codice
AND A1.codice = L1.aeroporto
AND L1.citta = 'Roma'
AND ArrPart.arrivo = A2.codice
AND A2.codice = L2.aeroporto
AND L2.citta = 'New York';




--query 11:
SELECT DISTINCT V1.comp
FROM ArrPart V1, Compagnia C
WHERE V1.partenza = 'FCO'
AND V1.arrivo = 'JFK'
AND V1.comp = C.nome
AND C.annoFondaz IS NOT NULL;




