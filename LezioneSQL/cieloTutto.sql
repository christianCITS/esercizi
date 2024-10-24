--cielo 1
--1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?

select v.codice, v.comp
from Volo v
where durataMinuti > 180;

--2. Quali sono le compagnie che hanno voli che superano le 3 ore?

select distinct v.comp
from Volo v
where v.durataMinuti > 180; 

--3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con codice ‘CIA’ ?

select ap.codice, v.comp
from ArrPart ap
where ap.partenza = 'CIA';

--4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice ‘FCO’ ?

select distinct ap.comp
from ArrPart ap
where ap.arrivo = 'FCO';

--5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’ e arrivano all’aeroporto ‘JFK’ ?

select ap.codice, ap.comp
from ArrPart ap
where ap.partenza = 'FCO'
	and ap.arrivo = 'JFK';

-- 6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’ ?

select distinct ap.comp
from ArrPart ap
where ap.partenza = 'FCO'
	and ap.arrivo = 'JFK';

--7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla città di ‘New York’ ?

select distinct v.comp
from Volo v, LuogoAeroporto la1, LuogoAeroporto la2, ArrPart ap
where v.codice = ap.codice and v.comp = ap.comp
	and ap.partenza = la1.aeroporto
	and ap.arrivo = la2.aeroporto
	and la1.citta = 'Roma'
	and la2.citta = 'New York';

--8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli della compagnia di nome ‘MagicFly’ ?

select distinct a.codice, a.nome, la.citta
from ArrPart ap, Aeroporto a, LuogoAeroporto la
where ap.comp = 'MagicFly' 
	and ap.partenza = la.aeroporto
	and ap.partenza = a.codice;

--9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice del volo, nome della compagnia, e aeroporti di partenza e arrivo.

select ap.codice, ap.comp, ap.partenza, ap.arrivo
from LuogoAeroporto la1, LuogoAeroporto la2, ArrPart ap
where ap.partenza = la1.aeroporto
	and ap.arrivo = la2.aeroporto
	and la1.citta = 'Roma'
	and la2.citta = 'New York';

--10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia, codici dei voli, e aeroporti di partenza, scalo e arrivo.

select ap1.comp, ap1.codice as primocodice, ap1.partenza, ap1.arrivo as scalo, ap2.codice as secondocodice, ap2.arrivo
from LuogoAeroporto la1, LuogoAeroporto la2, ArrPart ap1, ArrPart ap2
where ap1.partenza = la1.aeroporto
	and ap2.arrivo = la2.aeroporto
	and la1.citta = 'Roma'
	and la2.citta = 'New York'
	and ap1.arrivo = ap2.partenza
	and ap1.comp = ap2.comp;

--11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atterrano all'aeroporto 'JFK', e di cui si conosce l'anno di fondazione?

select distinct c.nome
from Compagnia c, Volo v, ArrPart ap
where v.codice = ap.codice and v.comp = ap.comp
	and ap.partenza = 'FCO'
	and c.annoFondaz is not null

-----------------------------------------------------------------------
--cielo2
--1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?

select a.codice, a.nome, count(distinct ap.comp) as num_compagnie
from Aeroporto a, ArrPart ap
where ap.arrivo = a.codice
or ap.partenza = a.codice
group by a.codice, a.nome

--2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno 100 minuti?

select count(ap.codice) as num_voli
from ArrPart ap, Volo v
where ap.partenza = 'HTR'
and v.codice = ap.codice
and v.comp = ap.comp
and v.durataMinuti >= 100;

--3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione nella quale opera?

select la.nazione, count(distinct la.aeroporto) as num_aerop
from LuogoAeroporto la, ArrPart ap
where ap.arrivo = la.aeroporto or ap.partenza = la.aeroporto
and ap.comp = 'Apitalia'
group by la.nazione;

--4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla compagnia ‘MagicFly’ ?

select avg(v.durataMinuti) as media, max(v.durataMinuti) as massimo, min(v.durataMinuti) as minimo
from Volo v
where v.comp = 'MagicFly';

--5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli aeroporti?

select a.codice, a.nome, min(c.annoFondaz)
from Compagnia c, Aeroporto a, ArrPart ap
where a.codice = ap.arrivo or a.codice = ap.partenza
and ap.comp = c.nome
group by a.codice, a.nome;

--6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più voli?

select la.nazione as nazione_partenza, count(distinct la2.nazione) as numero_nazioni_arrivo
from LuogoAeroporto la1, LuogoAeroporto la2, ArrPart ap1, ArrPart ap2
where la1.aeroporto = ap1.partenza 
and la2.aeroporto = ap.2arrivo
and ap1.arrivo = ap2.partenza
group by la1.nazione;
-- come faccio a considerare anche tratte con più di uno scalo? 

