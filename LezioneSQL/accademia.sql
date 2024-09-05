create domain Strutturato as enum (’Ricercatore’, ’Professore Associato’, ’Professore Ordinario’)
create domain LavoroProgetto as enum (’Ricerca e Sviluppo’, ’Dimostrazione’, ’Management’, ’Altro’)
create domain LavoroNonProgettuale as enum (’Didattica’, ’Ricerca’, ’Missione’, ’Incontro Dipartimentale’, ’Incontro Accademico’, ’Altro’)
create domain CausaAssenza as enum (’Chiusura Universitaria’, ’Maternita’, ’Malattia’)
create domain PosInteger as integer check (value ≥ 0)
create domain StringaM as varchar(100) not null
create domain NumeroOre as integer check(value >= 0 and value  <= 8)
create domain Denaro as real check (value >=0)


create table Persona(id: PosInteger, nome: StringaM, cognome: StringaM, posizione: Strutturato, stipendio: Denaro)
create table Progetto(id: PosInteger, nome: StringaM, inizio: date, fine: date, budget:Denaro, unique (nome), check (inizio < fine) )
create table WP (progetto: PosInteger, id: PosInteger, nome: StringaM, inizio: date, fine: date,check (inizio < fine) unique (progetto < nome),foreign key(progetto) references Progetto (id) )
create table AttivitaProgetto (id: PosInteger, persona: PosInteger, progetto: PosInteger,wp: PosInteger, giorno: date, tipo: LavoroProgetto, oreDurata: NumeroOre, foreign key (persona) references Persona (id),foreign key (progetto,wp) references WP (progetto,id) )
create table AttivitaNonProgettuale (id: PosInteger, persona: PosInteger, tipo: LavoroNonProgettuale, giorno: date, oreDurata: NumeroOre, foreign key (persona) references Persona (id))
create table Assenza(id: PosInteger, persona: PosInteger, tipo: CausaAssenza, giorno: date, unique (persona,giorno),foreign key (persona) references Persona(id))














