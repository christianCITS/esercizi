CREATE TABLE case_in_vendita (
    catastale VARCHAR(20) PRIMARY KEY,
    indirizzo VARCHAR(100),
    numero_civico INT,
    piano INT,
    metri INT,
    vani INT,
    prezzo DECIMAL(10, 2),
    stato ENUM('LIBERO', 'OCCUPATO'),
    filiale_proponente VARCHAR(20),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);




CREATE TABLE case_in_affitto (
    catastale VARCHAR(20) PRIMARY KEY,
    indirizzo VARCHAR(100),
    numero_civico INT,
    tipo_affitto ENUM('PARZIALE', 'TOTALE'),
    bagno_personale BOOLEAN,
    prezzo_mensile DECIMAL(10, 2),
    filiale_proponente VARCHAR(20),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);




CREATE TABLE filiali (
    partita_iva VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(50),
    indirizzo_sede VARCHAR(100),
    civico INT,
    telefono VARCHAR(20)
);





CREATE TABLE vendite_casa (
    catastale VARCHAR(20),
    data_vendita DATE,
    filiale_proponente VARCHAR(20),
    filiale_venditrice VARCHAR(20),
    prezzo_vendita DECIMAL(10, 2),
    PRIMARY KEY (catastale, data_vendita),
    FOREIGN KEY (catastale) REFERENCES case_in_vendita(catastale),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva)
);



CREATE TABLE affitti_casa (
    catastale VARCHAR(20),
    data_affitto DATE,
    filiale_proponente VARCHAR(20),
    filiale_venditrice VARCHAR(20),
    prezzo_affitto DECIMAL(10, 2),
    durata_contratto INT, 
    PRIMARY KEY (catastale, data_affitto),
    FOREIGN KEY (catastale) REFERENCES case_in_affitto(catastale),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva)
);



