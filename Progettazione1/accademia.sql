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














