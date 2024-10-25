--1. Quali sono le persone con stipendio di al massimo 40000
--euro [2 punti]
select *
from Persona p,
where p.stipendio <= 40000


--2. Quali sono i ricercatori che lavorano ad almeno un
--progetto e hanno uno stipendio di al massimo 40000

select per.nome, per.cognome,per.posizione
from Persona per, Progetto pro, AttivitaProgetto ap
where pro.id = ap.progetto
and per.posizione = 'Ricercatore'
and per.id = ap.persona
group by per.nome, per.cognome,per.posizione



--3. Qual è il budget totale dei progetti nel db [2 punti

select sum(pro.budget)
from Progetto pro


--4. Qual è il budget totale dei progetti a cui lavora ogni
--persona. Per ogni persona restituire nome, cognome e
--budget totale dei progetti nei quali è coinvolto. [3 punti]








--5. Qual è il numero di progetti a cui partecipa ogni
--professore ordinario. Per ogni professore ordinario,
--restituire nome, cognome, numero di progetti nei quali è
--coinvolto [3 punti]

select nome, cognome,
    (select count (distinct progetto)
from AttivitaProgetto
where persona= persona.id) as num_prog
from Persona
where posizione='Professore Ordinario'




--6 Qual è il numero di assenze per malattia di ogni
--professore associato. Per ogni professore associato,
--restituire nume, cognome e numero di assenze per
--malattia [3 punti]


select nome,cognome,
    (select count(*)
    from Assenza
    where persona= Persona.id
    and tipo='Malattia') as num_ass
    from Persona
    where posizione= 'Professore Associato'



-- 7 Qual è il numero totale di ore, per ogni persona, dedicate
--al progetto con id ‘5’. Per ogni persona che lavora al
--progetto, restituire nome, cognome e numero di ore totali
--dedicate ad attività progettuali relative al progetto [4
--punti
select P.nome, P.cognome,
sum(AP.oreDurata) as totale_ore
from Persona P
join AttivitaProgetto AP ON
P.id=AP.persona
where AP.progetto =5
group by P.nome, P.cognome


---8. Qual è il numero medio di ore delle attività progettuali
---svolte da ogni persona. Per ogni persona, restituire nome,
---cognome e numero medio di ore delle sue attività
---progettuali (in qualsivoglia progetto) [3 punti]

select nome,cognome,
(select avg(oreDurata)
from AttivitaProgetto
where persona = 
Persona.id)as media_ore
from Persona


----9. Qual è il numero totale di ore, per ogni persona, dedicate
----alla didattica. Per ogni persona che ha svolto attività
--didattica, restituire nome, cognome e numero di ore totali
--dedicate alla didattica [4 punti]

select
from
where





--10