--7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?

select a.codice, a.nome, avg(v.durataMinuti) as durata_media
from Aeroporto a, Volo v, ArrPart ap
where a.codice = ap.arrivo or a.codice = ap.partenza
and v.codice = ap.codice and v.comp = ap.comp
group by a.codice, a.nome;

--8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate a partire dal 1950?

select c.nome, sum(v.durataMinuti) as durata_complessiva
from Volo v, Compagnia c
where v.comp = c.nome
group by c.nome
having c.annoFondaz >= 1950;

--9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?

select a.codice, a.nome
from Aeroporto a, ArrPart ap
where a.codice = ap.arrivo or a.codice = ap.partenza
group by a.codice, a.nome
having count(distinct ap.comp) = 2;

--10. Quali sono le città con almeno due aeroporti?

select la.citta
from LuogoAeroporto la
group by la.citta
having count(la.aeroporto) >= 2;

--11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6 ore?

select c.nome
from Compagnia c, Volo v
where v.comp = c.nome
group by c.nome
having avg(v.durataMinuti) > 360;

--12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100 minuti?

select v.comp
from Volo v
group by v.comp
having min(v.durataMinuti) >100;

-----------------------------------------------------------------------
--cielo3
/*1. Qual è la durata media, per ogni compagnia, dei voli che partono da un aeroporto
situato in Italia?*/
select v.comp,
    avg(v.durataMinuti)
from Volo v, Luogoaeroporto la , ArrPart ap
where v.codice = ap.codice
and ap.partenza = la.aeroporto
and la.nazione = 'Italy'
group by v.comp

/*2. Quali sono le compagnie che operano voli con durata media maggiore della durata
media di tutti i voli?*/

with q as(
    select avg(v.durataMinuti) as media
    from Volo v
),
q1 as (select v.comp,
    avg(v.durataMinuti) as media
from Volo v, q
group by v.comp)
select q1.comp ,q1.media
from q1, q
where q1.media > q.media





/*3. Quali sono le città dove il numero totale di voli in arrivo è maggiore del numero
medio dei voli in arrivo per ogni città?*/

with q as(
    select la.citta,
    count(la.citta) as voli
    from Luogoaeroporto la, ArrPart ap
    where ap.arrivo = la.aeroporto
    group by la.citta
),
q1 as (
    select avg(voli) as media
    from q
)
select q.citta, q.voli
from q, q1
where q.voli > q1.media

/*4. Quali sono le compagnie aeree che hanno voli in partenza da aeroporti in Italia con
una durata media inferiore alla durata media di tutti i voli in partenza da aeroporti
in Italia?*/
with q as (
    select v.comp,
        avg(v.durataMinuti) as media_comp
    from Volo v, Luogoaeroporto la, ArrPart ap
    where ap.partenza = la.aeroporto
    and ap.codice = v.codice
    and la.nazione = 'Italy'
    group by v.comp
),
q1 as (select avg(v.durataMinuti) as media
from Volo v, Luogoaeroporto la, ArrPart ap
where ap.partenza = la.aeroporto
and ap.codice = v.codice
and la.nazione = 'Italy')

select q.comp, q.media_comp
from q, q1
where q.media_comp < q1.media

/*5. Quali sono le città i cui voli in arrivo hanno una durata media che differisce di più
di una deviazione standard dalla durata media di tutti i voli? Restituire città e
durate medie dei voli in arrivo*/


with q as (
    select la.citta, 
        avg(v.durataMinuti) as media_arrivo
    from Volo v, LuogoAeroporto la, ArrPart ap
    where ap.arrivo = la.aeroporto
    and ap.codice = v.codice
    group by la.citta
    ),
q1 as (
    select avg(v.durataMinuti) as media
    from Volo v
    ),
q2 as (
    select stddev(q.media_arrivo) as stddev
    from q
)

select q.citta, q.media_arrivo
from q, q1, q2
where (q.media_arrivo > (q1.media + q2.stddev)
or q.media_arrivo < (q1.media - q2.stddev))

--6. Quali sono le nazioni che hanno il maggior numero di città dalle quali partono voli
--diretti in altre nazioni?

with NumCIttaPerNazione as(
select la_part.nazione, count(Distinct la_part.citta) as num_citta
	from luogoaeroporto la_part, arrpart ap, luogoaeroporto la_arr
	where la_part.aeroporto = ap.partenza
		and ap.arrivo = la_arr.aeroporto
		and la_part.nazione <> la_arr.nazione
	group by la_part.nazione
	),
MaxVoli as (
		select max(num_citta) as max_num_citta
		from NumCittaPerNazione
		)
select n.nazione
from NumCittaPerNazione n, MaxVoli max
where n.num_citta = max.max_num_citta
