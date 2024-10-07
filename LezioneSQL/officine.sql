CREATE TYPE Indirizzo (via varchar(180), civico varchar(100), cap varchar(100));



CREATE DOMAIN CodiceFiscale as check (value[A-Z][6][0-9](9) [A-Z][0-9]{2}[0-9A-Z{5}$]);
CREATE DOMAIN Stringa as varchar(100);
CREATE DOMAIN Intero as INTEGER check(value>=0);




CREATE TABLE Nazione (nome varchar(100) PRIMARY KEY not null);

CREATE TABLE Regione (
    nome varchar(100) not null, 
    nazione varchar(100) not null,
    PRIMARY KEY(nome, nazione)
    FOREIGN KEY nazione REFERENCES Nazione(nome));



CREATE TABLE Citta (nome varchar(100) not null,
nazione varchar(100) not null, 
regione varchar(100) not null, 
PRIMARY KEY (nome, regione, nazione)
FOREIGN KEY (regione, nazione) REFERENCES Regione(nome, nazione))



CREATE TABLE Marca(nome varchar(100) PRIMARY KEY not null);



CREATE TABLE TipoVeicolo(
    nome varchar(100) PRIMARY KEY not null);



CREATE TABLE Modello (
    nome varchar(100) not null,
    marca varchar(100) not null, 
    tipoVeicolo varchar(100) not null,
    PRIMARY KEY (nome, marca)
    FOREIGN KEY (marca) REFERENCES Marca(nome),
    FOREIGN KEY (tipoveicolo) REFERENCES TipoVeicolo(nome));



CREATE TABLE Veicolo (
    targa varchar(100) PRIMARY KEY not null,
    immatricolazione INTEGER,
    modello varchar(100) not null,
    marca varchar(100) not null,
    tipoVeicolo varchar(100) not null,
    cliente varchar(100) not null,
    PRIMARY KEY (targa),
    FOREIGN KEY modello REFERENCES Modello(nome),
    FOREIGN KEY marca REFERENCES Marca(nome));



    CREATE TABLE Persona (
        cf CodiceFiscale NOT NULL,
        nome varchar(100) NOT NULL,
        indirizzo Indirizzo NOT NULL,
        telefono varchar(100) NOT NULL, 
        città varchar(100) NOT NULL,
        regione varchar(100) NOT NULL,
        nazione varchar(100) NOT NULL,
        PRIMARY KEY (cf),
        FOREIGN KEY (città, regione, nazione) references Città (nome, regione, nazione));




    CREATE TABLE Cliente (
        persona NOT NULL,
        PRIMARY KEY (persona),
        FOREIGN KEY persona references Persona (cf));


    CREATE TABLE Staff (
        persona NOT NULL,
        PRIMARY KEY (persona),
        FOREIGN KEY persona references Persona (cf));


    CREATE TABLE Dipendente (
        persona NOT NULL,
        staff NOT NULL,
        assunzione date NOT NULL
        PRIMARY KEY (staff),
        FOREIGN KEY (persona, staff) references Staff(cf, persona));


    CREATE TABLE Direttore (
        nascita date NOT NULL,
        persona NOT NULL,
        staff NOT NULL,
        PRIMARY KEY (staff),
        FOREIGN KEY (persona, staff) references Staff(cf. persona));


    CREATE TABLE Officina (
        nome varchar(100) NOT NULL,
        indirizzo Indirizzo NOT NULL,
        id INTEGER NOT NULL, PRIMARY KEY (id),
        FOREIGN KEY (città, regione, nazione) references Città (nome, regione,nazione));


    CREATE TABLE Riparazione (
        riconsegna TIMESTAMP NOT NULL,
        codice INTEGER NOT NULL, 
        officina varchar(100) NOT NULL,
        PRIMARY KEY (codice),
        FOREIGN KEY officina references Officina(id));














