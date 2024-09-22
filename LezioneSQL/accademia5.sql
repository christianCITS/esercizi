create type Strutturato as enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario');
create type LavoroProgetto as enum ('Ricerca e Sviluppo', 'Dimostrazione','Management', 'Altro');
create type LavoroNonProgettuale as enum ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro')
create type CausaAssenza as enum ('Chiusura Universitaria', 'Maternita', 'Malattia')
create domain PosInteger as integer check (value >= 0)
create domain StringaM as varchar(100) not null
create domain NumeroOre as integer check(value >= 0 and value  <= 8)
create domain Denaro as real check (value >=0)


create table Persona(id PosInteger NOT NULL primary key, nome StringaM NOT NULL, cognome StringaM NOT NULL, posizione Strutturato NOT NULL, stipendio Denaro NOT NULL)
create table Progetto(id PosInteger NOT NULL, nome StringaM NOT NULL, inizio date NOT NULL, fine date NOT NULL, budget Denaro NOT NULL, 
        unique (nome), check (inizio < fine),Primary key (id))
create table WP (progetto PosInteger NOT NULL, id PosInteger NOT NULL, nome StringaM NOT NULL, inizio date NOT NULL, fine date NOT NULL,
        check (inizio < fine), unique (progetto,nome),foreign key(progetto) references Progetto (id),primary key (progetto,id) )
create table AttivitaProgetto (id PosInteger NOT NULL, persona PosInteger NOT NULL, progetto PosInteger NOT NULL,wp PosInteger NOT NULL, giorno date NOT NULL, tipo LavoroProgetto NOT NULL, oreDurata NumeroOre NOT NULL, 
                foreign key (progetto,wp) references WP (progetto,id),Primary key (id))
create table AttivitaNonProgettuale (id PosInteger NOT NULL, persona PosInteger NOT NULL, tipo LavoroNonProgettuale NOT NULL, giorno date NOT NULL, oreDurata NumeroOre NOT NULL, 
        foreign key (persona) references Persona (id), Primary key (id))
create table Assenza(id PosInteger, persona PosInteger NOT NULL, tipo CausaAssenza NOT NULL, giorno date NOT NULL, 
        unique (persona,giorno),foreign key (persona) references Persona(id), Primary key (id))





--query 1:
SELECT WP.nome, WP.inizio, WP.fine
FROM WP, Progetto
WHERE Progetto.id = WP.progetto
AND Progetto.nome = 'Pegasus';

--query 2:
SELECT DISTINCT Persona.nome, Persona.cognome, Persona.posizione
FROM Persona, AttivitaProgetto, Progetto
WHERE Persona.id = AttivitaProgetto.persona
AND Progetto.id = AttivitaProgetto.progetto
AND Progetto.nome = 'Pegasus'
ORDER BY Persona.cognome DESC;


--query 3
SELECT Persona.nome, Persona.cognome, Persona.posizione
FROM Persona, AttivitaProgetto, Progetto
WHERE Persona.id = AttivitaProgetto.persona
AND Progetto.id = AttivitaProgetto.progetto
AND Progetto.nome = 'Pegasus'
GROUP BY Persona.nome, Persona.cognome, Persona.posizione
HAVING COUNT(AttivitaProgetto.id) > 1;


--query 4:
SELECT DISTINCT Persona.nome, Persona.cognome, Persona.posizione
FROM Persona, Assenza
WHERE Persona.id = Assenza.persona
AND Persona.posizione = 'Professore Ordinario'
AND Assenza.tipo = 'Malattia';


--query 5:
SELECT Persona.nome, Persona.cognome, Persona.posizione
FROM Persona, Assenza
WHERE Persona.id = Assenza.persona
AND Persona.posizione = 'Professore Ordinario'
AND Assenza.tipo = 'Malattia'
GROUP BY Persona.nome, Persona.cognome, Persona.posizione
HAVING COUNT(Assenza.id) > 1;



--query 6:
SELECT DISTINCT Persona.nome, Persona.cognome, Persona.posizione
FROM Persona, AttivitaNonProgettuale
WHERE Persona.id = AttivitaNonProgettuale.persona
AND Persona.posizione = 'Ricercatore'
AND AttivitaNonProgettuale.tipo = 'Didattica';



--query 7:
SELECT Persona.nome, Persona.cognome, Persona.posizione
FROM Persona, AttivitaNonProgettuale
WHERE Persona.id = AttivitaNonProgettuale.persona
AND Persona.posizione = 'Ricercatore'
AND AttivitaNonProgettuale.tipo = 'Didattica'
GROUP BY Persona.nome, Persona.cognome, Persona.posizione
HAVING COUNT(AttivitaNonProgettuale.id) > 1;


--query 8:
SELECT DISTINCT Persona.nome, Persona.cognome
FROM Persona, AttivitaProgetto, AttivitaNonProgettuale
WHERE Persona.id = AttivitaProgetto.persona
AND Persona.id = AttivitaNonProgettuale.persona
AND AttivitaProgetto.giorno = AttivitaNonProgettuale.giorno;


--query 9:
SELECT DISTINCT Persona.nome, Persona.cognome, AttivitaProgetto.giorno, Progetto.nome AS progetto, AttivitaNonProgettuale.tipo, 
AttivitaProgetto.oreDurata AS oreProgettuali, AttivitaNonProgettuale.oreDurata AS oreNonProgettuali
FROM Persona, AttivitaProgetto, AttivitaNonProgettuale, Progetto
WHERE Persona.id = AttivitaProgetto.persona
AND Persona.id = AttivitaNonProgettuale.persona
AND AttivitaProgetto.progetto = Progetto.id
AND AttivitaProgetto.giorno = AttivitaNonProgettuale.giorno;


--query 10:
SELECT DISTINCT Persona.nome, Persona.cognome
FROM Persona, AttivitaProgetto, Assenza
WHERE Persona.id = AttivitaProgetto.persona
AND Persona.id = Assenza.persona
AND AttivitaProgetto.giorno = Assenza.giorno;


--query 11:
SELECT DISTINCT Persona.nome, Persona.cognome, AttivitaProgetto.giorno, Progetto.nome AS progetto, Assenza.tipo, AttivitaProgetto.oreDurata
FROM Persona, AttivitaProgetto, Assenza, Progetto
WHERE Persona.id = AttivitaProgetto.persona
AND Persona.id = Assenza.persona
AND AttivitaProgetto.progetto = Progetto.id
AND AttivitaProgetto.giorno = Assenza.giorno;


--query 12:
SELECT WP.nome
FROM WP
GROUP BY WP.nome
HAVING COUNT(DISTINCT WP.progetto) > 1;





