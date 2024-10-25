main string(100) not null as varchar(100)
create domain DataOra not null as timestamp







Utente(cf: varchar, nome: varchar,cognome:varchar)

PeriodoNoleggioVeicolo(inizio:timestamp, fine:timestamp,targa:varchar)


create table Utente(
	cf varchar(100) not null,
	nome varchar(100) not null
	cognome varchar(100) not null
	primary key(cf)
	FK:periodonoleggioveicolo references PeriodoNoleggioVeicolo(targa))
	
	
create table PeriodoNoleggioVeicolo(
	inizio timestamp
	fine timestamp
	targa varchar(100) not null
	primary key (targa)
	FK:utente references Utente(cf)
	FK:periodonoleggioveicolo references PeriodoNoleggioVeicolo(targa))
	
	

create table Sinistro(
	istante timestamp
	id serial 
	primary key(id)
	FK:sinistro references Sinistro(id))
	
