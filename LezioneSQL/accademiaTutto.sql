--accademia4
--1. Quali sono i cognomi distinti di tutti gli strutturati?
select distinct Persona.cognome
from Persona;
--2. Quali sono i Ricercatori (con nome e cognome)?
select nome, cognome
from Persona 
where posizione = 'Ricercatore';
--3. Quali sono i Professori Associati il cui cognome comincia con la lettera ‘V’ ?
select nome, cognome
from Persona 
where posizione = 'Professore Associato' and cognome like 'V%';
--4. Quali sono i Professori (sia Associati che Ordinari) il cui cognome comincia con la lettera ‘V’ ?
select nome, cognome
from Persona 
where (posizione = 'Professore Associato' or posizione = 'Professore Ordinario') and cognome like 'V%';
--5. Quali sono i Progetti già terminati alla data odierna?
select *
from Progetto 
where fine < current_date;
--6. Quali sono i nomi di tutti i Progetti ordinati in ordine crescente di data di inizio?
select nome
from Progetto 
order by inizio asc;
--7. Quali sono i nomi dei WP ordinati in ordine crescente (per nome)?
select nome
from WP 
order by nome asc;
--8. Quali sono (distinte) le cause di assenza di tutti gli strutturati?
select distinct tipo
from Assenza;
--9. Quali sono (distinte) le tipologie di attività di progetto di tutti gli strutturati?
select distinct tipo
from AttivitaProgetto;
--10. Quali sono i giorni distinti nei quali del personale ha effettuato attività non progettuali di tipo ‘Didattica’ ? Dare il risultato in ordine crescente.
select distinct giorno
from AttivitaNonProgettuale
where tipo = 'Didattica'
order by giorno asc;

-----------------------------------------------------------------------
--accademia 5
--1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome ‘Pegasus’?

select wp.nome, wp.inizio, wp.fine 
from Progetto p, WP wp
where p.nome = 'Pegasus' and wp.progetto = p.id;

--2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?

select distinct per.nome, per.cognome, per.posizione
from Persona per, Progetto pro, AttivitaProgetto attpro
where pro.nome = 'Pegasus' 
and (attpro.persona = per.id) 
and (attpro.progetto = pro.id)
order by per.cognome desc;

--3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di una attività nel progetto ‘Pegasus’ ?

select distinct per.nome, per.cognome, per.posizione
from Persona per, Progetto pro, AttivitaProgetto attpro1, AttivitaProgetto attpro2
where attpro1.id <> attpro2.id
and attpro1.persona = attpro2.persona
and attpro1.progetto = pro.id 
and attpro2.progetto = pro.id 
and pro.nome = 'Pegasus'
and attpro1.persona = per.id 

--4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno fatto almeno una assenza per malattia?

select distinct p.nome, p.cognome, p.posizione
from Assenza a, Persona p
where p.posizione = 'Professore Ordinario' and a.persona = p.id and a.tipo = 'Malattia';

--5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno fatto più di una assenza per malattia?

select distinct p.nome, p.cognome, p.posizione
from Assenza a1, Assenza a2, Persona p
where p.posizione = 'Professore Ordinario' 
and a1.persona = p.id
and a1.tipo = 'Malattia'
and a2.tipo = 'Malattia'
and a1.persona = a2.persona
and a1.giorno <> a2.giorno;

--6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno un impegno per didattica?

select distinct p.nome, p.cognome, p.posizione
from Persona p, AttivitaNonProgettuale anp
where p.posizione = 'Ricercatore' and anp.persona = p.id and anp.tipo = 'Didattica';

--7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un impegno per didattica?

select distinct p.nome, p.cognome, p.posizione
from Persona p, AttivitaNonProgettuale anp1, AttivitaNonProgettuale anp2 
where p.posizione = 'Ricercatore' 
and anp1.persona = p.id 
and anp1.tipo = 'Didattica'
and ((anp1.persona) = (anp2.persona) and (anp1.giorno <> anp2.giorno));

--8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia attività progettuali che attività non progettuali?

select distinct p.nome, p.cognome
from Persona p, AttivitaProgetto ap, AttivitaNonProgettuale anp 
where p.id = ap.persona and p.id = anp.persona
and (ap.persona = anp.persona and anp.giorno = ap.giorno);

--9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia attività progettuali che attività non progettuali? Si richiede anche di proiettare il giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di entrambe le attività.

select p.nome, p.cognome
from Persona p
where

--10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono assenti e hanno attività progettuali?

select p.nome, p.cognome
from Persona p, AttivitaProgetto ap, Assenza a
where p.id = ap.persona
and p.id = a.persona
and ap.giorno = a.giorno

--11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il nome del progetto, la causa di assenza e la durata in ore della attività progettuale.

select p.nome, p.cognome, ap.giorno, a.tipo, pg.nome, ap.oreDurata
from Persona p, AttivitaProgetto ap, Assenza a, Progetto pg
where p.id = ap.persona
and p.id = a.persona
and pg.id = ap.progetto
and ap.giorno = a.giorno

--12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?

SELECT distinct wp1.nome, wp1.id, wp2.id
FROM WP wp1, WP wp2
WHERE wp1.nome = wp2.nome
AND wp1.progetto <> wp2.progetto

-----------------------------------------------------------------------
--accademia6
--1. Quanti sono gli strutturati di ogni fascia?

select p.posizione, count (*) as numero
from Persona p
group by p.posizione;

--2. Quanti sono gli strutturati con stipendio ≥ 40000?

select count (*) as numero
from Persona p
where p.stipendio >= 40000;

--3. Quanti sono i progetti già finiti che superano il budget di 50000?

