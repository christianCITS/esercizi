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
    nome varchar(100) not null
    marca varchar(100) not null, 
    tipoveicolo varchar(100) not null
    PRIMARY KEY (nome, marca)
    FOREIGN KEY (marca) REFERENCES Marca(nome),
    FOREIGN KEY (tipoveicolo) REFERENCES TipoVeicolo(nome));


CREATE TABLE Veicolo (
    targa varchar(100) PRIMARY KEY not null,
    immatricolazione INTEGER,
    modello varchar(100) not null,
    FOREIGN KEY (modello) REFERENCES Modello(nome));