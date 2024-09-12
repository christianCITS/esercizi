create type Strutturato as enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type LavoroProgetto as enum ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');

create type LavoroNonProgettuale as enum ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');

create type CausaAssenza as enum ('Chiusura Universitaria', 'Maternita', 'Malattia');

create domain PosInteger as integer check(value >= 0);

create domain StringaM as varchar(100) not null;

create domain NumeroOre as integer check(value >= 0 and value <=8);

create domain Denaro as integer check(value >= 0);



create table Persona(id PosInteger NOT NULL primary key, nome  StringaM NOT NULL, cognome  StringaM NOT NULL, posizione  Strutturato NOT NULL , stipendio  Denaro NOT NULL);

create table Progetto(id  PosInteger NOT NULL, nome StringaM NOT NULL, inizio  date NOT NULL, fine  date NOT NULL, budget  Denaro NOT NULL, 
                     check (inizio < fine), unique (nome), Primary key (id));


create table WP(progetto  PosInteger NOT NULL, id  PosInteger NOT NULL, nome  StringaM NOT NULL, inizio  date NOT NULL, fine  date NOT NULL, 
               check (inizio < fine), unique (progetto,nome), foreign key (progetto) references Progetto (id), primary key (progetto,id) );


create table AttivitaProgetto(id  PosInteger NOT NULL, persona  PosInteger NOT NULL, progetto  PosInteger NOT NULL, wp  PosInteger NOT NULL, giorno  date NOT NULL, 
                             tipo  LavoroProgetto NOT NULL, oreDurata  NumeroOre NOT NULL, foreign key (persona) references Persona (id), 
                             foreign key (progetto, wp) references WP (progetto,id), primary key (id));


create table AttivitaNonProgettuale(id  PosInteger NOT NULL, persona  PosInteger NOT NULL, tipo  LavoroNonProgettuale NOT NULL, giorno  date NOT NULL, 
                                   oreDurata  NumeroOre NOT NULL, foreign key (persona) references Persona(id), primary key (id));


create table Assenza(id  PosInteger NOT NULL, persona  PosInteger NOT NULL, tipo  CausaAssenza NOT NULL, giorno  date NOT NULL, 
                    unique (persona,giorno), foreign key (persona) references Persona(id), primary key(id));


INSERT INTO Persona (id, nome, cognome, posizione, stipendio) VALUES
(1, 'Franco', 'Righi', 'Ricercatore', 30000),
(2, 'Lorenzo', 'Derti', 'Professore Associato', 45000),
(3, 'Isaia', 'Meloni', 'Professore Ordinario', 55000),
(4, 'Marco', 'Sperti', 'Professore Associato', 40000),
(5, 'Francisco', 'TITTI', 'Ricercatore', 32000);


INSERT INTO Progetto (id, nome, inizio, fine, budget) VALUES
(1, 'Progetto x', '2023-01-01', '2023-12-31', 100000),
(2, 'Progetto y', '2022-03-15', '2023-06-30', 80000),
(3, 'Progetto z', '2021-09-01', '2022-08-31', 60000);


INSERT INTO WP (progetto, id, nome, inizio, fine) VALUES
(1, 1, 'WP1 - Analisi', '2023-01-01', '2023-03-31'),
(1, 2, 'WP2 - Sviluppo', '2023-04-01', '2023-06-30'),
(2, 1, 'WP1 - Ricerca', '2022-03-15', '2022-12-31');


INSERT INTO Assenza (id, persona, causa, giorno) VALUES
(1, 1, 'Malattia', '2023-01-15'),
(2, 2, 'Chiusura Universitaria', '2023-08-01'),
(3, 3, 'Maternita', '2023-07-01');


INSERT INTO AttivitaProgetto (id, persona, progetto, wp, giorno, tipo) VALUES
(1, 1, 1, 1, '2023-02-15', 'Ricerca e Sviluppo'),
(2, 2, 2, 1, '2023-03-20', 'Management');


INSERT INTO AttivitaNonProgettuale (id, persona, giorno, tipo) VALUES
(1, 1, '2023-02-10', 'Didattica'),
(2, 3, '2023-02-15', 'Ricerca'),
(3, 4, '2023-03-01', 'Didattica');



SELECT DISTINCT cognome
FROM Persona
WHERE posizione IN ('Ricercatore', 'Professore Associato', 'Professore Ordinario');


SELECT nome, cognome
FROM Persona
WHERE posizione = 'Ricercatore';


SELECT nome, cognome
FROM Persona
WHERE posizione = 'Professore Associato'
  AND cognome LIKE 'V%';


SELECT nome, cognome
FROM Persona
WHERE posizione IN ('Professore Associato', 'Professore Ordinario')
  AND cognome LIKE 'V%';


SELECT nome
FROM Progetto
WHERE fine < CURRENT_DATE;

SELECT nome
FROM Progetto
ORDER BY inizio ASC;

SELECT nome
FROM WP
ORDER BY nome ASC;


SELECT DISTINCT causa
FROM Assenza
INNER JOIN Persona ON Assenza.persona = Persona.id
WHERE Persona.posizione IN ('Ricercatore', 'Professore Associato', 'Professore Ordinario');


SELECT DISTINCT tipo
FROM AttivitaProgetto
INNER JOIN Persona ON AttivitaProgetto.persona = Persona.id
WHERE Persona.posizione IN ('Ricercatore', 'Professore Associato', 'Professore Ordinario');



SELECT DISTINCT giorno
FROM AttivitaNonProgettuale
WHERE tipo = 'Didattica'
ORDER BY giorno ASC;