select count(*) as numero
from Progetto p
where p.budget > 50000;

--4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’ ?

select avg(ap.oreDurata) as media, min(ap.oreDurata) as minimo, max(ap.oreDurata) as massimo
from Progetto p, AttivitaProgetto ap
where p.nome = 'Pegasus'
and p.id = ap.id;

--5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto ‘Pegasus’ da ogni singolo docente?

select per.id as id_persona, per.nome, per.cognome, avg(ap1.oreDurata) as media, min(ap1.oreDurata) as minimo, max(ap1.oreDurata) as massimo
from Persona per, Progetto p, AttivitaProgetto ap1, AttivitaProgetto ap2
where p.nome = 'Pegasus'
and p.id = ap1.id
and per.posizione = 'Professore Ordinario' or per.posizione = 'Professore Associato'
group by per.id, per.nome, per.cognome;

--6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?

select per.id, per.nome, per.cognome, sum(anp.oreDurata) as ore_didattica
from Persona per, AttivitaNonProgettuale anp
where per.id = anp.persona
and anp.tipo = 'Didattica'
group by per.id, per.nome, per.cognome;

--7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?

select avg(per.stipendio) as media, min(per.stipendio) as minimo, max(per.stipendio) as massimo
from Persona per
where per.posizione = 'Ricercatore';

--8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori associati e dei professori ordinari?

select avg(per.stipendio) as media, min(per.stipendio) as minimo, max(per.stipendio) as massimo
from Persona per
group by per.posizione;

--9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?

select pro.id, pro.nome, sum(ap.oreDurata) as totale_ore
from Persona per, AttivitaProgetto ap, Progetto pro
where per.nome = 'Ginevra' 
and per.cognome = 'Riva' 
and ap.persona = per.id
and pro.id = ap.progetto
group by pro.id, pro.nome;

--10. Qual è il nome dei progetti su cui lavorano più di due strutturati?

select pro.id, pro.nome
from Progetto pro, AttivitaProgetto ap
where pro.id = ap.progetto
group by pro.id, pro.nome 
having count (ap.persona) > 2;

--11. Quali sono i professori associati che hanno lavorato su più di un progetto?

select per.id, per.nome, per.cognome
from Persona per, Progetto pro, AttivitaProgetto ap
where pro.id = ap.progetto
and per.posizione = 'Professore Associato'
and per.id = ap.persona
group by per.id, per.nome, per.cognome

-----------------------------------------------------------------------
--accademia7
--1. Qual è media e deviazione standard degli stipendi per ogni categoria di strutturati?

select p.posizione, avg(p.stipendio) as media, stddev(p.stipendio) as dev_standard
from Persona p
group by p.posizione;

--2. Quali sono i ricercatori (tutti gli attributi) con uno stipendio superiore alla media della loro categoria?

select p.id, p.nome, p.cognome, p.posizione, p.stipendio
from Persona p, (
select avg(p.stipendio) as media
from Persona p
where p.posizione = 'Ricercatore'
) as q
where p.stipendio > q.media
and p.posizione = 'Ricercatore';

--3. Per ogni categoria di strutturati quante sono le persone con uno stipendio che differisce di al massimo una deviazione standard dalla media della loro categoria?

select per.posizione, count(per) as numero
from Persona per, (
select per.posizione, avg(per.stipendio) as media, stddev(per.stipendio) as dev_standard
from Persona per
group by per.posizione
) as q
where per.posizione = q.posizione
and per.stipendio <= (q.media + q.dev_standard)
and per.stipendio >= (q.media - q.dev_standard)
group by per.posizione;

--4. Chi sono gli strutturati che hanno lavorato almeno 20 ore complessive in attività progettuali? Restituire tutti i loro dati e il numero di ore lavorate.

select per.id, per.nome, per.cognome, per.posizione, per.stipendio, sum(ap.oreDurata)
from Persona per, AttivitaProgetto ap
where ap.persona = per.id
group by per.id, per.nome, per.cognome, per.posizione, per.stipendio
having sum(ap.oreDurata) >= 20;

--5. Quali sono i progetti la cui durata è superiore alla media delle durate di tutti i progetti? Restituire nome dei progetti e loro durata in giorni.

with Stats as (
select avg(pro.fine-pro.inizio) as media
from Progetto pro
)
select pro.nome, fine-inizio as durata_giorni
from Progetto pro, Stats s
where (pro.fine - pro.inizio) > s.media;

--6. Quali sono i progetti terminati in data odierna che hanno avuto attività di tipo “Dimostrazione”? Restituire nome di ogni progetto e il numero complessivo delle ore dedicate a tali attività nel progetto.

select p.id, p.nome, sum(ap.oreDurata) as durata_ore
from Progetto p, AttivitaProgetto ap
where ap.progetto = p.id
and p.fine <= current_date
and ap.tipo = 'Dimostrazione'
group by p.id, p.nome;

--7. Quali sono i professori ordinari che hanno fatto più assenze per malattia del numero di assenze medio per malattia dei professori associati? Restituire id, nome e cognome del professore e il numero di giorni di assenza per malattia.

select per.id, per.nome, per.cognome, count(a.tipo) as n_assenze_malattia
from Persona per, Assenza a, (
select count(ass.tipo) as tot
from Persona p, Assenza ass
where ass.persona = p.id 
and ass.tipo = 'Malattia'
and p.posizione = 'Professore Associato'
) as q
where a.persona = per.id 
and per.posizione = 'Professore Ordinario'
and a.tipo = 'Malattia'
group by per.id, per.nome, per.cognome, q.tot
having count(a.tipo) > avg(q.tot);